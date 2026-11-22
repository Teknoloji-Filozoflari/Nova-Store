# Signed catalog publish

Nova must **not** blindly fetch a remote catalog. Every published catalog is a
GitHub Release asset pair that matches Nova's client
(`src/store/remote.rs`):

| Asset | Purpose |
|-------|---------|
| `store-catalog.toml` | Aggregated apps from `apps/**/*.toml` in Nova `StoreFile` shape (`[[apps]]`, Turkish category labels) |
| `store-catalog.toml.minisig` | Detached minisign signature over the exact bytes of `store-catalog.toml` |

Also uploaded for tooling (not required by Nova's runtime client):

| Asset | Purpose |
|-------|---------|
| `catalog.json` | Schema v1 JSON aggregate (`scripts/build_catalog.py`) |
| `catalog.json.minisig` | Signature over `catalog.json` (when signing) |

Nova pins the Nova-Store **public key** (see [`keys/`](../keys/)) and verifies
the signature before replacing its in-memory catalog. On failure it keeps the
last trusted catalog (or the embedded `assets/store` snapshot).

Default download URLs (override with `NOVA_STORE_CATALOG_URL` /
`NOVA_STORE_CATALOG_SIG_URL`):

```text
https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml
https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml.minisig
```

## Trust model

1. Contributors PR TOML under `apps/<category>/`.
2. CI validates schema, unique ids, SPDX, source URL, install method, OS/arch,
   privilege, and trust class rules.
3. Maintainers merge to `main`.
4. The **Publish signed catalog** workflow (tag `catalog-v*` or
   `workflow_dispatch`) builds `store-catalog.toml` (+ `catalog.json`), signs
   when `MINISIGN_SECRET_KEY` is set, and uploads both files to the GitHub
   Release (marked latest).
5. Nova clients fetch `releases/latest`, verify, then apply.

Signing keys never live in this repository. Only the **public** verification
material is committed under `keys/`.

## Secrets

| Name | Required for | Value |
|------|--------------|-------|
| `MINISIGN_SECRET_KEY` | Signed GitHub Release | Full contents of the minisign **secret** key file whose public half is `keys/minisign.pub` |

Without the secret, the workflow still **builds** `store-catalog.toml` /
`catalog.json` and uploads them as Actions artifacts (dry-run / unsigned). It
does **not** create a GitHub Release until the secret is present and signing
succeeds.

The public key in `keys/minisign.pub` must match Nova's pin:

```text
RWTq0P6AM5pR0HlqD09S6QW1Yf0X5sIWRah5Q1UQDMJFBxzzI/GuCNpg
```

## Option A — minisign (default / Nova path)

### One-time key generation (maintainer laptop)

Only when **rotating** (coordinate a Nova pubkey bump in the same train):

```bash
minisign -G -W -p keys/minisign.pub -s nova-store.key
# Store nova-store.key offline. Commit keys/minisign.pub.
# Update Nova NOVA_STORE_CATALOG_PUBLIC_KEY + assets/keys/nova-store-catalog.pub.
```

`-W` writes an unencrypted secret key suitable for Actions (no password prompt).

### Build + sign locally

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_catalog.py
mkdir -p dist
python3 scripts/build_store_catalog_toml.py -o dist/store-catalog.toml
python3 scripts/build_catalog.py -o dist/catalog.json
minisign -S -s /path/to/nova-store.key -W -m dist/store-catalog.toml -x dist/store-catalog.toml.minisig
minisign -Vm dist/store-catalog.toml -p keys/minisign.pub -x dist/store-catalog.toml.minisig
```

### Verify (what Nova does)

```bash
minisign -Vm dist/store-catalog.toml -p keys/minisign.pub -x dist/store-catalog.toml.minisig
```

The publish workflow uses repository secret `MINISIGN_SECRET_KEY` and writes
`store-catalog.toml.minisig`.

## Option B — cosign (tooling only)

Cosign remains documented for JSON aggregate tooling. Nova's runtime client
verifies **minisign** over `store-catalog.toml` only.

### Key-based

```bash
cosign generate-key-pair   # cosign.key / cosign.pub
cosign sign-blob --key cosign.key --output-signature catalog.json.sig catalog.json
cosign verify-blob --key keys/cosign.pub --signature catalog.json.sig catalog.json
```

### Keyless (Fulcio / Rekor)

```bash
cosign sign-blob --yes --output-signature catalog.json.sig \
  --output-certificate catalog.json.pem catalog.json
# Verify with certificate identity + OIDC issuer constraints published in keys/cosign-identity.json
cosign verify-blob --certificate catalog.json.pem \
  --signature catalog.json.sig \
  --certificate-identity-regexp 'https://github.com/Teknoloji-Filozoflari/Nova-Store/.*' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  catalog.json
```

## Dry-run

- **Always-on job:** every publish workflow run includes a **Dry-run build
  (unsigned)** job that validates + builds `store-catalog.toml` /
  `catalog.json` and uploads Actions artifacts — no secret required.
- **Manual:** Actions → Publish signed catalog → Run workflow with
  `dry_run=true` (default). Only the dry-run job runs.
- **Publish attempt:** set `dry_run=false` on `workflow_dispatch`, or push a
  `catalog-v*` tag. Signing + Release happen only when `MINISIGN_SECRET_KEY`
  is set.

## How Nova consumes

1. Pin `keys/minisign.pub` into the Nova binary (`NOVA_STORE_CATALOG_PUBLIC_KEY`).
2. GET `releases/latest/download/store-catalog.toml` + `.minisig` over HTTPS.
3. Verify signature with the pinned key.
4. Parse as `StoreFile` (`[[apps]]`); reject unknown categories / invalid entries.
5. On any failure: keep the previous trusted catalog / embedded snapshot and
   surface a non-fatal “catalog update skipped” status (`KeptTrusted`).
6. Map trust via install method (A/B/C/D derived in Nova); class C shows a
   risk note on install confirm.

Embedded / last-known-good catalog remains the offline fallback.

## Tagging the first / next catalog release

After this workflow is on `main` and `MINISIGN_SECRET_KEY` is configured:

```bash
git checkout main
git pull
git tag -a catalog-v0.1.0 -m "catalog v0.1.0 — first signed store-catalog.toml"
git push origin catalog-v0.1.0
```

Confirm the Release lists **`store-catalog.toml`** and
**`store-catalog.toml.minisig`**, and that
`…/releases/latest/download/store-catalog.toml` resolves.

Then in Nova: Mağaza → `U` (or boot refresh) should move from `KeptTrusted`
(404) to `Updated` when the signature verifies.

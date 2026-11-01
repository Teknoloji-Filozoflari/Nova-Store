# Signed catalog publish

Nova must **not** blindly fetch a remote catalog. Every published catalog is a
GitHub Release asset pair:

| Asset | Purpose |
|-------|---------|
| `catalog.json` | Aggregated apps from `apps/**/*.toml` (`schema_version = 1`) |
| `catalog.json.minisig` **or** `catalog.json.sig` | Detached signature over the exact bytes of `catalog.json` |

Nova pins the Nova-Store **public key** (see [`keys/`](../keys/)) and verifies
the signature before replacing its in-memory catalog. On failure it keeps the
last trusted catalog.

## Trust model

1. Contributors PR TOML under `apps/<category>/`.
2. CI validates schema, unique ids, SPDX, source URL, install method, OS/arch,
   privilege, and trust class rules.
3. Maintainers merge to `main`.
4. The **Publish catalog** workflow (tag `catalog-v*`) builds `catalog.json`,
   signs it, and uploads both files to the GitHub Release.
5. Nova clients fetch the latest `catalog-v*` release, verify, then apply.

Signing keys never live in this repository. Only the **public** verification
material is committed under `keys/`.

## Option A — minisign (default)

### One-time key generation (maintainer laptop)

```bash
minisign -G -p nova-store.pub -s nova-store.key
# Store nova-store.key in a password manager / hardware token offline.
# Commit nova-store.pub as keys/minisign.pub
```

### Sign a release artifact

```bash
python3 scripts/build_catalog.py -o dist/catalog.json
minisign -S -s /path/to/nova-store.key -m dist/catalog.json -x dist/catalog.json.minisig
```

### Verify (what Nova does)

```bash
minisign -Vm dist/catalog.json -p keys/minisign.pub -x dist/catalog.json.minisig
```

The publish workflow uses repository secret `MINISIGN_SECRET_KEY` (contents of
`nova-store.key`) and writes `catalog.json.minisig`.

## Option B — cosign (keyless or key-based)

### Key-based

```bash
cosign generate-key-pair   # cosign.key / cosign.pub
cosign sign-blob --key cosign.key --output-signature catalog.json.sig catalog.json
cosign verify-blob --key keys/cosign.pub --signature catalog.json.sig catalog.json
```

### Keyless ( Fulcio / Rekor )

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

When using cosign, the release uploads `catalog.json`, `catalog.json.sig`, and
(optionally) `catalog.json.pem`. Set workflow input / secret
`SIGNING_METHOD=cosign`.

## How Nova should consume

1. Pin `keys/minisign.pub` (or cosign pub / identity) into the Nova binary or a
   first-run trusted store.
2. GET the latest GitHub Release with tag matching `catalog-v*` from
   `Teknoloji-Filozoflari/Nova-Store`.
3. Download `catalog.json` + signature asset over HTTPS.
4. Verify signature with the pinned key.
5. Validate `schema_version`, unique ids, and reject unsigned field mutations.
6. On any failure: keep the previous trusted catalog and surface a non-fatal
   “catalog update skipped” status.
7. Map `trust_class` A/B/C/D to UI badges; never treat A and B as equivalent.
   Class C must show `risk_note` on the install confirm screen.

Embedded / last-known-good catalog remains the offline fallback.

## Tagging a catalog release

```bash
git tag -a catalog-v0.1.0 -m "catalog v0.1.0"
git push origin catalog-v0.1.0
```

The `publish-catalog.yml` workflow runs on `catalog-v*` tags only.

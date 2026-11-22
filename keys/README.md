# Catalog verification keys

| File | Purpose |
|------|---------|
| `minisign.pub` | Public key Nova pins to verify `store-catalog.toml.minisig` |
| `cosign-identity.json` | Expected identity constraints for keyless cosign (optional) |

**Never commit private keys.** Publish workflow reads `MINISIGN_SECRET_KEY`
from GitHub Actions secrets. Rotation: generate a new pair, update this
directory **and** Nova's pinned key (`NOVA_STORE_CATALOG_PUBLIC_KEY` /
`assets/keys/nova-store-catalog.pub`), then cut a new `catalog-v*` release.

## Alignment with Nova

The base64 line in `minisign.pub` **must** match Nova's embedded pin:

```text
RWTq0P6AM5pR0HlqD09S6QW1Yf0X5sIWRah5Q1UQDMJFBxzzI/GuCNpg
```

(see `Teknoloji-Filozoflari/Nova` → `src/store/remote.rs`).

## Maintainer: set the signing secret

1. Prefer the existing keypair that matches the pubkey above (offline /
   password manager). If rotating, run:

   ```bash
   minisign -G -W -p keys/minisign.pub -s nova-store.key
   # then bump Nova's pinned pubkey in the same release train
   ```

2. Repo → Settings → Secrets and variables → Actions → New repository secret:
   - Name: `MINISIGN_SECRET_KEY`
   - Value: **full file contents** of `nova-store.key` (including the
     `untrusted comment:` line)

3. Dry-run first: Actions → **Publish signed catalog** → Run workflow with
   `dry_run=true` (default). Confirm `store-catalog.toml` artifact builds.

4. Cut a signed release (see `docs/catalog-signing.md`).

# Catalog verification keys

| File | Purpose |
|------|---------|
| `minisign.pub` | Public key Nova pins to verify `catalog.json.minisig` |
| `cosign-identity.json` | Expected identity constraints for keyless cosign (optional) |

**Never commit private keys.** Publish workflow reads `MINISIGN_SECRET_KEY`
from GitHub Actions secrets. Rotation: generate a new pair, update this
directory + Nova's pinned key, then cut a new `catalog-v*` release.

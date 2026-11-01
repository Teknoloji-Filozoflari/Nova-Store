# Nova-Store

Signed, PR-reviewed application catalog for
[Nova](https://github.com/Teknoloji-Filozoflari/Nova).

Contributors add apps here; Nova fetches **signed** release artifacts only and
falls back to the last trusted catalog if verification fails.

## Layout

```
apps/
  development/   networking/   system/
  security/      containers/   productivity/
schema/
  app.schema.json      # per-app JSON Schema (trust A–D, privilege, …)
  catalog.schema.json  # published aggregate
metadata/
  categories.toml
  trust-classes.toml
  catalog.json         # built aggregate
scripts/
  validate_catalog.py
  build_catalog.py
keys/
  minisign.pub         # public verify key (secret key is NOT in git)
docs/
  catalog-signing.md
  nova-consumption.md
```

## Validate

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_catalog.py
python3 scripts/build_catalog.py
```

## Trust classes

| Class | Meaning |
|-------|---------|
| **A** | Distro / official package manager (`apt`/`dnf`/`pacman`/`brew`) |
| **B** | Project official binary (`download_archive`, signature preferred) |
| **C** | Registry (`cargo`/`npm`/`pipx`/`uv`) — requires `risk_note` |
| **D** | Manual docs only |

## How Nova consumes

See [docs/nova-consumption.md](docs/nova-consumption.md) and
[docs/catalog-signing.md](docs/catalog-signing.md).

Short version: pin `keys/minisign.pub`, download the latest GitHub Release
`catalog-v*` assets (`catalog.json` + `.minisig`), verify, then apply; on
failure keep the previous trusted catalog.

## License

MIT — see [LICENSE](LICENSE).

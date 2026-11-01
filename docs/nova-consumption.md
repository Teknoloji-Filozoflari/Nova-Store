# How Nova consumes Nova-Store

Repository: https://github.com/Teknoloji-Filozoflari/Nova-Store

## Source of truth

| Path | Role |
|------|------|
| `apps/<category>/<id>.toml` | One app per file; contributors PR here |
| `schema/app.schema.json` | Entry schema (trust classes A–D, privilege, SPDX, …) |
| `metadata/catalog.json` | Built aggregate (also regenerated on publish) |
| `keys/minisign.pub` | Pinned public key for catalog signature verify |
| GitHub Release `catalog-v*` | Signed publish channel |

## Client flow

```
Nova boot
  └─ load last trusted catalog (embedded or disk cache)
  └─ (optional) fetch latest catalog-v* release
        ├─ verify minisign/cosign over catalog.json
        ├─ schema_version == 1 && structural checks
        └─ replace trusted catalog OR keep previous on failure
```

Do **not** fetch raw `main` TOML at runtime for install decisions. Only the
signed release artifact is authoritative.

## Field mapping (Nova-Store → Nova `StoreEntry`)

| Nova-Store | Nova today | Notes |
|------------|------------|-------|
| `category` (`development`, …) | Turkish `category` via `metadata/categories.toml` `nova_label` | Map slug → label in loader |
| `trust_class` | new | Distinct from archive `TrustLevel` hash/sig badge |
| `privilege` | derived from method today | Prefer explicit flag |
| `risk_note` | new (class C) | Show on confirm |
| `install_method` / `install_command` / artifacts | same | Keep argv shell-free rules |

## Categories

Full Nova mağaza set (18), mirrored under `apps/<slug>/` with Turkish labels
in `metadata/categories.toml`:

`ai`, `git`, `files`, `development`, `editors`, `system`, `panels`,
`networking`, `containers`, `database`, `security`, `media`, `messaging`,
`productivity`, `games`, `screensavers`, `web`, `daily`

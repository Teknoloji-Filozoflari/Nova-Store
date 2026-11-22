# How Nova consumes Nova-Store

Repository: https://github.com/Teknoloji-Filozoflari/Nova-Store

## Source of truth

| Path | Role |
|------|------|
| `apps/<category>/<id>.toml` | One app per file; contributors PR here |
| `schema/app.schema.json` | Entry schema (trust classes A–D, privilege, SPDX, …) |
| `metadata/catalog.json` | Built JSON aggregate (also regenerated on publish) |
| `scripts/build_store_catalog_toml.py` | Builds Nova-facing `store-catalog.toml` |
| `keys/minisign.pub` | Pinned public key for catalog signature verify |
| GitHub Release `catalog-v*` (latest) | Signed publish channel |

## Client flow

```
Nova boot
  └─ load last trusted catalog (embedded or disk cache)
  └─ (optional) fetch releases/latest store-catalog.toml + .minisig
        ├─ verify minisign with pinned pubkey
        ├─ parse StoreFile [[apps]] + structural checks
        └─ replace trusted catalog OR keep previous on failure (KeptTrusted)
```

Do **not** fetch raw `main` TOML at runtime for install decisions on the
signed path. Only the signed release artifact is authoritative for remote
refresh. (Nova also has an optional unsigned `main` repo-sync path that is
labeled separately.)

## Release asset contract

| Asset | Required by Nova? |
|-------|-------------------|
| `store-catalog.toml` | **Yes** |
| `store-catalog.toml.minisig` | **Yes** |
| `catalog.json` (+ `.minisig`) | No (tooling / SSOT JSON) |

URLs (defaults in `Nova` `src/store/remote.rs`):

```text
https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml
https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml.minisig
```

Env overrides: `NOVA_STORE_CATALOG_URL`, `NOVA_STORE_CATALOG_SIG_URL`,
`NOVA_STORE_CATALOG_DISABLE_REMOTE=1`.

Pinned pubkey (must match `keys/minisign.pub`):

```text
RWTq0P6AM5pR0HlqD09S6QW1Yf0X5sIWRah5Q1UQDMJFBxzzI/GuCNpg
```

## Field mapping (Nova-Store → Nova `StoreEntry`)

| Nova-Store | Nova today | Notes |
|------------|------------|-------|
| `category` (`development`, …) | Turkish `category` via `metadata/categories.toml` `nova_label` | Mapped in `build_store_catalog_toml.py` |
| `trust_class` / `privilege` / `risk_note` | derived / UI | Omitted from `store-catalog.toml`; Nova derives A–D from method + signature |
| `install_method` / `install_command` / artifacts | same | Keep argv shell-free rules |
| `[[artifacts]]` | `[[apps.artifacts]]` | Nested under each `[[apps]]` table |

## Categories

Full Nova mağaza set (18), mirrored under `apps/<slug>/` with Turkish labels
in `metadata/categories.toml`:

`ai`, `git`, `files`, `development`, `editors`, `system`, `panels`,
`networking`, `containers`, `database`, `security`, `media`, `messaging`,
`productivity`, `games`, `screensavers`, `web`, `daily`

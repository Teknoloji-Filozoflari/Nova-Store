# Contributing to Nova-Store

This repository owns the **installable app catalog** for
[Nova](https://github.com/Teknoloji-Filozoflari/Nova). Contribute apps here —
not in the Nova Rust tree.

## Quick path: add an app

1. Pick a category directory under `apps/` (must match
   `metadata/categories.toml`): `ai`, `git`, `files`, `development`,
   `editors`, `system`, `panels`, `networking`, `containers`, `database`,
   `security`, `media`, `messaging`, `productivity`, `games`,
   `screensavers`, `web`, `daily`.
2. Create `apps/<category>/<id>.toml` (filename stem **must** equal `id`).
3. Fill required fields (see `schema/app.schema.json`).
4. Run validation locally:

   ```bash
   python3 -m pip install -r requirements-dev.txt
   python3 scripts/validate_catalog.py
   ```

5. Open a pull request. CI must pass before merge.

## Required fields

| Field | Rule |
|-------|------|
| `id` | Unique, `^[a-z0-9][a-z0-9._-]*$` |
| `source` | `https://` project / homepage URL |
| `license` | SPDX id or simple `AND`/`OR`/`WITH` expression |
| `install_method` | `manual` \| `download_archive` \| `pipx` \| `npm` \| `cargo` \| `brew` \| `apt` \| `dnf` \| `pacman` \| `uv` |
| `supported_platforms` | Non-empty; `linux-x64`, `linux-aarch64`, `macos-x64`, `macos-aarch64`, `windows-x64`, `windows-aarch64` |
| `privilege` | `none` \| `user` \| `elevated` (must match method) |
| `trust_class` | `A` \| `B` \| `C` \| `D` (must match method) |

## Trust classes (do not conflate A and B)

| Class | Meaning | Typical `install_method` |
|-------|---------|---------------------------|
| **A** | Distro / official package manager | `apt`, `dnf`, `pacman`, `brew` |
| **B** | Project official binary (+ signature preferred) | `download_archive` |
| **C** | Language registry — **requires `risk_note`** | `cargo`, `npm`, `pipx`, `uv` |
| **D** | Manual docs only — **requires `install_notes`** | `manual` |

## Privilege

| Value | When |
|-------|------|
| `elevated` | `apt` / `dnf` / `pacman` (or any `sudo …` argv) |
| `user` | User-space install (`cargo`, `npm`, `pipx`, `uv`, `brew`, archives) |
| `none` | Docs-only (`manual`) with no Nova-driven install |

## Install command rules

- Package-manager methods need `install_command` as an argv array (no shell).
- First program must match the method (`pacman`/`sudo`, `pipx`, `cargo`, …).
- Never start with `sh` / `bash` / `curl` / `wget`. Put those under `manual`.

Arch hosts: prefer `pacman` when the package exists in official repos.

## Signed releases

Maintainers publish signed `catalog.json` on tags `catalog-v*`. Contributors do
not need signing keys. See [docs/catalog-signing.md](docs/catalog-signing.md).

## License of contributions

By contributing, you agree your catalog metadata may be redistributed with
Nova-Store under the repository license (MIT).

#!/usr/bin/env python3
"""Migrate Nova assets/store/*.toml into Nova-Store apps/<category>/<id>.toml.

Adds trust_class / privilege / risk_note, normalizes SPDX licenses and
https sources, and remaps Turkish Nova categories to English slugs.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"

# Nova Turkish category label → Nova-Store directory / category slug.
CATEGORY_MAP = {
    "AI": "ai",
    "Git": "git",
    "Dosya ve Arama": "files",
    "Geliştirme": "development",
    "Editörler": "editors",
    "Sistem": "system",
    "Paneller": "panels",
    "Ağ": "networking",
    "Konteyner": "containers",
    "Veritabanı": "database",
    "Güvenlik": "security",
    "Medya": "media",
    "Mesajlaşma": "messaging",
    "Verimlilik": "productivity",
    "Oyunlar": "games",
    "Ekran Koruyucular": "screensavers",
    "Web": "web",
    "Günlük": "daily",
}

CATEGORIES = tuple(dict.fromkeys(CATEGORY_MAP.values()))

LICENSE_MAP = {
    "BSD": "BSD-3-Clause",
    "MIT/Apache-2.0": "MIT OR Apache-2.0",
    "Apache-2.0/MIT": "Apache-2.0 OR MIT",
    "MIT/Unlicense": "MIT OR Unlicense",
    "AGPL-3.0": "AGPL-3.0-or-later",
    "GPL-1.0+": "GPL-1.0-or-later",
    "LGPL-3.0": "LGPL-3.0-or-later",
    "LGPL/GPL": "LGPL-2.1-or-later OR GPL-2.0-or-later",
    "Proprietary": "LicenseRef-Proprietary",
    "Public Domain": "CC0-1.0",
    "CDDL": "CDDL-1.0",
    "Nmap": "LicenseRef-Nmap",
    "NGPL": "LicenseRef-NGPL",
    "w3m": "LicenseRef-w3m",
}

# Prefer https project homes when Nova still listed http://.
SOURCE_HTTPS = {
    "figlet": "https://www.figlet.org/",
    "toilet": "https://github.com/cacalabs/toilet",
    "sox": "https://sourceforge.net/projects/sox/",
    "hexedit": "https://github.com/pixel/hexedit",
    "greed": "https://www.catb.org/~esr/greed/",
    "robotfindskitten": "https://robotfindskitten.org/",
    "socat": "http://www.dest-unreach.org/socat/",  # site is http-only; fixed below
    "links": "http://links.twibright.com/",
    "elinks": "http://elinks.or.cz/",
}

# http-only upstreams: use a stable https documentation / mirror URL.
SOURCE_FALLBACK_HTTPS = {
    "socat": "https://github.com/3ndG4me/socat",
    "links": "https://github.com/twibright-links/links",
    "elinks": "https://github.com/rkd77/elinks",
}

RISK_NOTE = (
    "Registry install (cargo/npm/pypi/uv): package contents are not pinned "
    "by Nova-Store signatures; review upstream before install."
)


def expected_privilege(method: str, install_command: list | None) -> str:
    if method in {"apt", "dnf", "pacman"}:
        return "elevated"
    if install_command and install_command[:1] == ["sudo"]:
        return "elevated"
    if method == "manual":
        return "none"
    return "user"


def expected_trust(method: str) -> str:
    if method in {"apt", "dnf", "pacman", "brew"}:
        return "A"
    if method == "download_archive":
        return "B"
    if method in {"pipx", "npm", "cargo", "uv"}:
        return "C"
    return "D"


def normalize_license(raw: str) -> str:
    return LICENSE_MAP.get(raw, raw)


def normalize_source(app_id: str, source: str) -> str:
    if source.startswith("https://"):
        return source
    if app_id in SOURCE_FALLBACK_HTTPS:
        return SOURCE_FALLBACK_HTTPS[app_id]
    mapped = SOURCE_HTTPS.get(app_id)
    if mapped and mapped.startswith("https://"):
        return mapped
    if source.startswith("http://"):
        https = "https://" + source[len("http://") :]
        return https
    raise ValueError(f"{app_id}: cannot normalize source {source!r}")


def toml_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )


def toml_string(s: str) -> str:
    return f'"{toml_escape(s)}"'


def toml_array_str(items: list[str]) -> str:
    return "[" + ", ".join(toml_string(x) for x in items) + "]"


def write_app_toml(path: Path, app: dict) -> None:
    lines: list[str] = []
    order = [
        "id",
        "name",
        "description",
        "category",
        "source",
        "license",
        "executable",
        "install_method",
        "supported_platforms",
        "privilege",
        "trust_class",
        "risk_note",
        "version",
        "download_url",
        "checksum",
        "checksum_type",
        "install_command",
        "install_notes",
    ]
    for key in order:
        if key not in app:
            continue
        val = app[key]
        if key in {"supported_platforms", "install_command"}:
            lines.append(f"{key} = {toml_array_str(list(val))}")
        elif key in {"install_notes", "risk_note", "description"} and (
            "\n" in str(val) or len(str(val)) > 80
        ):
            # Prefer literal multiline for notes.
            body = str(val)
            if not body.endswith("\n"):
                body += "\n"
            # Escape triple-quote edge cases.
            body = body.replace('"""', '\\"""')
            lines.append(f'{key} = """\n{body}"""')
        elif isinstance(val, str):
            lines.append(f"{key} = {toml_string(val)}")
        else:
            lines.append(f"{key} = {val!r}")

    arts = app.get("artifacts") or []
    for art in arts:
        lines.append("")
        lines.append("[[artifacts]]")
        for k in (
            "arch",
            "download_url",
            "checksum",
            "checksum_type",
            "asset_pattern",
            "checksum_asset_pattern",
        ):
            if k not in art:
                continue
            v = art[k]
            lines.append(f"{k} = {toml_string(v) if isinstance(v, str) else v}")

    release = app.get("release")
    if release:
        lines.append("")
        lines.append("[release]")
        for k in (
            "repo",
            "tag_prefix",
            "asset_pattern",
            "checksum_asset_pattern",
        ):
            if k not in release:
                continue
            lines.append(f"{k} = {toml_string(release[k])}")

    sig = app.get("signature")
    if sig:
        lines.append("")
        lines.append("[signature]")
        for k, v in sig.items():
            lines.append(f"{k} = {toml_string(v) if isinstance(v, str) else v}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def convert_app(raw: dict) -> dict:
    app_id = raw["id"]
    method = raw["install_method"]
    nova_cat = raw["category"]
    if nova_cat not in CATEGORY_MAP:
        raise ValueError(f"{app_id}: unknown Nova category {nova_cat!r}")
    category = CATEGORY_MAP[nova_cat]
    cmd = raw.get("install_command")
    trust = expected_trust(method)
    out: dict = {
        "id": app_id,
        "name": raw["name"],
        "description": raw["description"],
        "category": category,
        "source": normalize_source(app_id, raw["source"]),
        "license": normalize_license(raw["license"]),
        "executable": raw["executable"],
        "install_method": method,
        "supported_platforms": list(raw["supported_platforms"]),
        "privilege": expected_privilege(method, cmd),
        "trust_class": trust,
    }
    if trust == "C":
        out["risk_note"] = RISK_NOTE
    for key in (
        "version",
        "download_url",
        "checksum",
        "checksum_type",
        "install_command",
        "install_notes",
        "artifacts",
        "release",
        "signature",
    ):
        if key in raw:
            out[key] = raw[key]
    if method == "manual" and not out.get("install_notes"):
        raise ValueError(f"{app_id}: manual requires install_notes")
    return out


def load_nova_apps(nova_store: Path) -> list[dict]:
    apps: list[dict] = []
    for path in sorted(nova_store.glob("*.toml")):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        for raw in data.get("apps", []):
            apps.append(raw)
    return apps


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--nova-store",
        type=Path,
        required=True,
        help="Path to Nova assets/store/ directory",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing apps/*/*.toml before writing",
    )
    args = parser.parse_args()

    if not args.nova_store.is_dir():
        print(f"error: {args.nova_store} is not a directory", file=sys.stderr)
        return 1

    raw_apps = load_nova_apps(args.nova_store)
    if not raw_apps:
        print("error: no apps found in Nova store", file=sys.stderr)
        return 1

    if args.clean:
        for cat in CATEGORIES:
            d = APPS_DIR / cat
            if d.is_dir():
                shutil.rmtree(d)

    # Ensure every category directory exists (including empty-capable).
    for cat in CATEGORIES:
        (APPS_DIR / cat).mkdir(parents=True, exist_ok=True)

    # Drop legacy sample-only dirs that are no longer in the map? keep all.
    # Remove leftover files from old 6-category layout when remapping.
    if args.clean:
        for child in APPS_DIR.iterdir():
            if child.is_dir() and child.name not in CATEGORIES:
                shutil.rmtree(child)

    converted: list[dict] = []
    seen: set[str] = set()
    for raw in raw_apps:
        app = convert_app(raw)
        if app["id"] in seen:
            print(f"error: duplicate id {app['id']}", file=sys.stderr)
            return 1
        seen.add(app["id"])
        dest = APPS_DIR / app["category"] / f"{app['id']}.toml"
        write_app_toml(dest, app)
        converted.append(app)

    by_cat: dict[str, int] = {}
    by_trust: dict[str, int] = {}
    for a in converted:
        by_cat[a["category"]] = by_cat.get(a["category"], 0) + 1
        by_trust[a["trust_class"]] = by_trust.get(a["trust_class"], 0) + 1

    print(f"migrated {len(converted)} apps into apps/")
    print("by category:")
    for cat in CATEGORIES:
        print(f"  {cat}: {by_cat.get(cat, 0)}")
    print("by trust:")
    for t in ("A", "B", "C", "D"):
        print(f"  {t}: {by_trust.get(t, 0)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build Nova-consumable aggregated `store-catalog.toml` from `apps/**/*.toml`.

Nova's client (`src/store/remote.rs`) fetches:

  https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml
  https://github.com/Teknoloji-Filozoflari/Nova-Store/releases/latest/download/store-catalog.toml.minisig

The file must parse as Nova `StoreFile` (`[[apps]]` with Turkish `category`
labels from `metadata/categories.toml` `nova_label`). Store-only fields
(`privilege`, `trust_class`, `risk_note`) are omitted — Nova derives trust
class from `install_method` (+ optional `signature`).

This mirrors the conversion in Nova's `tools/sync_store_catalog.sh`, but
emits one aggregate file for the signed Releases channel.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"
CATEGORIES_TOML = ROOT / "metadata" / "categories.toml"
OUT_DEFAULT = ROOT / "dist" / "store-catalog.toml"

KEEP = {
    "id",
    "name",
    "description",
    "source",
    "license",
    "executable",
    "install_method",
    "supported_platforms",
    "checksum",
    "checksum_type",
    "version",
    "download_url",
    "install_command",
    "install_notes",
    "repository_url",
    "artifacts",
    "release",
    "signature",
}

DROP = {"privilege", "trust_class", "risk_note", "category"}

FIELD_ORDER = [
    "id",
    "name",
    "category",
    "description",
    "source",
    "license",
    "executable",
    "install_method",
    "supported_platforms",
    "version",
    "download_url",
    "checksum",
    "checksum_type",
    "install_command",
    "install_notes",
    "repository_url",
]


def git_sha() -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return out.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def load_nova_labels() -> dict[str, str]:
    data = tomllib.loads(CATEGORIES_TOML.read_text(encoding="utf-8"))
    labels: dict[str, str] = {}
    for cat in data.get("categories", []):
        cid = cat["id"]
        labels[cid] = cat["nova_label"]
    if not labels:
        raise SystemExit(f"error: no categories in {CATEGORIES_TOML}")
    return labels


def toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def emit_value(v: object) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return str(v)
    if isinstance(v, str):
        if "\n" in v:
            return '"""\n' + v.replace('"""', '\\"""') + '\n"""'
        return toml_str(v)
    if isinstance(v, list):
        if not v:
            return "[]"
        if all(isinstance(x, str) for x in v):
            inner = ", ".join(toml_str(x) for x in v)
            return f"[{inner}]"
        raise TypeError(f"unsupported list for scalar emit: {v!r}")
    raise TypeError(f"unsupported value type: {type(v)}")


def emit_app(app: dict, nova_label: str) -> str:
    lines = ["[[apps]]"]
    app = dict(app)
    app["category"] = nova_label
    for key in FIELD_ORDER:
        if key not in app or app[key] is None:
            continue
        lines.append(f"{key} = {emit_value(app[key])}")
    for art in app.get("artifacts") or []:
        lines.append("")
        lines.append("[[apps.artifacts]]")
        for k, v in art.items():
            if v is None:
                continue
            lines.append(f"{k} = {emit_value(v)}")
    if app.get("release"):
        lines.append("")
        lines.append("[apps.release]")
        for k, v in app["release"].items():
            if v is None:
                continue
            lines.append(f"{k} = {emit_value(v)}")
    if app.get("signature"):
        lines.append("")
        lines.append("[apps.signature]")
        for k, v in app["signature"].items():
            if v is None:
                continue
            lines.append(f"{k} = {emit_value(v)}")
    return "\n".join(lines) + "\n"


def load_apps(labels: dict[str, str]) -> list[tuple[str, dict]]:
    """Return list of (nova_label, cleaned_app) sorted by id."""
    rows: list[tuple[str, str, dict]] = []
    skipped = 0
    for path in sorted(APPS_DIR.rglob("*.toml")):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        slug = data.get("category") or path.parent.name
        if slug not in labels:
            print(f"skip unknown category {slug}: {path}", file=sys.stderr)
            skipped += 1
            continue
        cleaned = {k: v for k, v in data.items() if k in KEEP and k not in DROP}
        if cleaned.get("repository_url") == "":
            cleaned.pop("repository_url", None)
        rows.append((cleaned["id"], labels[slug], cleaned))
    rows.sort(key=lambda r: r[0])
    if skipped:
        print(f"warning: skipped {skipped} apps", file=sys.stderr)
    return [(label, app) for _, label, app in rows]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=OUT_DEFAULT,
        help="Output store-catalog.toml path (default: dist/store-catalog.toml)",
    )
    args = parser.parse_args()

    labels = load_nova_labels()
    apps = load_apps(labels)
    if not apps:
        print("error: no apps to publish", file=sys.stderr)
        return 1

    sha = git_sha() or "unknown"
    header = (
        "# Nova-Store signed catalog aggregate (store-catalog.toml)\n"
        "# Consumed by Nova via releases/latest/download/store-catalog.toml\n"
        f"# apps={len(apps)} git_sha={sha}\n"
        "# Do not edit by hand — regenerate with scripts/build_store_catalog_toml.py\n"
        "\n"
    )
    body = "\n".join(emit_app(app, label) for label, app in apps)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(header + body, encoding="utf-8")

    # Structural sanity: unique ids + every category is a known nova_label.
    ids = [app["id"] for _, app in apps]
    if len(ids) != len(set(ids)):
        print("error: duplicate ids in aggregate", file=sys.stderr)
        return 1
    known = set(labels.values())
    for label, app in apps:
        if label not in known:
            print(f"error: unknown nova_label {label!r} for {app['id']}", file=sys.stderr)
            return 1

    rel = args.output if not args.output.is_absolute() else args.output
    try:
        rel = args.output.resolve().relative_to(ROOT)
    except ValueError:
        rel = args.output
    print(f"wrote {rel} ({len(apps)} apps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

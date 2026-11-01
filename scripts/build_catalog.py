#!/usr/bin/env python3
"""Aggregate apps/*.toml into metadata/catalog.json for signed publish."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"
OUT_DEFAULT = ROOT / "metadata" / "catalog.json"
CATEGORIES = (
    "ai",
    "git",
    "files",
    "development",
    "editors",
    "system",
    "panels",
    "networking",
    "containers",
    "database",
    "security",
    "media",
    "messaging",
    "productivity",
    "games",
    "screensavers",
    "web",
    "daily",
)


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


def load_apps() -> list[dict]:
    apps: list[dict] = []
    for cat in CATEGORIES:
        for path in sorted((APPS_DIR / cat).glob("*.toml")):
            with path.open("rb") as fh:
                data = tomllib.load(fh)
            apps.append(data)
    apps.sort(key=lambda a: a["id"])
    return apps


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=OUT_DEFAULT,
        help="Output catalog JSON path",
    )
    args = parser.parse_args()

    apps = load_apps()
    if not apps:
        print("error: no apps to publish", file=sys.stderr)
        return 1

    catalog = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "apps": apps,
    }
    sha = git_sha()
    if sha:
        catalog["git_sha"] = sha

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {args.output.relative_to(ROOT)} ({len(apps)} apps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate Nova-Store catalog entries.

Checks (CI gate):
  - JSON Schema conformance (app.schema.json)
  - Unique app ids across apps/
  - SPDX license identifiers / simple expressions
  - HTTPS source URL
  - Known install_method
  - OS/arch (supported_platforms)
  - privilege flag present and consistent with install_method
  - trust_class A/B/C/D rules (incl. risk_note for C, manual→D)
  - category directory matches category field and filename matches id
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"
SCHEMA_PATH = ROOT / "schema" / "app.schema.json"
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

INSTALL_METHODS = {
    "manual",
    "download_archive",
    "pipx",
    "npm",
    "cargo",
    "brew",
    "apt",
    "dnf",
    "pacman",
    "uv",
}
PLATFORMS = {
    "linux-x64",
    "linux-aarch64",
    "macos-x64",
    "macos-aarch64",
    "windows-x64",
    "windows-aarch64",
}
PRIVILEGES = {"none", "user", "elevated"}
TRUST = {"A", "B", "C", "D"}

# Curated SPDX license ids seen in Nova + common FOSS identifiers.
# Expressions like "MIT OR Apache-2.0" are accepted when every atom is known.
# LicenseRef-* covers non-SPDX / proprietary markers used in the catalog.
SPDX_IDS = {
    "0BSD",
    "Apache-2.0",
    "Artistic-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "BSL-1.0",
    "BUSL-1.1",
    "CC0-1.0",
    "CDDL-1.0",
    "curl",
    "EUPL-1.2",
    "GPL-1.0-or-later",
    "GPL-2.0",
    "GPL-2.0-only",
    "GPL-2.0-or-later",
    "GPL-3.0",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
    "ImageMagick",
    "Info-ZIP",
    "ISC",
    "LGPL-2.1",
    "LGPL-2.1-only",
    "LGPL-2.1-or-later",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "LicenseRef-Nmap",
    "LicenseRef-NGPL",
    "LicenseRef-Proprietary",
    "LicenseRef-w3m",
    "MIT",
    "MPL-2.0",
    "NCSA",
    "PostgreSQL",
    "Unlicense",
    "Vim",
    "WTFPL",
    "Zlib",
}

SPDX_TOKEN = re.compile(r"[A-Za-z0-9.+-]+")
HTTPS = re.compile(r"^https://", re.I)
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


class Issue:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path.relative_to(ROOT)}: {self.message}"


def load_toml(path: Path) -> dict:
    with path.open("rb") as fh:
        return tomllib.load(fh)


def validate_spdx(expr: str) -> str | None:
    if not expr or not expr.strip():
        return "license is empty"
    # Allow simple SPDX expressions: ID (AND|OR|WITH ID)* with optional parens.
    cleaned = expr.replace("(", " ").replace(")", " ")
    tokens = cleaned.split()
    if not tokens:
        return "license is empty"
    expect_id = True
    for tok in tokens:
        upper = tok.upper()
        if expect_id:
            if tok in ("AND", "OR", "WITH") or upper in ("AND", "OR", "WITH"):
                return f"unexpected operator {tok!r} in license"
            if tok not in SPDX_IDS:
                return f"unknown SPDX license id {tok!r}"
            expect_id = False
        else:
            if upper not in ("AND", "OR", "WITH"):
                return f"expected AND/OR/WITH in license, got {tok!r}"
            expect_id = True
    if expect_id:
        return "license expression ends with an operator"
    return None


def expected_privilege(method: str, install_command: list | None) -> set[str]:
    if method in {"apt", "dnf", "pacman"}:
        return {"elevated"}
    if install_command and install_command[:1] == ["sudo"]:
        return {"elevated"}
    if method == "manual":
        return {"none", "user"}  # docs-only; usually none
    return {"user"}


def expected_trust(method: str) -> str:
    if method in {"apt", "dnf", "pacman", "brew"}:
        return "A"
    if method == "download_archive":
        return "B"
    if method in {"pipx", "npm", "cargo", "uv"}:
        return "C"
    return "D"


def validate_app(path: Path, data: dict, schema: dict | None) -> list[Issue]:
    issues: list[Issue] = []
    rel = path

    def err(msg: str) -> None:
        issues.append(Issue(rel, msg))

    for key in (
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
    ):
        if key not in data:
            err(f"missing required field {key!r}")

    if issues:
        return issues

    app_id = data["id"]
    if not isinstance(app_id, str) or not ID_RE.match(app_id):
        err(f"invalid id {app_id!r}")
    if path.stem != app_id:
        err(f"filename stem {path.stem!r} must match id {app_id!r}")

    category = data["category"]
    if category not in CATEGORIES:
        err(f"unknown category {category!r}")
    if path.parent.name != category:
        err(
            f"category field {category!r} must match directory "
            f"{path.parent.name!r}"
        )

    source = data["source"]
    if not isinstance(source, str) or not HTTPS.match(source):
        err("source must be an https:// URL")

    lic_err = validate_spdx(str(data["license"]))
    if lic_err:
        err(lic_err)

    method = data["install_method"]
    if method not in INSTALL_METHODS:
        err(f"unknown install_method {method!r}")

    platforms = data["supported_platforms"]
    if not isinstance(platforms, list) or not platforms:
        err("supported_platforms must be a non-empty list")
    else:
        for p in platforms:
            if p not in PLATFORMS:
                err(f"unknown supported_platforms entry {p!r}")

    privilege = data["privilege"]
    if privilege not in PRIVILEGES:
        err(f"unknown privilege {privilege!r}")
    else:
        allowed = expected_privilege(method, data.get("install_command"))
        if privilege not in allowed:
            err(
                f"privilege {privilege!r} inconsistent with install_method "
                f"{method!r} (expected one of {sorted(allowed)})"
            )

    trust = data["trust_class"]
    if trust not in TRUST:
        err(f"unknown trust_class {trust!r}")
    else:
        want = expected_trust(method)
        if trust != want:
            err(
                f"trust_class {trust!r} inconsistent with install_method "
                f"{method!r} (expected {want!r})"
            )
        if trust == "C" and not data.get("risk_note"):
            err("trust_class C requires risk_note")
        if trust == "D" and method != "manual":
            err("trust_class D requires install_method manual")
        if method == "manual" and not data.get("install_notes"):
            err("manual install_method requires install_notes")

    if method in {
        "pipx",
        "npm",
        "cargo",
        "brew",
        "apt",
        "dnf",
        "pacman",
        "uv",
    }:
        cmd = data.get("install_command")
        if not isinstance(cmd, list) or not cmd:
            err("package-manager install_method requires install_command argv")
        elif any(not isinstance(x, str) or not x for x in cmd):
            err("install_command entries must be non-empty strings")
        else:
            prog = cmd[0]
            banned = {"sh", "bash", "zsh", "curl", "wget", "fish"}
            if prog in banned:
                err(f"install_command must not start with {prog!r}")
            if method == "apt" and prog not in {"apt", "sudo"}:
                err("apt install_command must start with apt or sudo")
            if method == "dnf" and prog not in {"dnf", "sudo"}:
                err("dnf install_command must start with dnf or sudo")
            if method == "pacman" and prog not in {"pacman", "sudo"}:
                err("pacman install_command must start with pacman or sudo")
            if method == "pipx" and prog != "pipx":
                err("pipx install_command must start with pipx")
            if method == "npm" and prog != "npm":
                err("npm install_command must start with npm")
            if method == "cargo" and prog != "cargo":
                err("cargo install_command must start with cargo")
            if method == "brew" and prog != "brew":
                err("brew install_command must start with brew")
            if method == "uv" and prog != "uv":
                err("uv install_command must start with uv")

    if method == "download_archive":
        arts = data.get("artifacts") or []
        if arts:
            if not data.get("version"):
                err("download_archive with artifacts requires version")
            for i, art in enumerate(arts):
                if art.get("arch") not in {"x86_64", "aarch64"}:
                    err(f"artifacts[{i}].arch invalid")
                url = art.get("download_url", "")
                if not isinstance(url, str) or not HTTPS.match(url):
                    err(f"artifacts[{i}].download_url must be https://")
                ck = art.get("checksum", "")
                if not isinstance(ck, str) or not re.fullmatch(
                    r"[a-fA-F0-9]{64}", ck
                ):
                    err(f"artifacts[{i}].checksum must be 64 hex chars")
        else:
            for key in ("version", "download_url", "checksum"):
                if key not in data:
                    err(f"download_archive requires {key} (or artifacts)")
            url = data.get("download_url", "")
            if url and (not isinstance(url, str) or not HTTPS.match(url)):
                err("download_url must be https://")
            ck = data.get("checksum", "")
            if ck and (
                not isinstance(ck, str)
                or not re.fullmatch(r"[a-fA-F0-9]{64}", ck)
            ):
                err("checksum must be 64 hex chars")

    if schema is not None:
        try:
            import jsonschema
        except ImportError:
            err("jsonschema package required for schema validation")
        else:
            try:
                jsonschema.validate(instance=data, schema=schema)
            except jsonschema.ValidationError as exc:
                err(f"schema: {exc.message}")

    return issues


def iter_app_files() -> list[Path]:
    files: list[Path] = []
    for cat in CATEGORIES:
        d = APPS_DIR / cat
        if not d.is_dir():
            continue
        files.extend(sorted(d.glob("*.toml")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-schema",
        action="store_true",
        help="Skip JSON Schema validation (structural checks still run)",
    )
    args = parser.parse_args()

    schema = None
    if not args.skip_schema:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    files = iter_app_files()
    if not files:
        print("error: no apps/*.toml found", file=sys.stderr)
        return 1

    issues: list[Issue] = []
    seen: dict[str, Path] = {}

    for path in files:
        try:
            data = load_toml(path)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue(path, f"TOML parse error: {exc}"))
            continue
        issues.extend(validate_app(path, data, schema))
        app_id = data.get("id")
        if isinstance(app_id, str):
            if app_id in seen:
                issues.append(
                    Issue(
                        path,
                        f"duplicate id {app_id!r} "
                        f"(also in {seen[app_id].relative_to(ROOT)})",
                    )
                )
            else:
                seen[app_id] = path

    # Ensure category directories exist
    for cat in CATEGORIES:
        if not (APPS_DIR / cat).is_dir():
            issues.append(
                Issue(APPS_DIR, f"missing category directory apps/{cat}/")
            )

    if issues:
        print(f"FAIL: {len(issues)} issue(s) in {len(files)} app file(s)")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    print(f"OK: {len(files)} apps, {len(seen)} unique ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())

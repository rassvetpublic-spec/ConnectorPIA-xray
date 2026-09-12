#!/usr/bin/env python3
"""Fail-closed lightweight repository governance validator."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "AGENTS.md",
    "QA_INSTRUCTIONS.md",
    ".gitignore",
    ".agent/rules/auto_project_initialize.md",
    ".agent/rules/issue_driven_workflow.md",
    ".agent/rules/safe_sync_gate.md",
    ".agent/rules/security.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/feature.md",
    ".github/ISSUE_TEMPLATE/bug.md",
    ".github/workflows/ci.yml",
)

FORBIDDEN_PREFIXES = (
    "outputs/",
    "artifacts/",
    "auth/",
    "browser-profile/",
    "profiles/",
    "logs/",
    ".agents/",
)

PLACEHOLDERS = (
    "REDACTED",
    "EXAMPLE",
    "DUMMY",
    "CHANGEME",
    "PLACEHOLDER",
)

SECRET_PATTERNS = (
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("api-key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("bearer-token", re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b")),
    (
        "credential-assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|secret)"
            r"\s*[:=]\s*[\"']?([A-Za-z0-9_./+=-]{12,})"
        ),
    ),
    (
        "private-key",
        re.compile("-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
)

TEXT_LIMIT = 2_000_000


def tracked_files() -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [p.decode("utf-8") for p in proc.stdout.split(b"\0") if p]


def looks_placeholder(match_text: str) -> bool:
    upper = match_text.upper()
    return any(token in upper for token in PLACEHOLDERS)


def main() -> int:
    errors: list[str] = []

    for required in REQUIRED:
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")

    files = tracked_files()
    for path in files:
        normalized = path.replace("\\", "/")
        if normalized.startswith(FORBIDDEN_PREFIXES):
            errors.append(f"forbidden tracked local/generated path: {path}")
            continue

        file_path = ROOT / path
        if not file_path.is_file() or file_path.stat().st_size > TEXT_LIMIT:
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for name, pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                candidate = match.group(0)
                if looks_placeholder(candidate):
                    continue
                errors.append(f"possible {name} in {path}")
                break

    if errors:
        print("Repository validation FAILED:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f" - {error}", file=sys.stderr)
        return 1

    print(f"Repository validation OK: {len(files)} tracked files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

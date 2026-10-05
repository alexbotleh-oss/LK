#!/usr/bin/env python3
"""B77 project diagnostic.

Read-only diagnostic pass. Does not modify project files.
Exit code:
  0 = OK
  1 = warnings
  2 = errors
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = ["core", "scripts", "guards", "tests", "reports", "docs", "src", "assets", "data", ".github"]
CRITICAL_FILES = [
    "index.html",
    "stage14.html",
    "docs/DIAGNOSTICS.md",
    "scripts/project_diagnostic.py",
    "src/web/diagnostics.js",
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    warnings: list[str] = []
    errors: list[str] = []
    rows = []

    for d in REQUIRED_DIRS:
        p = ROOT / d
        if not p.is_dir():
            errors.append(f"missing directory: {d}")

    for rel in CRITICAL_FILES:
        p = ROOT / rel
        if not p.is_file():
            errors.append(f"missing critical file: {rel}")
            continue
        rows.append({
            "path": rel,
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
        })

    # Read-only structural sanity checks.
    stage14 = ROOT / "stage14.html"
    if stage14.exists():
        text = stage14.read_text(encoding="utf-8", errors="replace")
        for marker in ("function openScanner", "function scanSubmit", "Core.findQR"):
            if marker not in text:
                warnings.append(f"stage14 marker not found: {marker}")

    report = {
        "schema": "b77-project-diagnostic-1",
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(ROOT),
        "required_dirs": REQUIRED_DIRS,
        "critical_files": rows,
        "warnings": warnings,
        "errors": errors,
        "status": "ERROR" if errors else ("WARN" if warnings else "OK"),
    }

    out = ROOT / "reports" / "project_diagnostic.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if errors else (1 if warnings else 0)

if __name__ == "__main__":
    raise SystemExit(main())

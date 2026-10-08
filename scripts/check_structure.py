#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    SKILL,
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "references" / "sources.md",
]

errors = []
for p in REQUIRED:
    if not p.exists():
        errors.append(f"missing required project file: {p.relative_to(ROOT)}")

if SKILL.exists():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md must begin with YAML frontmatter")
    else:
        front = m.group(1)
        nm = re.search(r"^name:\s*(.+)$", front, re.M)
        desc = re.search(r"^description:\s*(.+)$", front, re.M)
        if not nm:
            errors.append("frontmatter missing name")
        else:
            name = nm.group(1).strip().strip('"\'')
            if name != "liang-qichao-skill":
                errors.append(f"name must be liang-qichao-skill, got {name}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                errors.append("name violates Agent Skills naming rules")
        if not desc or not desc.group(1).strip():
            errors.append("frontmatter missing description")
        elif len(desc.group(1).strip()) > 1024:
            errors.append("description exceeds 1024 characters")

if errors:
    print("FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK: basic liang-qichao-skill structure looks valid")

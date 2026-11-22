#!/usr/bin/env python3
"""Check that every Font Awesome icon used in the built site is in the subset.

Usage:
    python tools/fonts/check-fontawesome.py [site_dir]

Defaults to `_site`. Exits non-zero if an icon class is missing from
`tools/fonts/fontawesome-icons.txt`.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ICONS_FILE = Path(__file__).with_name("fontawesome-icons.txt")
STYLE_ALIASES = {
    "fas": "solid",
    "far": "regular",
    "fab": "brands",
    "fa-solid": "solid",
    "fa-regular": "regular",
    "fa-brands": "brands",
}
IGNORED = {
    "fa-fw",
    "fa-display",
    "fa-solid",
    "fa-regular",
    "fa-brands",
    "fas",
    "far",
    "fab",
}
CLASS_RE = re.compile(r"class\s*=\s*([\"'])(.*?)\1", re.S)


def load_allowed() -> set[tuple[str, str]]:
    allowed = set()
    for line in ICONS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        style, icon = line.split()
        allowed.add((style, icon))
    return allowed


def scan(site_dir: Path) -> Counter[tuple[str, str]]:
    found: Counter[tuple[str, str]] = Counter()

    for path in site_dir.rglob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        for match in CLASS_RE.finditer(html):
            classes = match.group(2).split()
            style = next(
                (STYLE_ALIASES[c] for c in classes if c in STYLE_ALIASES),
                None,
            )
            if style is None:
                continue
            for icon in classes:
                if icon.startswith("fa-") and icon not in IGNORED:
                    found[(style, icon)] += 1

    return found


def main() -> None:
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
    if not site_dir.is_dir():
        raise SystemExit(f"Site directory not found: {site_dir}")

    allowed = load_allowed()
    found = scan(site_dir)
    missing = {pair: count for pair, count in found.items() if pair not in allowed}

    print(
        f"Checked {len(list(site_dir.rglob('*.html')))} HTML files, "
        f"{len(found)} Font Awesome icon pairs."
    )

    if missing:
        print("Missing from tools/fonts/fontawesome-icons.txt:")
        for (style, icon), count in sorted(missing.items()):
            print(f"  {style} {icon} ({count} uses)")
        print(
            "Add the pair to fontawesome-icons.txt and run "
            "tools/fonts/subset-fontawesome.py."
        )
        raise SystemExit(1)

    print("Font Awesome subset covers all icons used in the build.")


if __name__ == "__main__":
    main()
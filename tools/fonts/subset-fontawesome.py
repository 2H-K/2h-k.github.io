#!/usr/bin/env python3
"""Regenerate the self-hosted Font Awesome subset.

The blog only uses a small set of Font Awesome icons. This script downloads
Font Awesome Free 7.3.1, subsets the three woff2 files to the icons listed in
PAIRS, and writes the result to assets/fontawesome.

Requirements:
    python -m pip install "fonttools[woff]" brotli

Run from anywhere:
    python tools/fonts/subset-fontawesome.py

If you add a new `fa-*` class to the site, add the (style, class) pair to
`fontawesome-icons.txt` and run this script again.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "fontawesome"
VERSION = "7.3.1"
BASE = f"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@{VERSION}"
ICONS_FILE = Path(__file__).with_name("fontawesome-icons.txt")
METADATA_URL = (
    f"https://cdn.jsdelivr.net/gh/FortAwesome/Font-Awesome@{VERSION}/"
    "metadata/icons.json"
)
LICENSE_URL = f"{BASE}/LICENSE.txt"

FONT_FILES = {
    "solid": "fa-solid-900.woff2",
    "regular": "fa-regular-400.woff2",
    "brands": "fa-brands-400.woff2",
}


def download(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=180) as response:
        return response.read()


def build_alias_map(metadata: dict) -> dict[str, str]:
    aliases = {}
    for name, info in metadata.items():
        for alias in info.get("aliases", {}).get("names", []):
            aliases[alias] = name
    return aliases


def load_pairs() -> list[tuple[str, str]]:
    pairs = []
    for line in ICONS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        style, icon = line.split()
        pairs.append((style, icon))
    return pairs


def codepoints_by_style(metadata: dict) -> dict[str, list[str]]:
    aliases = build_alias_map(metadata)
    grouped: dict[str, set[str]] = defaultdict(set)

    for style, icon_class in load_pairs():
        name = icon_class.removeprefix("fa-")
        canonical = aliases.get(name, name)
        info = metadata.get(canonical)
        if info is None:
            raise SystemExit(f"Unknown Font Awesome icon: {icon_class}")

        unicode_value = str(info["unicode"]).lower()
        if unicode_value.startswith("0x"):
            unicode_value = unicode_value[2:]
        grouped[style].add(f"0x{int(unicode_value, 16):x}")

    return {style: sorted(values) for style, values in grouped.items()}


def subset(source: Path, target: Path, codepoints: list[str]) -> None:
    unicodes = ",".join(f"U+{value[2:].upper()}" for value in codepoints)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "fontTools.subset",
            str(source),
            f"--output-file={target}",
            "--flavor=woff2",
            f"--unicodes={unicodes}",
        ],
        check=True,
    )


def main() -> None:
    css_dir = OUT / "css"
    font_dir = OUT / "webfonts"
    css_dir.mkdir(parents=True, exist_ok=True)
    font_dir.mkdir(parents=True, exist_ok=True)

    (css_dir / "all.min.css").write_bytes(download(f"{BASE}/css/all.min.css"))

    metadata = json.loads(download(METADATA_URL))
    grouped = codepoints_by_style(metadata)

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        for style, filename in FONT_FILES.items():
            source = tmpdir / filename
            source.write_bytes(download(f"{BASE}/webfonts/{filename}"))
            subset(source, font_dir / filename, grouped[style])

    # The v4 compatibility font is tiny and is referenced by all.min.css.
    # Keep it so old `fa fa-*` classes do not break.
    (font_dir / "fa-v4compatibility.woff2").write_bytes(
        download(f"{BASE}/webfonts/fa-v4compatibility.woff2")
    )

    try:
        (OUT / "LICENSE.txt").write_bytes(download(LICENSE_URL))
    except Exception:
        pass

    for style, filename in FONT_FILES.items():
        path = font_dir / filename
        print(f"{style:8} {path.stat().st_size:7} bytes  {path.name}")
    print(f"css      {(css_dir / 'all.min.css').stat().st_size:7} bytes  all.min.css")


if __name__ == "__main__":
    main()
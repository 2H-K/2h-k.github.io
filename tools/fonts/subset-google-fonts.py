#!/usr/bin/env python3
"""Regenerate the self-hosted Google Fonts subset.

Downloads the `latin` woff2 files for the Lato and Source Sans Pro weights used
by Chirpy and writes them to assets/fonts.

Requirements: Python 3.9+ (standard library only).

Run from anywhere:
    python tools/fonts/subset-google-fonts.py
"""

from __future__ import annotations

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "fonts"
CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Lato:wght@300;400"
    "&family=Source+Sans+Pro:wght@400;600;700;900"
    "&display=swap"
)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
)
BLOCK_RE = re.compile(r"/*\s*([a-z0-9-]+)\s*\*/\s*@font-face\s*\{(.*?)\}", re.S)


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    css = download(CSS_URL).decode("utf-8")

    blocks = []
    for subset, body in BLOCK_RE.findall(css):
        if subset != "latin":
            continue

        family = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        weight = re.search(r"font-weight:\s*(\d+)", body).group(1)
        url = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", body).group(1)
        unicode_range = re.search(r"unicode-range:\s*([^;]+);", body).group(1).strip()

        slug = family.lower().replace(" ", "-")
        filename = f"{slug}-{weight}.woff2"
        data = download(url)
        (OUT / filename).write_bytes(data)
        blocks.append((family, weight, filename, unicode_range))
        print(f"{len(data):7} bytes  {filename}")

    css_blocks = []
    for family, weight, filename, unicode_range in blocks:
        css_blocks.append(
            f"""/* {family} {weight} */
@font-face {{
  font-family: "{family}";
  font-style: normal;
  font-weight: {weight};
  font-display: swap;
  src: url("{filename}") format("woff2");
  unicode-range: {unicode_range};
}}"""
        )

    (OUT / "main.css").write_text("\n\n".join(css_blocks) + "\n", encoding="utf-8")
    print(f"main.css blocks: {len(blocks)}")


if __name__ == "__main__":
    main()
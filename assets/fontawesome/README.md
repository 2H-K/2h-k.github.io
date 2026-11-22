# Self-hosted Font Awesome subset

`css/all.min.css` is the upstream Font Awesome Free 7.3.1 stylesheet.
The three woff2 files in `webfonts/` are subset to the icons actually used by
this site, so they are only a few KB instead of ~250KB.

To regenerate after adding a new icon:

```bash
python -m pip install "fonttools[woff]" brotli
python tools/fonts/subset-fontawesome.py
```

The icon list lives in `tools/fonts/fontawesome-icons.txt`. Add the new
`(style, icon)` pair there before running the script. CI checks that every
Font Awesome class in the built HTML is present in that list.

License: Font Awesome Free (icons CC BY 4.0, fonts SIL OFL 1.1, code MIT).
See `LICENSE.txt`.
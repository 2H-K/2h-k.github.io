# Self-hosted web fonts

These files replace the Google Fonts request in Chirpy's default `cors.yml`.

- `Lato` 300/400
- `Source Sans Pro` 400/600/700/900

Only the Google Fonts `latin` subset is kept. Chinese text continues to use
the system font stack. The `unicode-range` in `main.css` matches the upstream
Google Fonts CSS, so the browser only uses these files for Latin characters.

Sources:

- https://fonts.google.com/specimen/Lato
- https://fonts.google.com/specimen/Source+Sans+Pro
- License: SIL Open Font License 1.1 (`OFL-Lato.txt`, `OFL-SourceSansPro.txt`)

The woff2 files are downloaded from the Google Fonts `latin` subset. To
regenerate them:

```bash
python tools/fonts/subset-google-fonts.py
```

If you change the font families or weights, update `CSS_URL` in the script and
keep the OFL files.
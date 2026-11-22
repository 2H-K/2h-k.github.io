/**
 * Build-time Mermaid renderer.
 *
 * Reads a JSON file produced by `_plugins/mermaid_prerender.rb`, renders every
 * diagram once per theme in a single headless Chromium instance, writes the
 * SVGs to the requested output directory, and writes a manifest describing
 * every generated file.
 *
 * Usage:
 *   node render.mjs --input blocks.json --manifest manifest.json --out ../../assets/img/mermaid
 */

import { access, mkdir, readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import process from 'node:process';
import puppeteer from 'puppeteer';

const HERE = path.dirname(fileURLToPath(import.meta.url));

const DEFAULT_FONT_FAMILY =
  '"Noto Sans CJK SC", "Noto Sans CJK", "Source Sans Pro", "Microsoft YaHei", sans-serif';

function parseArgs(argv) {
  const result = {};

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith('--')) {
      continue;
    }

    const key = arg.slice(2);
    const value = argv[i + 1];

    if (value === undefined || value.startsWith('--')) {
      throw new Error(`Missing value for --${key}`);
    }

    result[key] = value;
    i += 1;
  }

  return result;
}

async function exists(file) {
  try {
    await access(file);
    return true;
  } catch {
    return false;
  }
}

function dimensionFromSvg(svg) {
  const viewBox = svg.match(/\bviewBox="([^"]+)"/i);
  if (viewBox) {
    const values = viewBox[1]
      .trim()
      .split(/[\s,]+/)
      .map(Number);

    if (values.length === 4 && values[2] > 0 && values[3] > 0) {
      return {
        width: Math.ceil(values[2]),
        height: Math.ceil(values[3]),
      };
    }
  }

  const width = svg.match(/\bwidth="([\d.]+)"/i);
  const height = svg.match(/\bheight="([\d.]+)"/i);

  return {
    width: width ? Math.ceil(Number(width[1])) : 800,
    height: height ? Math.ceil(Number(height[1])) : 600,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));

  for (const required of ['input', 'manifest', 'out']) {
    if (!args[required]) {
      throw new Error(`Missing --${required}`);
    }
  }

  const inputPath = path.resolve(args.input);
  const manifestPath = path.resolve(args.manifest);
  const outputDir = path.resolve(args.out);
  const themes = (args.themes || 'default,dark')
    .split(',')
    .map((theme) => theme.trim())
    .filter(Boolean);
  const fontFamily = args.fontFamily || DEFAULT_FONT_FAMILY;

  const input = JSON.parse(await readFile(inputPath, 'utf8'));
  const blocks = Array.isArray(input.blocks) ? input.blocks : [];

  await mkdir(outputDir, { recursive: true });

  const manifest = {};
  let page = null;
  let browser = null;

  const getPage = async () => {
    if (page) {
      return page;
    }

    const mermaidPath = path.join(HERE, 'node_modules/mermaid/dist/mermaid.min.js');
    if (!(await exists(mermaidPath))) {
      throw new Error(
        `Mermaid runtime not found at ${mermaidPath}. Run "npm ci" in tools/mermaid first.`,
      );
    }

    const mermaidSource = await readFile(mermaidPath, 'utf8');
    const executablePath = process.env.PUPPETEER_EXECUTABLE_PATH || undefined;

    browser = await puppeteer.launch({
      headless: true,
      ...(executablePath ? { executablePath } : {}),
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--font-render-hinting=none',
      ],
    });

    page = await browser.newPage();
    await page.setViewport({ width: 1600, height: 1200, deviceScaleFactor: 1 });
    await page.setContent(
      '<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>',
    );
    await page.addScriptTag({ content: mermaidSource });

    return page;
  };

  try {
    for (const block of blocks) {
      if (!block || typeof block.id !== 'string' || typeof block.code !== 'string') {
        throw new Error('Invalid block in input JSON: expected { id, code }');
      }

      const entry = {};

      for (const theme of themes) {
        const themeKey = theme === 'dark' ? 'dark' : 'light';
        const mermaidTheme = theme === 'dark' ? 'dark' : 'default';
        const fileName = `${block.id}-${themeKey}.svg`;
        const filePath = path.join(outputDir, fileName);

        let svg = null;

        if (await exists(filePath)) {
          const cached = await readFile(filePath, 'utf8');
          if (/^\s*<svg\b/i.test(cached)) {
            svg = cached;
          }
        }

        if (!svg) {
          const activePage = await getPage();
          svg = await activePage.evaluate(
            async ({ code, mermaidTheme, id, fontFamily }) => {
              const mermaid = window.mermaid;

              if (!mermaid || typeof mermaid.render !== 'function') {
                throw new Error('Mermaid runtime did not expose the render() API');
              }

              mermaid.initialize({
                startOnLoad: false,
                theme: mermaidTheme,
                securityLevel: 'loose',
                fontFamily,
                flowchart: { htmlLabels: true, useMaxWidth: false },
                sequence: { useMaxWidth: false },
                gantt: { useMaxWidth: false },
                class: { useMaxWidth: false },
                state: { useMaxWidth: false },
                er: { useMaxWidth: false },
                journey: { useMaxWidth: false },
                timeline: { useMaxWidth: false },
                mindmap: { useMaxWidth: false },
              });

              const rendered = await mermaid.render(
                `mermaid-${id}-${mermaidTheme}`,
                code,
              );

              return rendered.svg;
            },
            {
              code: block.code,
              mermaidTheme,
              id: block.id,
              fontFamily,
            },
          );

          if (!/^\s*<svg\b/i.test(svg)) {
            throw new Error(`Mermaid returned a non-SVG result for ${block.id}`);
          }

          await writeFile(filePath, svg, 'utf8');
          console.log(`Rendered ${fileName}`);
        }

        entry[themeKey] = {
          file: fileName,
          ...dimensionFromSvg(svg),
        };
      }

      manifest[block.id] = entry;
    }
  } finally {
    if (browser) {
      await browser.close();
    }
  }

  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
  console.log(
    `Rendered ${Object.keys(manifest).length} diagram(s) x ${themes.length} theme(s) into ${outputDir}`,
  );
}

main().catch((error) => {
  console.error(error instanceof Error ? error.stack : error);
  process.exitCode = 1;
});

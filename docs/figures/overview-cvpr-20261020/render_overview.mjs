// Render the SVG with the locally available Chromium renderer and record text QA.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const modulePath = process.env.OVERVIEW_PUPPETEER_PATH ||
  'C:/Users/changan/AppData/Local/npm-cache/_npx/668c188756b835f3/node_modules/puppeteer/lib/puppeteer/puppeteer.js';
const { default: puppeteer } = await import(pathToFileURL(modulePath).href);
const browser = await puppeteer.launch({
  executablePath: process.env.OVERVIEW_BROWSER_PATH || 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  headless: true,
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 2400, height: 1120, deviceScaleFactor: 1.5 });
  await page.goto(pathToFileURL(path.join(root, 'drivecompose-overview-native.svg')).href);
  await page.screenshot({ path: path.join(root, 'drivecompose-overview-native.png') });
  const qa = await page.evaluate(() => {
    const text = Array.from(document.querySelectorAll('text')).map(e => {
      const r = e.getBoundingClientRect();
      return { text: e.textContent, x: r.x, y: r.y, w: r.width, h: r.height,
        fontSize: Number.parseFloat(getComputedStyle(e).fontSize) };
    });
    const overlaps = [];
    for (let i = 0; i < text.length; ++i) {
      for (let j = i + 1; j < text.length; ++j) {
        const a = text[i], b = text[j];
        const w = Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x);
        const h = Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
        if (w > 2 && h > 2) overlaps.push({ a: a.text, b: b.text, w, h });
      }
    }
    return {
      svgCanvas: [2400,1120], pngPixels: [3600,1680],
      textCount: text.length,
      minFontPx: Math.min(...text.map(t => t.fontSize)),
      minFontPtAt178mm: Math.min(...text.map(t => t.fontSize))*178/25.4*72/2400,
      outOfBoundsText: text.filter(t => t.x<0 || t.y<0 || t.x+t.w>2400 || t.y+t.h>1120),
      overlappingTextBoxes: overlaps,
      rasterImageElements: document.querySelectorAll('image').length,
      vectorElements: document.querySelectorAll('path,rect,ellipse,text').length,
    };
  });
  await fs.writeFile(path.join(root,'render-qa.json'),JSON.stringify(qa,null,2)+'\n');
  process.stdout.write(JSON.stringify(qa));
} finally {
  await browser.close();
}

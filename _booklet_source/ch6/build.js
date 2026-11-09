// Build: concatenate parts -> render TeX with KaTeX -> print A4 PDF with Chromium -> report overflow per page.
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright');

const dir = __dirname;
const parts = ['a_head.html', 'b_u1u2.html', 'c_u3.html', 'd_u4u5.html', 'e_u6.html', 'f_u7.html'];
let src = parts.map(p => fs.readFileSync(path.join(dir, p), 'utf8')).join('\n');
src = src.replace('KATEX_CSS', 'file://' + path.join(dir, 'node_modules/katex/dist/katex.min.css'));

let errors = 0;
function render(tex, display) {
  try {
    return katex.renderToString(tex, { displayMode: display, throwOnError: true, strict: 'ignore', output: 'html' });
  } catch (e) {
    errors++;
    console.error('KaTeX error:', e.message, '\n  in:', tex.slice(0, 120));
    return '<span style="color:red">[TeX error]</span>';
  }
}
// display first, then inline
src = src.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => render(t.trim(), true));
src = src.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => '<span class="mx">' + render(t.trim(), false) + '</span>');
const out = path.join(dir, 'out.html');
fs.writeFileSync(out, src);
console.log('KaTeX errors:', errors);

(async () => {
  const pdfPath = process.argv[2] || path.join(dir, 'booklet.pdf');
  const browser = await chromium.launch({ proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const page = await browser.newPage();
  const bad = [];
  page.on('requestfailed', r => bad.push('reqfail ' + r.url() + ' ' + (r.failure() && r.failure().errorText)));
  page.on('pageerror', e => bad.push('pageerror ' + e.message));
  await page.goto('file://' + out, { waitUntil: 'networkidle', timeout: 90000 });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const report = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page').forEach((p, i) => {
      const over = p.scrollHeight - p.clientHeight;
      // also detect children overflowing horizontally
      let wide = 0;
      p.querySelectorAll('.tpl .v, .stmt, .t, .paper').forEach(el => { if (el.scrollWidth > el.clientWidth + 2) wide++; });
      const spaces = Array.from(p.querySelectorAll('.space')).map(s => Math.round(s.getBoundingClientRect().height));
      res.push({ n: i + 1, id: p.id, over, wide, spaces });
    });
    const fonts = Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family);
    return { res, fonts: Array.from(new Set(fonts)) };
  });
  console.log('fonts:', report.fonts.join(', '));
  report.res.forEach(r => {
    const flag = (r.over > 1 ? ' OVERFLOW ' + r.over + 'px' : '') + (r.wide ? ' WIDE x' + r.wide : '');
    console.log(String(r.n).padStart(2), r.id.padEnd(10), flag || 'ok', r.spaces.length ? 'spaces(px): ' + r.spaces.join(',') : '');
  });
  await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  console.log('PDF:', pdfPath);
  console.log('problems:', bad.length ? bad.join('\n') : 'none');
  await browser.close();
})();

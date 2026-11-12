// Build: concatenate parts -> render TeX with KaTeX -> print A4 PDF with Chromium -> report overflow per page.
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright');

const dir = __dirname;
const TOTAL_UNITS = 6;
const parts = ['a_head.html'].concat(fs.readdirSync(dir).filter(f => /^[b-z]_.*\.html$/.test(f)).sort());
let src = parts.map(p => fs.readFileSync(path.join(dir, p), 'utf8')).join('\n');
src = src.replace('KATEX_CSS', 'file://' + path.join(dir, 'node_modules/katex/dist/katex.min.css'));

// v2: page kinds + footer progress
src = src.replace(/<section class="page([^"]*)" id="([^"]+)"([^>]*)>([\s\S]*?)<\/section>/g, (m, cls, id, attrs, body) => {
  let kind = '';
  if (cls.includes('sol')) kind = ' k-sol';
  else if (body.includes('tag past')) kind = ' k-past';
  else if (body.includes('tag ex')) kind = ' k-ex';
  const hm = body.match(/<span class="u">([^<]*)<\/span>/);
  const um = hm && hm[1].match(/(?:الوحدة|الوحدتين)\s*(\d)(?:\s*و(\d))?/);
  let foot = '';
  if (um) {
    const u = +(um[2] || um[1]);
    let bar = '';
    for (let i = 1; i <= TOTAL_UNITS; i++) bar += '<i class="' + (i < u ? 'd' : i === u ? 'c' : '') + '"></i>';
    foot = '<div class="foot"><span>الوحدة ' + u + ' من ' + TOTAL_UNITS + '</span><div class="bar">' + bar + '</div></div>';
  }
  return '<section class="page' + cls + kind + '" id="' + id + '"' + attrs + '>' + body + foot + '</section>';
});

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
src = src.replace(/<span class="mx">(\\\([^<]+?\\\))<\/span>/g, '$1');
src = src.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => render(t.trim(), true));
src = src.replace(/\\\(([\s\S]+?)\\\)([,.;:،؛])?/g, (_, t, p) => {
  const tex = t.trim();
  const m = '<span class="mx" data-tex="' + tex.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;') + '">' + render(tex, false) + '</span>';
  return p ? '<span style="white-space:nowrap">' + m + p + '</span>' : m;
});
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
  // keep short inline formulas on one line; long ones may wrap (only at the breaks KaTeX allows)
  await page.evaluate(() => {
    document.querySelectorAll('.mx').forEach(el => {
      el.style.whiteSpace = 'nowrap';
      const w = el.getBoundingClientRect().width;
      const box = el.closest('p, li, td, th, .v, .idea, .note, .aa, .qq, .f, .stmt, .q, .tf, .cap, h2, h3, .err') || el.parentElement;
      if (w > 0.6 * box.clientWidth) el.style.whiteSpace = 'normal';
    });
  });
  const report = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page').forEach((p, i) => {
      const over = p.scrollHeight - p.clientHeight;
      // also detect children overflowing horizontally
      let wide = 0;
      p.querySelectorAll('.tpl .v, .stmt, .t, .paper').forEach(el => { if (el.scrollWidth > el.clientWidth + 2) wide++; });
      const spaces = Array.from(p.querySelectorAll('.space')).map(s => Math.round(s.getBoundingClientRect().height));
      let bot = 0; const pr = p.getBoundingClientRect();
      Array.from(p.children).forEach(c => { if (!c.classList.contains('foot')) bot = Math.max(bot, c.getBoundingClientRect().bottom - pr.top); });
      const free = Math.round((pr.height - bot) / pr.height * 297 - 13);
      const wraps = [];
      p.querySelectorAll('.mx[data-tex]').forEach(el => {
        const tops = new Set(Array.from(el.getClientRects()).map(r => Math.round(r.top)));
        if (tops.size > 1) wraps.push(el.dataset.tex);
      });
      res.push({ n: i + 1, id: p.id, over, wide, spaces, free, wraps });
    });
    const fonts = Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family);
    return { res, fonts: Array.from(new Set(fonts)) };
  });
  console.log('fonts:', report.fonts.join(', '));
  report.res.forEach(r => {
    const flag = (r.over > 1 ? ' OVERFLOW ' + r.over + 'px' : '') + (r.wide ? ' WIDE x' + r.wide : '');
    console.log(String(r.n).padStart(2), r.id.padEnd(10), 'free', String(r.free).padStart(3)+'mm', flag || 'ok', r.spaces.length ? 'spaces(px): ' + r.spaces.join(',') : '');
    if (process.env.WRAPS) r.wraps.forEach(w => console.log('      wrap:', w));
  });
  await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  console.log('PDF:', pdfPath);
  console.log('problems:', bad.length ? bad.join('\n') : 'none');
  await browser.close();
})();

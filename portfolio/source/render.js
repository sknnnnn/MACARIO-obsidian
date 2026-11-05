// Exporta los PDF con Chromium (Playwright) y, opcionalmente, PNG por página para revisión.
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const langs = process.argv.slice(2).length ? process.argv.slice(2) : ['es','en'];
  const b = await chromium.launch();
  for (const lang of langs) {
    const p = await b.newPage();
    await p.goto('file://' + path.resolve(__dirname, `portfolio_${lang}.html`), {waitUntil: 'networkidle'});
    await p.evaluate(() => document.fonts.ready);
    const out = path.resolve(__dirname, '..', `Portfolio_Ignacio_Sconza_${lang.toUpperCase()}.pdf`);
    await p.pdf({path: out, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true, tagged: true, outline: true});
    console.log('pdf', out);
    await p.close();
  }
  await b.close();
})();

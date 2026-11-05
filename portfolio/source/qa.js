// Control de calidad: detecta elementos que se salen de su página o del área útil,
// imágenes rotas y enlaces. Uso: node qa.js es|en
const {chromium}=require('playwright');const path=require('path');
(async()=>{const lang=process.argv[2]||'es';const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(__dirname,`portfolio_${lang}.html`),{waitUntil:'networkidle'});
await p.emulateMedia({media:'print'});await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>{const out=[];const pages=[...document.querySelectorAll('.page')];
pages.forEach((pg,i)=>{const pr=pg.getBoundingClientRect();
 pg.querySelectorAll('*').forEach(el=>{if(el.closest('svg')&&el.tagName!=='svg')return; if(el.classList.contains('abs')&&el.tagName==='svg')return;
  const r=el.getBoundingClientRect(); if(r.width===0&&r.height===0)return;
  const tol=1; if(r.right>pr.right+tol||r.bottom>pr.bottom+tol||r.left<pr.left-tol||r.top<pr.top-tol){
   if(el.tagName==='IMG'&&el.classList.contains('abs'))return;
   out.push({page:i+1,tag:el.tagName,cls:el.className&&el.className.baseVal===undefined?el.className:'',txt:(el.textContent||'').trim().slice(0,50),over:[Math.round(r.right-pr.right),Math.round(r.bottom-pr.bottom)]});}
  // texto recortado por overflow interno
  if(el.scrollHeight>el.clientHeight+2 && getComputedStyle(el).overflow==='hidden' && !el.classList.contains('page')) out.push({page:i+1,clipped:el.className});
 });
 // área útil: contenido de .body no debe pasar el margen inferior
 const bd=pg.querySelector('.body'); if(bd){const br=bd.getBoundingClientRect(); bd.querySelectorAll('*').forEach(el=>{const r=el.getBoundingClientRect(); if(r.height>0 && r.bottom>br.bottom+2) out.push({page:i+1,belowBody:Math.round(r.bottom-br.bottom),tag:el.tagName,txt:(el.textContent||'').trim().slice(0,40)});});}
});
const imgs=[...document.images].filter(im=>!im.complete||im.naturalWidth===0).map(im=>im.src);
const links=[...document.querySelectorAll('a[href]')].map(a=>a.href);
return {issues:out,broken:imgs,links:[...new Set(links)],pages:pages.length};});
console.log(JSON.stringify(r,null,1));await b.close();})();

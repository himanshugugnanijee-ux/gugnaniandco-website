// Usage: node post_image.js spec.json out.png
// spec.json: {"tag":"GST UPDATE","title":"Scrap & E-Waste: *New GST Rules*","points":["...","...","..."],"note":"Effective 1 November 2026"}
// title: wrap the highlighted words in *asterisks*. Use 2-4 points, each under ~60 characters. Always carries the CA India logo.
const { chromium } = require('playwright');
const fs=require('fs'), path=require('path');
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8')); const out=process.argv[3]||'post.png';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const logo='data:image/png;base64,'+fs.readFileSync(path.join(__dirname,'ca-logo.png')).toString('base64');
const title=esc(spec.title).replace(/\*(.+?)\*/g,'<em>$1</em>');
const n=(spec.points||[]).length, fs1=title.length>48?56:66, fsp=n>3?30:34;
const html=`<style>*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1080px;font-family:'Segoe UI',Arial,sans-serif;background:linear-gradient(150deg,#0a2540 0%,#0b3d6e 60%,#11528f 100%);color:#fff;position:relative;overflow:hidden}
.top{display:flex;align-items:center;gap:22px;padding:56px 64px 0}.top img{height:96px;background:#fff;border-radius:16px;padding:8px}
.firm b{font-size:44px;display:block;font-family:Georgia,serif}.firm span{font-size:20px;letter-spacing:5px;color:#f2a900;font-weight:700}
.main{position:absolute;top:190px;bottom:96px;left:64px;right:64px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;background:#f2a900;color:#0a2540;font-weight:800;font-size:26px;padding:8px 22px;border-radius:30px;margin-bottom:20px;letter-spacing:2px}
h1{font-size:${fs1}px;line-height:1.12;margin-bottom:28px}h1 em{color:#f2a900;font-style:normal}
.step{display:flex;gap:22px;align-items:center;background:rgba(255,255,255,.1);border-radius:14px;padding:18px 22px;margin-bottom:16px}
.n{background:#f2a900;color:#0a2540;font-weight:800;font-size:32px;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.step p{font-size:${fsp}px;font-weight:600;line-height:1.25}.note{font-size:27px;margin-top:12px;opacity:.92}
.foot{position:absolute;left:0;right:0;bottom:0;background:#f2a900;color:#0a2540;padding:26px 64px;display:flex;justify-content:space-between;font-size:30px;font-weight:800}
.circle{position:absolute;right:-160px;top:-160px;width:460px;height:460px;border-radius:50%;background:rgba(242,169,0,.12)}</style>
<div class="circle"></div><div class="top"><img src="${logo}"><div class="firm"><b>Gugnani &amp; Co</b><span>CHARTERED ACCOUNTANTS</span></div></div>
<div class="main">${spec.tag?`<div class="tag">${esc(spec.tag)}</div>`:''}<h1>${title}</h1>${(spec.points||[]).map((p,i)=>`<div class="step"><div class="n">${i+1}</div><p>${esc(p)}</p></div>`).join('')}${spec.note?`<p class="note">${esc(spec.note)}</p>`:''}</div>
<div class="foot"><span>Call +91-9953788989</span><span>gugnaniandco.com</span></div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});await p.setContent(html);await p.screenshot({path:out});await b.close();console.log('saved',out)})();

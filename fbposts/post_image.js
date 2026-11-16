// Usage: node post_image.js spec.json out.png
// spec.json: {"tag":"GST UPDATE","title":"Scrap & E-Waste: *New GST Rules*","points":["...","...","..."],"note":"Effective 1 November 2026","design":3}
// title: wrap the highlighted words in *asterisks*. Use 2-4 points, each under ~60 characters. Always carries the CA India logo.
// design: 1-6 picks the layout (1 navy cards, 2 cream checklist, 3 teal header, 4 indigo grid, 5 maroon timeline, 6 white & blue).
//   Leave it out and the design is chosen from the date in the output file name (fb-post-YYYY-MM-DD.png), so it changes every day.
//   Use a design different from the one used on the previous day's post.
const { chromium } = require('playwright');
const fs=require('fs'), path=require('path');
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8')); const out=process.argv[3]||'post.png';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const logo='data:image/png;base64,'+fs.readFileSync(path.join(__dirname,'ca-logo.png')).toString('base64');
const title=esc(spec.title).replace(/\*(.+?)\*/g,'<em>$1</em>');
const pts=(spec.points||[]).map(esc), n=pts.length, long=title.length>48;
const tag=spec.tag?esc(spec.tag):'', note=spec.note?esc(spec.note):'';
const DESIGNS=6;
const m=/(\d{4})-(\d{2})-(\d{2})/.exec(path.basename(out));
const day=Math.floor((m?Date.UTC(+m[1],+m[2]-1,+m[3]):Date.now())/864e5);
const design=spec.design?((+spec.design-1)%DESIGNS+DESIGNS)%DESIGNS+1:day%DESIGNS+1;
const PHONE='Call +91-9953788989', SITE='gugnaniandco.com';
const base=`*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1080px;font-family:'Segoe UI',Arial,sans-serif;position:relative;overflow:hidden}h1 em{font-style:normal}
.firm b{font-size:44px;display:block;font-family:Georgia,serif}.firm span{font-size:20px;letter-spacing:5px;font-weight:700}
.top{display:flex;align-items:center;gap:22px}.top img{height:96px;background:#fff;border-radius:16px;padding:8px}
.foot{position:absolute;left:0;right:0;bottom:0;padding:26px 64px;display:flex;justify-content:space-between;font-size:30px;font-weight:800}`;
const top=`<div class="top"><img src="${logo}"><div class="firm"><b>Gugnani &amp; Co</b><span>CHARTERED ACCOUNTANTS</span></div></div>`;
const foot=`<div class="foot"><span>${PHONE}</span><span>${SITE}</span></div>`;
const fsp=n>3?30:34;
const D={
// 1: navy gradient, numbered glass cards
1:()=>`<style>${base}body{background:linear-gradient(150deg,#0a2540 0%,#0b3d6e 60%,#11528f 100%);color:#fff}
.top{padding:56px 64px 0}.firm span{color:#f2a900}
.main{position:absolute;top:190px;bottom:96px;left:64px;right:64px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;background:#f2a900;color:#0a2540;font-weight:800;font-size:26px;padding:8px 22px;border-radius:30px;margin-bottom:20px;letter-spacing:2px}
h1{font-size:${long?56:66}px;line-height:1.12;margin-bottom:28px}h1 em{color:#f2a900}
.step{display:flex;gap:22px;align-items:center;background:rgba(255,255,255,.1);border-radius:14px;padding:18px 22px;margin-bottom:16px}
.n{background:#f2a900;color:#0a2540;font-weight:800;font-size:32px;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.step p{font-size:${fsp}px;font-weight:600;line-height:1.25}.note{font-size:27px;margin-top:12px;opacity:.92}
.foot{background:#f2a900;color:#0a2540}
.circle{position:absolute;right:-160px;top:-160px;width:460px;height:460px;border-radius:50%;background:rgba(242,169,0,.12)}</style>
<div class="circle"></div>${top}
<div class="main">${tag?`<div class="tag">${tag}</div>`:''}<h1>${title}</h1>${pts.map((p,i)=>`<div class="step"><div class="n">${i+1}</div><p>${p}</p></div>`).join('')}${note?`<p class="note">${note}</p>`:''}</div>${foot}`,
// 2: cream paper, tick checklist
2:()=>`<style>${base}body{background:#fbf5e6;color:#12263f}
.bar{position:absolute;left:0;top:0;bottom:0;width:22px;background:#c8102e}
.top{padding:56px 64px 0 86px}.top img{border:2px solid #e6dcc3}.firm span{color:#c8102e}
.main{position:absolute;top:190px;bottom:96px;left:86px;right:64px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;background:#12263f;color:#fff;font-weight:800;font-size:26px;padding:8px 22px;border-radius:6px;margin-bottom:22px;letter-spacing:2px}
h1{font-size:${long?58:68}px;line-height:1.1;margin-bottom:26px;font-family:Georgia,serif}h1 em{color:#c8102e}
.step{display:flex;gap:24px;align-items:center;padding:20px 0;border-top:2px solid #e2d6b8}.step:last-of-type{border-bottom:2px solid #e2d6b8}
.n{background:#1f7a4d;color:#fff;font-weight:800;font-size:34px;width:56px;height:56px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.step p{font-size:${fsp+1}px;font-weight:600;line-height:1.25}.note{font-size:27px;margin-top:22px;color:#5b4a2a;font-style:italic}
.foot{background:#12263f;color:#fff;padding-left:86px}</style>
<div class="bar"></div>${top}
<div class="main">${tag?`<div class="tag">${tag}</div>`:''}<h1>${title}</h1>${pts.map(p=>`<div class="step"><div class="n">&#10003;</div><p>${p}</p></div>`).join('')}${note?`<p class="note">${note}</p>`:''}</div>${foot}`,
// 3: teal header block over white, big outline numerals
3:()=>`<style>${base}body{background:#fff;color:#0f2b2a;display:flex;flex-direction:column}
.head{background:linear-gradient(135deg,#0b5d57,#0f8a7e);color:#fff;padding:52px 64px 44px;border-radius:0 0 60px 60px}
.firm span{color:#ffd166}
.tag{display:inline-block;border:3px solid #ffd166;color:#ffd166;font-weight:800;font-size:24px;padding:6px 20px;border-radius:30px;margin:34px 0 16px;letter-spacing:2px}
h1{font-size:${long?54:64}px;line-height:1.12}h1 em{color:#ffd166}
.body{flex:1;padding:10px 64px 110px;display:flex;flex-direction:column;justify-content:center}
.step{display:flex;gap:26px;align-items:center;padding:${n>3?12:18}px 0}
.n{font-size:${n>3?58:68}px;font-weight:800;color:#0f8a7e;width:92px;flex-shrink:0;line-height:1;font-family:Georgia,serif}
.step p{font-size:${fsp}px;font-weight:600;line-height:1.25;border-left:4px solid #ffd166;padding-left:24px}
.note{font-size:26px;margin-top:10px;color:#3f5f5c}
.foot{background:#0b3b38;color:#fff}</style>
<div class="head">${top}${tag?`<div class="tag">${tag}</div>`:'<div style="height:34px"></div>'}<h1>${title}</h1></div>
<div class="body">${pts.map((p,i)=>`<div class="step"><div class="n">0${i+1}</div><p>${p}</p></div>`).join('')}${note?`<p class="note">${note}</p>`:''}</div>${foot}`,
// 4: indigo, centered title, white cards in a grid
4:()=>`<style>${base}body{background:linear-gradient(160deg,#1e1b4b 0%,#3730a3 70%,#4f46e5 100%);color:#fff}
.top{padding:52px 64px 0;justify-content:center}.firm span{color:#a5f3fc}
.main{position:absolute;top:180px;bottom:96px;left:56px;right:56px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.tag{background:#a5f3fc;color:#1e1b4b;font-weight:800;font-size:24px;padding:8px 24px;border-radius:8px;margin-bottom:18px;letter-spacing:3px}
h1{font-size:${long?52:62}px;line-height:1.12;margin-bottom:30px}h1 em{color:#a5f3fc}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;width:100%}
.card{background:#fff;color:#1e1b4b;border-radius:22px;padding:${n>2?22:30}px 24px;text-align:left;display:flex;flex-direction:column;gap:10px}
.card.wide{grid-column:1/3}
.n{background:#4f46e5;color:#fff;font-weight:800;font-size:26px;width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center}
.card p{font-size:${n>2?29:33}px;font-weight:700;line-height:1.25}
.note{font-size:26px;margin-top:22px;opacity:.95}
.foot{background:#a5f3fc;color:#1e1b4b}
.dots{position:absolute;left:-90px;bottom:40px;width:300px;height:300px;border-radius:50%;border:40px solid rgba(165,243,252,.10)}</style>
<div class="dots"></div>${top}
<div class="main">${tag?`<div class="tag">${tag}</div>`:''}<h1>${title}</h1><div class="grid">${pts.map((p,i)=>`<div class="card${n%2&&i==n-1?' wide':''}"><div class="n">${i+1}</div><p>${p}</p></div>`).join('')}</div>${note?`<p class="note">${note}</p>`:''}</div>${foot}`,
// 5: maroon, vertical timeline
5:()=>`<style>${base}body{background:linear-gradient(170deg,#3b0a16 0%,#7a1325 100%);color:#fff7e6}
.top{padding:56px 64px 0}.firm span{color:#fbbf24}
.main{position:absolute;top:190px;bottom:96px;left:64px;right:64px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;color:#fbbf24;font-weight:800;font-size:27px;letter-spacing:6px;margin-bottom:14px;border-bottom:4px solid #fbbf24;padding-bottom:8px}
h1{font-size:${long?56:66}px;line-height:1.12;margin-bottom:34px;font-family:Georgia,serif}h1 em{color:#fbbf24}
.line{border-left:5px solid rgba(251,191,36,.55);margin-left:22px;padding-left:44px}
.step{position:relative;padding:${n>3?14:20}px 0}
.step:before{content:'';position:absolute;left:-63px;top:50%;margin-top:-16px;width:32px;height:32px;border-radius:50%;background:#fbbf24;border:5px solid #5a0f1d}
.step p{font-size:${fsp+1}px;font-weight:600;line-height:1.25}
.note{font-size:27px;margin-top:26px;color:#fde9b8}
.foot{background:#fff7e6;color:#5a0f1d}
.ring{position:absolute;right:-120px;top:-120px;width:380px;height:380px;border-radius:50%;border:46px solid rgba(251,191,36,.12)}</style>
<div class="ring"></div>${top}
<div class="main">${tag?`<div class="tag">${tag}</div>`:''}<h1>${title}</h1><div class="line">${pts.map(p=>`<div class="step"><p>${p}</p></div>`).join('')}</div>${note?`<p class="note">${note}</p>`:''}</div>${foot}`,
// 6: white & royal blue, pill rows
6:()=>`<style>${base}body{background:#f4f7fc;color:#0f172a}
.q{position:absolute;right:-140px;top:-140px;width:440px;height:440px;border-radius:50%;background:#1d4ed8}
.q2{position:absolute;left:-110px;bottom:20px;width:260px;height:260px;border-radius:50%;background:#dbe7ff}
.top{padding:56px 64px 0;position:relative}.top img{box-shadow:0 4px 16px rgba(15,23,42,.15)}.firm span{color:#1d4ed8}
.main{position:absolute;top:190px;bottom:96px;left:64px;right:64px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;background:#ff7a1a;color:#fff;font-weight:800;font-size:25px;padding:8px 22px;border-radius:30px;margin-bottom:20px;letter-spacing:2px}
h1{font-size:${long?58:68}px;line-height:1.1;margin-bottom:28px;font-weight:800}h1 em{color:#1d4ed8}
.step{display:flex;gap:20px;align-items:center;background:#fff;border-radius:60px;padding:14px 30px 14px 14px;margin-bottom:16px;box-shadow:0 6px 18px rgba(29,78,216,.12)}
.n{background:#1d4ed8;color:#fff;font-weight:800;font-size:30px;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.step p{font-size:${fsp-1}px;font-weight:600;line-height:1.22}.note{font-size:27px;margin-top:12px;color:#334155}
.foot{background:#1d4ed8;color:#fff}</style>
<div class="q"></div><div class="q2"></div>${top}
<div class="main">${tag?`<div class="tag">${tag}</div>`:''}<h1>${title}</h1>${pts.map((p,i)=>`<div class="step"><div class="n">${i+1}</div><p>${p}</p></div>`).join('')}${note?`<p class="note">${note}</p>`:''}</div>${foot}`
};
const html=D[design]();
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});await p.setContent(html);await p.screenshot({path:out});await b.close();console.log('saved',out,'design',design)})();

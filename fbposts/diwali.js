const { chromium } = require('playwright');const fs=require('fs');
const logo='data:image/png;base64,'+fs.readFileSync('ca-logo.png').toString('base64');
function diya(x,y,s){return `<g transform="translate(${x} ${y}) scale(${s})">
<ellipse cx="0" cy="-58" rx="70" ry="90" fill="url(#glow)"/>
<path d="M0 -70 C14 -48 16 -30 0 -18 C-16 -30 -14 -48 0 -70Z" fill="url(#flame)"/>
<path d="M0 -56 C7 -44 8 -34 0 -26 C-8 -34 -7 -44 0 -56Z" fill="#fff6c8"/>
<path d="M-62 -14 Q0 -26 62 -14 Q52 30 0 34 Q-52 30 -62 -14Z" fill="url(#clay)"/>
<path d="M-62 -14 Q0 -2 62 -14" fill="none" stroke="#ffcf6a" stroke-width="4"/>
<path d="M-40 6 Q0 16 40 6" fill="none" stroke="#ffd98a" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/></g>`}
const lights=Array.from({length:23},(_,i)=>{const x=20+i*46,y=40+Math.sin(i/22*Math.PI)*70;const c=['#ffd54a','#ff8a3d','#ff5c8a','#7ee0ff','#a6ff8a'][i%5];return `<circle cx="${x}" cy="${y}" r="9" fill="${c}"/><circle cx="${x}" cy="${y}" r="22" fill="${c}" opacity=".25"/>`}).join('');
const wire=`<path d="M0 30 Q540 ${40+140} 1080 30" fill="none" stroke="#3a2a10" stroke-width="2" opacity=".6"/>`;
const sparks=Array.from({length:60},()=>{const x=Math.random()*1080,y=Math.random()*1080,r=Math.random()*2+0.6;return `<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${r.toFixed(1)}" fill="#ffe7a3" opacity="${(Math.random()*.6+.2).toFixed(2)}"/>`}).join('');
const petals=Array.from({length:16},(_,i)=>`<ellipse cx="0" cy="-118" rx="22" ry="52" fill="${i%2?'#ff7a1a':'#e8306b'}" transform="rotate(${i*22.5})"/>`).join('')+Array.from({length:12},(_,i)=>`<ellipse cx="0" cy="-70" rx="16" ry="34" fill="${i%2?'#ffd23f':'#ff9f1c'}" transform="rotate(${i*30+15})"/>`).join('')+Array.from({length:24},(_,i)=>`<circle cx="0" cy="-170" r="7" fill="#ffd23f" transform="rotate(${i*15})"/>`).join('');
const html=`<meta charset="utf-8"><style>*{margin:0;padding:0}body{width:1080px;height:1080px;overflow:hidden;font-family:'Segoe UI',Arial,sans-serif;background:radial-gradient(circle at 50% 42%,#4a1e6b 0%,#2a0f45 45%,#13061f 100%)}
.wrap{position:absolute;inset:0}svg{position:absolute;inset:0}
.txt{position:absolute;left:0;right:0;top:210px;text-align:center;color:#fff}
.hindi{font-size:44px;color:#ffd77a;font-weight:700;letter-spacing:2px;text-shadow:0 0 18px rgba(255,190,80,.6)}
.big{font-family:Georgia,'Times New Roman',serif;font-size:132px;line-height:1;font-weight:700;margin-top:10px;background:linear-gradient(180deg,#fff3c4,#ffc54d 60%,#e8892a);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 4px 18px rgba(255,170,60,.45))}
.sub{font-size:30px;margin:22px auto 0;max-width:760px;line-height:1.45;color:#f5e9ff}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(0deg,rgba(0,0,0,.55),transparent);display:flex;align-items:flex-end;justify-content:space-between;padding:0 54px 34px}
.brand{display:flex;align-items:center;gap:16px}.brand img{height:74px;background:#fff;border-radius:12px;padding:6px}
.brand b{display:block;color:#fff;font-size:34px;font-family:Georgia,serif}.brand span{color:#ffd77a;font-size:15px;letter-spacing:4px;font-weight:700}
.contact{text-align:right;color:#fff;font-size:22px;font-weight:600;line-height:1.5}</style>
<div class="wrap"><svg viewBox="0 0 1080 1080"><defs>
<radialGradient id="glow"><stop offset="0" stop-color="#ffcf5a" stop-opacity=".75"/><stop offset="1" stop-color="#ff8a00" stop-opacity="0"/></radialGradient>
<linearGradient id="flame" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2a8"/><stop offset=".5" stop-color="#ffb52e"/><stop offset="1" stop-color="#ff5a1f"/></linearGradient>
<linearGradient id="clay" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2762b"/><stop offset="1" stop-color="#8f3512"/></linearGradient></defs>
${sparks}${wire}${lights}
<g transform="translate(540 1030) scale(.8)" opacity=".95">${petals}<circle r="40" fill="#fff4d1"/><circle r="22" fill="#e8306b"/></g>
${diya(230,860,1.25)}${diya(850,860,1.25)}${diya(400,930,.9)}${diya(680,930,.9)}
</svg>
<div class="txt"><div class="hindi">शुभ दीपावली</div><div class="big">Happy Diwali</div><p class="sub">May this festival of lights bring prosperity, good health and success to you and your family.</p></div>
<div class="foot"><div class="brand"><img src="${logo}"><div><b>Gugnani &amp; Co</b><span>CHARTERED ACCOUNTANTS</span></div></div><div class="contact">📞 +91-9953788989<br>gugnaniandco.com</div></div></div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});await p.setContent(html);await p.waitForTimeout(500);await p.screenshot({path:'diwali-post.png'});await b.close();})();

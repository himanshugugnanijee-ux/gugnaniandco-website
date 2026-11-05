(function(){var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
var els=document.querySelectorAll('section .card, section .rev, .stats>div, .content>div, .content>aside, .chips, section h2, .map');
els.forEach(function(e){e.classList.add('reveal')});
if('IntersectionObserver' in window&&!rm){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.12});els.forEach(function(e,i){e.style.transitionDelay=(i%4)*80+'ms';io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
var cs=document.querySelectorAll('.count');function runCount(c){var to=parseFloat(c.dataset.to),d=+c.dataset.dec||0,suf=c.dataset.suf||'',t0=null;function f(t){if(!t0)t0=t;var k=Math.min((t-t0)/1600,1),v=to*(1-Math.pow(1-k,3));c.textContent=v.toFixed(d)+suf;if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
if('IntersectionObserver' in window&&!rm){var co=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){runCount(en.target);co.unobserve(en.target)}})});cs.forEach(function(c){co.observe(c)})}else cs.forEach(function(c){c.textContent=c.dataset.to+(c.dataset.suf||'')});
var hero=document.querySelector('.hero'),st=document.querySelector('.story');
if(rm)return;
var steps=st?st.querySelectorAll('.step'):[],scenes=st?st.querySelectorAll('.scene'):[],num=st?st.querySelector('.big-num'):null,cur=-1,tick=false;
function upd(){tick=false;var y=scrollY;if(hero)hero.style.setProperty('--hy',Math.min(y,600)*0.3);
if(!st)return;var r=st.getBoundingClientRect(),tot=st.offsetHeight-innerHeight,p=Math.min(Math.max(-r.top/tot,0),1);st.style.setProperty('--p',p.toFixed(4));
var i=Math.min(Math.floor(p*4),3);if(i!==cur){cur=i;steps.forEach(function(s,k){s.classList.toggle('on',k===i)});scenes.forEach(function(s,k){s.classList.toggle('on',k===i)});if(num)num.textContent='0'+(i+1)}}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);upd();})();

document.querySelector('.burger').onclick=()=>document.querySelector('.menu').classList.toggle('on');
document.querySelector('.dd>a').addEventListener('click',e=>{if(innerWidth<=900){e.preventDefault();e.target.parentNode.classList.toggle('on')}});
const m=document.getElementById('qm');document.querySelectorAll('.openq').forEach(b=>b.onclick=e=>{e.preventDefault();m.classList.add('on')});
m.querySelector('.x').onclick=()=>m.classList.remove('on');m.onclick=e=>{if(e.target===m)m.classList.remove('on')};
document.querySelectorAll('form.lead').forEach(f=>f.onsubmit=e=>{e.preventDefault();const d=new FormData(f);
const t=`New enquiry from website%0AName: ${d.get('name')}%0APhone: ${d.get('phone')}%0AService: ${d.get('service')||''}%0AMessage: ${d.get('msg')||''}%0APage: ${location.pathname}`;
window.open('https://wa.me/919953788989?text='+t,'_blank');location.href=f.dataset.ty;});
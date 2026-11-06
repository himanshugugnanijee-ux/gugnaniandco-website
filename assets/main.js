(function(){var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
var els=document.querySelectorAll('section .card, section .rev, .stats>div, .content>div, .content>aside, .chips, section h2, .map');
els.forEach(function(e){e.classList.add('reveal')});
if('IntersectionObserver' in window&&!rm){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.12});els.forEach(function(e,i){e.style.transitionDelay=(i%4)*80+'ms';io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
var cs=document.querySelectorAll('.count');function runCount(c){var to=parseFloat(c.dataset.to),d=+c.dataset.dec||0,suf=c.dataset.suf||'',t0=null;function f(t){if(!t0)t0=t;var k=Math.min((t-t0)/1600,1),v=to*(1-Math.pow(1-k,3));c.textContent=v.toFixed(d)+suf;if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
if('IntersectionObserver' in window&&!rm){var co=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){runCount(en.target);co.unobserve(en.target)}})});cs.forEach(function(c){co.observe(c)})}else cs.forEach(function(c){c.textContent=c.dataset.to+(c.dataset.suf||'')});
var hero=document.querySelector('.hero'),sts=[].slice.call(document.querySelectorAll('.story'));
if(rm)return;
var S=sts.map(function(st){return{el:st,steps:st.querySelectorAll('.step'),scenes:st.querySelectorAll('.scene'),num:st.querySelector('.big-num'),cur:-1}}),tick=false;
function upd(){tick=false;var y=scrollY;if(hero)hero.style.setProperty('--hy',Math.min(y,600)*0.3);
S.forEach(function(o){var r=o.el.getBoundingClientRect();if(r.bottom<-200||r.top>innerHeight+200)return;var tot=o.el.offsetHeight-innerHeight,p=Math.min(Math.max(-r.top/tot,0),1),n=o.steps.length;o.el.style.setProperty('--p',p.toFixed(4));
var i=Math.min(Math.floor(p*n),n-1);if(i!==o.cur){o.cur=i;o.steps.forEach(function(s,k){s.classList.toggle('on',k===i)});o.scenes.forEach(function(s,k){s.classList.toggle('on',k===i)});if(o.num)o.num.textContent='0'+(i+1)}})}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);upd();})();

(function(){var bg=document.querySelector('.burger'),mn=document.querySelector('.menu'),hd=document.querySelector('header'),dd=document.querySelector('.dd'),dda=document.querySelector('.dd>a');
function setH(){document.documentElement.style.setProperty('--hh',Math.max(0,hd.getBoundingClientRect().bottom)+'px')}
function setOpen(o){setH();mn.classList.toggle('on',o);document.body.classList.toggle('menu-open',o);bg.textContent=o?'✕':'☰';bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu');if(!o)dd.classList.remove('on')}
bg.addEventListener('click',function(){setOpen(!mn.classList.contains('on'))});
dda.addEventListener('click',function(e){if(innerWidth<=900){e.preventDefault();var o=dd.classList.toggle('on');dda.setAttribute('aria-expanded',o);if(o)setTimeout(function(){dd.scrollIntoView({behavior:'smooth',block:'start'})},120)}});
mn.querySelectorAll('a:not(.dd>a)').forEach(function(a){a.addEventListener('click',function(){if(mn.classList.contains('on'))setOpen(false)})});
addEventListener('keydown',function(e){if(e.key==='Escape'&&mn.classList.contains('on'))setOpen(false)});
addEventListener('resize',function(){if(innerWidth>900&&mn.classList.contains('on'))setOpen(false)});})();

const m=document.getElementById('qm');document.querySelectorAll('.openq').forEach(b=>b.onclick=e=>{e.preventDefault();m.classList.add('on')});
m.querySelector('.x').onclick=()=>m.classList.remove('on');m.onclick=e=>{if(e.target===m)m.classList.remove('on')};
document.querySelectorAll('form.lead').forEach(f=>f.onsubmit=e=>{e.preventDefault();const d=new FormData(f);
const t=`New enquiry from website%0AName: ${d.get('name')}%0APhone: ${d.get('phone')}%0AService: ${d.get('service')||''}%0AMessage: ${d.get('msg')||''}%0APage: ${location.pathname}`;
window.open('https://wa.me/919953788989?text='+t,'_blank');location.href=f.dataset.ty;});
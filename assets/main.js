document.querySelector('.burger').onclick=()=>document.querySelector('.menu').classList.toggle('on');
document.querySelector('.dd>a').addEventListener('click',e=>{if(innerWidth<=900){e.preventDefault();e.target.parentNode.classList.toggle('on')}});
const m=document.getElementById('qm');document.querySelectorAll('.openq').forEach(b=>b.onclick=e=>{e.preventDefault();m.classList.add('on')});
m.querySelector('.x').onclick=()=>m.classList.remove('on');m.onclick=e=>{if(e.target===m)m.classList.remove('on')};
document.querySelectorAll('form.lead').forEach(f=>f.onsubmit=e=>{e.preventDefault();const d=new FormData(f);
const t=`New enquiry from website%0AName: ${d.get('name')}%0APhone: ${d.get('phone')}%0AService: ${d.get('service')||''}%0AMessage: ${d.get('msg')||''}%0APage: ${location.pathname}`;
window.open('https://wa.me/919953788989?text='+t,'_blank');location.href=f.dataset.ty;});
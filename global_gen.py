
# ---------- GLOBAL / COUNTRY PAGES ----------
page("global/index.html","International Accounting & Compliance Services | Gugnani & Co",
 "Accounting, bookkeeping, incorporation and tax compliance support for businesses in the USA, UK, UAE, Canada, Australia and Singapore from Gugnani & Co.",
 hero("International Accounting &amp; Compliance","Company formation, bookkeeping and tax compliance support for businesses in the USA, UK, UAE, Canada, Australia and Singapore – delivered by a qualified CA team in India.","../",names=[c["full"] for c in COUNTRIES],intl=True)+
 f'<section class="globe"><div class="wrap"><div class="globe-top"><h2>Choose your country</h2><select class="country-select" aria-label="Choose your country"><option value="">🌐 Select your country</option>{country_opts("../")}</select></div><div class="cgrid">{country_cards("../")}</div><p class="intl-note">{DISCLAIMER}</p></div></section>',
 1,crumbs=[("Home",""),("International","global/")])

for c in COUNTRIES:
    cc=c["cc"]; base=f"global/{cc}/"; r2="../../"
    names=[x[1] for x in c["services"]]
    flag=f'<span class="hero-flag"><img src="{r2}assets/flags/{c["flag"]}.svg" alt="" width="30" height="20">{c["full"]}</span>'
    cards="".join(f'<a class="card" href="{x[0]}.html"><h3>{x[1]}</h3><p>{x[2]}</p><small style="color:var(--p);font-weight:700">Learn more →</small></a>' for x in c["services"])
    hub_faq=[q for x in c["services"] for q in x[5]][:5]
    fh="".join(f"<details><summary>{q.split('|')[0]}</summary><p>{q.split('|')[1]}</p></details>" for q in hub_faq)
    body=hero(f'Accounting &amp; Compliance Services for {c["full"]} Businesses',c["tag"]+" Work with a qualified CA team that overlaps with "+c["tz"]+".",r2,crumb=f'<div class="crumb"><a href="{r2}index.html">Home</a> › <a href="../index.html">International</a> › {c["name"]}</div>'+flag,names=names,intl=True)
    body+=story_html(f'How we get you started in <em>{c["full"]}</em>',c["story"],eyebrow=c["name"]+" PROCESS",sid="process")
    body+=f'''<section><div class="wrap"><h2>Our Services in {c["full"]}</h2><p class="sub">{c["intro"]}</p><div class="grid">{cards}</div></div></section>
<section class="alt"><div class="wrap"><h2>Why clients in {c["full"]} work with us</h2><div class="why4"><div><b>Qualified CA team</b>Every file is reviewed by a Chartered Accountant.</div><div><b>Your time zone</b>Working hours that overlap with {c["tz"]}.</div><div><b>Cost-effective</b>Fixed monthly pricing – typically far below local rates.</div><div><b>Secure &amp; cloud-based</b>QuickBooks, Xero and secure document sharing.</div></div></div></section>
<section><div class="wrap"><h2>FAQs – {c["full"]}</h2>{fh}<p class="intl-note">{DISCLAIMER}</p></div></section>'''
    page(base+"index.html",f'{c["full"]} Accounting, Bookkeeping & Company Formation | Gugnani & Co',
         f'{c["tag"]} Gugnani & Co – CA firm supporting {c["full"]} businesses. WhatsApp +91-9953788989.',body,2,
         [{"@context":"https://schema.org","@type":"Service","serviceType":"Accounting and compliance services","provider":{"@id":SITE+"/#firm"},"areaServed":c["full"]}],
         [("Home",""),("International","global/"),(c["full"],base)],cc=cc)
    for slug,name,short,desc,inc,faqs,story in c["services"]:
        others="".join(f'<li><a href="{x[0]}.html">{x[1]}</a></li>' for x in c["services"] if x[0]!=slug)
        fq="".join(f"<details><summary>{q.split('|')[0]}</summary><p>{q.split('|')[1]}</p></details>" for q in faqs)
        incl="".join(f"<li>{i}</li>" for i in inc)
        b=hero(f'{name} – {c["full"]}',short+" Delivered by a qualified CA team working in "+c["tz"]+".",r2,crumb=f'<div class="crumb"><a href="{r2}index.html">Home</a> › <a href="../index.html">International</a> › <a href="index.html">{c["name"]}</a> › {name}</div>'+flag,sel=name,names=names,intl=True)
        b+=story_html(f'{name.split(" (")[0]} <em>Process</em>',story,eyebrow=c["name"]+" · STEP-BY-STEP",sid="process")
        b+=f'''<section><div class="wrap content"><div><h2>{name} for {c["full"]} businesses</h2><p>{desc}</p><h2>What's included</h2><ul class="ticks">{incl}</ul><h2>Frequently Asked Questions</h2>{fq}<p class="intl-note">{DISCLAIMER}</p></div>
<aside class="side card"><h3>{c["name"]} Services</h3><ul style="margin-left:18px">{others}</ul><p style="margin:14px 0 8px"><a class="btn" href="https://wa.me/{WA}" target="_blank" rel="noopener">💬 WhatsApp Us</a></p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p style="margin-top:10px"><a href="index.html">← All {c["name"]} services</a></p></aside></div></section>'''
        page(base+slug+".html",f'{name} – {c["full"]} | Gugnani & Co',f'{short} Gugnani & Co supports {c["full"]} businesses with {name.lower()}. WhatsApp +91-9953788989.',b,2,
             [{"@context":"https://schema.org","@type":"Service","serviceType":name,"provider":{"@id":SITE+"/#firm"},"areaServed":c["full"],"description":short},
              {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q.split('|')[0],"acceptedAnswer":{"@type":"Answer","text":q.split('|')[1]}} for q in faqs]}],
             [("Home",""),("International","global/"),(c["full"],base),(name,base+slug+".html")],cc=cc)

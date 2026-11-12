import os, json, shutil, datetime
from global_data import COUNTRIES, DISCLAIMER
OUT = "gugnaniandco"
shutil.rmtree(OUT, ignore_errors=True)
for d in ["", "services", "areas", "blog", "assets"]:
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

SITE = "https://gugnaniandco.com"
GTM_ID = "GTM-WFWH8J7L"
GTM_HEAD = "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','" + GTM_ID + "');</script>"
GTM_BODY = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' + GTM_ID + '" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
FIRM = "Gugnani & Co"
PHONE = "+91-9953788989"
TEL = "+919953788989"
WA = "919953788989"
EMAIL = "gugnaniandco@gmail.com"
ADDR = "130 Star Apartment, Sector 9, Rohini, Delhi 110085"
MAP = "https://www.google.com/maps?q=Star+Apartment+Sector+9+Rohini+Delhi+110085&output=embed"
MAPLINK = "https://www.google.com/maps/search/?api=1&query=Star+Apartment+Sector+9+Rohini+Delhi+110085"
TODAY = datetime.date(2026, 11, 1).isoformat()

# ---------------- SERVICES (unique content each) ----------------
SERVICES = [
 ("gst-registration","GST Registration","New GST registration for proprietors, partnerships, LLPs and companies in Delhi.",
  "Whether you have crossed the turnover threshold, started selling on Amazon or Flipkart, or need GSTIN for an inter-state supply, we file your REG-01 correctly the first time. Most rejections happen because of a mismatched rent agreement, missing NOC from the property owner or an unclear principal place of business photo. Our team checks every document before submission and replies to any clarification notice (REG-03) within the deadline.",
  ["PAN, Aadhaar & photo of proprietor / partners / directors","Address proof of business place with NOC or rent agreement","Bank statement or cancelled cheque","Authorisation letter / board resolution"],
  ["Who must register for GST?|Businesses with aggregate turnover above ₹40 lakh (goods) or ₹20 lakh (services) in Delhi, plus anyone making inter-state taxable supplies or selling through e-commerce operators.","How long does GST registration take?|Usually 3–7 working days after Aadhaar authentication, provided no clarification is raised.","Can I register from my home address?|Yes, a residential address can be the principal place of business with proper ownership proof or NOC."]),
 ("gst-return-filing","GST Return Filing","Monthly and quarterly GSTR-1, GSTR-3B, QRMP and annual GSTR-9 filing.",
  "Late GST returns attract ₹50 per day late fee plus 18% interest, and repeated non-filing can lead to cancellation of your GSTIN. We take over your sales and purchase data every month, reconcile it with GSTR-2B so you claim only eligible input tax credit, and file GSTR-1 and GSTR-3B on time. For small businesses we evaluate whether the QRMP scheme reduces your compliance load.",
  ["Sales invoices / sales register","Purchase invoices and expense bills","Credit & debit notes","E-way bill data if applicable"],
  ["What is the due date for GSTR-3B?|Generally the 20th of the following month for monthly filers; 22nd/24th of the month after the quarter for QRMP filers depending on state.","What if I have nil sales?|You still have to file a nil return; it can be filed by SMS but we recommend portal filing to avoid errors.","Do you file GSTR-9 annual return?|Yes, along with GSTR-9C reconciliation wherever applicable."]),
 ("income-tax-return-filing","Income Tax Return Filing","ITR filing for salaried, business, professionals, NRIs and senior citizens.",
  "Choosing the wrong ITR form or missing an income shown in your AIS is the most common reason for a defective-return notice. We match your Form 16, Form 26AS and Annual Information Statement line-by-line, compare the old and new tax regime for you, and claim every deduction you are legally entitled to—80C, 80D, HRA, home-loan interest and capital-gain exemptions.",
  ["PAN & Aadhaar","Form 16 / salary slips","Bank interest certificates and AIS","Capital gains statements from broker","Investment & insurance proofs"],
  ["What is the last date to file ITR?|For non-audit individuals it is usually 31 July; belated returns can be filed until 31 December with late fee.","Which regime is better, old or new?|It depends on your deductions. We calculate both and file under the one that saves more tax.","Can you file ITR for NRIs?|Yes, including DTAA relief and Indian rental or capital-gain income."]),
 ("tds-return-filing","TDS Return Filing","Quarterly TDS/TCS returns 24Q, 26Q, 27Q and Form 16/16A issue.",
  "Employers, landlords paying above threshold and businesses paying contractors or professionals must deduct TDS and file quarterly statements. A wrong challan mapping or PAN error creates short-deduction demands on TRACES. We prepare your 24Q, 26Q and 27Q, correct past defaults, and issue Form 16 and 16A to your deductees.",
  ["TAN details","Challan (ITNS 281) copies","Deductee PAN and payment details","Salary details for 24Q"],
  ["What is the penalty for late TDS return?|₹200 per day under section 234E, up to the TDS amount, plus possible penalty under 271H.","Can you resolve TRACES demand notices?|Yes, we file correction statements and close short-payment and short-deduction defaults.","Do I need TAN?|Any person required to deduct TDS must obtain a TAN; we can apply for it too."]),
 ("company-registration","Private Limited Company Registration","Incorporate a Pvt Ltd company with DSC, DIN, name approval and PAN/TAN.",
  "A private limited company gives limited liability, easier fundraising and better credibility with banks and large clients. We handle the full SPICe+ process—digital signatures, name reservation, MOA/AOA drafting, PAN, TAN, EPFO, ESIC and bank account linkage—so you get your Certificate of Incorporation without running to the ROC.",
  ["PAN, Aadhaar and photos of directors","Registered office proof and NOC","Utility bill not older than 2 months","Proposed company names (2 options)"],
  ["How many people are needed?|Minimum 2 directors and 2 shareholders (can be the same persons).","How long does incorporation take?|Typically 7–12 working days, subject to MCA approval.","Is a minimum capital required?|No, there is no minimum paid-up capital requirement now."]),
 ("llp-registration","LLP Registration","Limited Liability Partnership incorporation with LLP agreement drafting.",
  "LLPs suit professional firms and small businesses that want limited liability without the heavy compliance of a company. We reserve the name through RUN-LLP, file FiLLiP, draft a balanced LLP agreement covering profit share, capital and exit, and file Form 3 within 30 days of incorporation.",
  ["Designated partners' KYC","Registered office proof","Capital contribution details","Profit-sharing ratio"],
  ["LLP or Pvt Ltd—which is better?|LLP has lower compliance; Pvt Ltd is better if you plan to raise equity funding.","Is audit compulsory for LLP?|Only if turnover exceeds ₹40 lakh or contribution exceeds ₹25 lakh.","What annual filings are required?|Form 8 and Form 11 every year, plus income-tax return."]),
 ("partnership-firm-registration","Partnership Firm Registration","Partnership deed drafting and registration with Registrar of Firms, Delhi.",
  "A properly drafted partnership deed avoids most future disputes between partners. We draft the deed with clauses for capital, interest, remuneration within section 40(b) limits, admission and retirement, get it stamped and register the firm with the Registrar of Firms, Delhi, followed by PAN and bank account opening.",
  ["Partners' PAN & Aadhaar","Business address proof","Capital and profit-sharing terms","Stamp paper as per Delhi stamp duty"],
  ["Is registration of partnership mandatory?|Not mandatory, but an unregistered firm cannot sue third parties to enforce contracts.","Can the deed be changed later?|Yes, through a supplementary deed.","Is partner salary deductible?|Yes, within section 40(b) limits if authorised in the deed."]),
 ("roc-compliance","ROC & MCA Annual Compliance","AOC-4, MGT-7, DIR-3 KYC, ADT-1 and event-based ROC filings.",
  "Missing ROC filings attract ₹100 per day additional fees per form and can disqualify directors. We maintain a compliance calendar for your company or LLP, hold board and AGM minutes, and file AOC-4, MGT-7/7A, DPT-3, MSME-1, ADT-1 and DIR-3 KYC before due dates.",
  ["Audited financial statements","Shareholding details","Board and AGM minutes","Director KYC"],
  ["What if my company hasn't filed for years?|We can regularise past defaults and evaluate the Company Fresh Start / condonation schemes when available.","Can a dormant company be closed?|Yes, through strike-off under section 248.","Is DIR-3 KYC yearly?|Directors must update KYC as per the current MCA rules; we track it for you."]),
 ("accounting-bookkeeping","Accounting & Bookkeeping","Monthly bookkeeping in Tally / Zoho / cloud accounting with MIS reports.",
  "Clean books are the foundation of tax savings and loan approvals. We offer both traditional and cloud-based bookkeeping, so you can see your accounts live on mobile through Zoho Books, Tally on Cloud or QuickBooks. Our accountants record sales, purchases, expenses, bank and cash entries every month, reconcile bank and GST data, and give you a simple MIS showing profit, receivables and payables so you can make decisions with real numbers.",
  ["Bank statements","Sales & purchase invoices","Expense vouchers","Previous year balance sheet"],
  ["Which software do you use?|Tally Prime, Tally on Cloud, Zoho Books, QuickBooks Online and Busy. For remote clients we recommend cloud accounting so books stay updated in real time.","Can you work from my office?|Yes, we offer both on-site and remote bookkeeping.","How much does bookkeeping cost?|It depends on number of transactions; we give a fixed monthly quote after a free review."]),
 ("cloud-accounting","Cloud Accounting Services","Online cloud accounting on Zoho Books, Tally on Cloud and QuickBooks — access your books anytime, anywhere.",
  "With cloud accounting your books live securely online instead of on one office computer. You and our team see the same live data from mobile or laptop, invoices go out with GST details automatically, bank feeds pull transactions daily, and your CA can review entries in real time instead of waiting for month-end. We set up Zoho Books, Tally on Cloud or QuickBooks for your business, migrate your existing data, train your staff and then handle day-to-day entries, reconciliation and monthly MIS remotely — no need to send bills by courier or visit our office.",
  ["Existing Tally / Excel data or last balance sheet","Bank account details for bank feeds","GSTIN and invoice format","List of users who need access"],
  ["What is cloud accounting?|Accounting software that runs online, so your books are available on any device with secure login, and your CA can work on the same data in real time.","Which software do you support?|Zoho Books, Tally on Cloud (Tally Prime hosted), QuickBooks Online and Busy on cloud. We suggest the right one for your size and industry.","Is my data safe on the cloud?|Reputed cloud providers use encryption, backups and access controls. We set role-based access so each user sees only what they need.","Can you shift my old Tally data to the cloud?|Yes, we migrate masters, opening balances and past entries and verify them before you go live."]),
 ("tax-audit","Tax Audit (Section 44AB)","Tax audit and Form 3CA/3CB-3CD reporting for businesses and professionals.",
  "If your business turnover exceeds ₹1 crore (₹10 crore with mostly digital transactions) or your professional receipts exceed ₹50 lakh, a tax audit is mandatory. We verify books, prepare the 44 clauses of Form 3CD, and upload the audit report before the due date to save the 0.5% penalty under section 271B.",
  ["Complete books of accounts","Fixed asset register","GST returns","Loan and TDS details"],
  ["What is the due date of tax audit?|Generally 30 September of the assessment year.","What is the penalty for not getting audited?|0.5% of turnover up to ₹1.5 lakh.","Is tax audit needed under presumptive scheme?|Only in specific cases where lower profits are declared and income exceeds the basic exemption."]),
 ("statutory-audit","Statutory & Internal Audit","Company statutory audit, internal audit and stock audit services.",
  "Every company must get its accounts audited by a chartered accountant regardless of turnover. We conduct independent statutory audits under the Companies Act and Standards on Auditing, and internal audits that find leakages in purchase, inventory and cash processes before they become losses.",
  ["Trial balance and ledgers","Bank confirmations","Inventory records","Statutory registers"],
  ["Is audit required for a small company?|Yes, statutory audit applies to all companies.","What does internal audit cover?|Process controls, purchase, sales, payroll, inventory and compliance checks.","Do you do stock audits for banks?|Yes, as per lending bank formats."]),
 ("income-tax-notice","Income Tax Notice Handling","Reply to 143(1), 139(9), 148, 142(1) and scrutiny notices.",
  "An income tax notice does not always mean you did something wrong—often it is a mismatch between your ITR and AIS. We read the notice, identify the exact issue, collect evidence and file a reasoned response on the e-filing portal, and represent you in faceless assessment and appeals before CIT(A).",
  ["Copy of the notice","Filed ITR and computation","AIS / 26AS","Supporting bank and investment documents"],
  ["What is a 143(1) intimation?|A processing intimation showing adjustments or demand; it can be rectified if incorrect.","How much time do I have to reply?|Usually 15–30 days as mentioned in the notice; don't ignore it.","Can you handle appeals?|Yes, we file appeals before CIT(A) and assist with ITAT matters."]),
 ("msme-udyam-registration","MSME / Udyam Registration","Udyam registration for priority lending, subsidies and delayed-payment protection.",
  "Udyam registration unlocks collateral-free loans, interest subvention, government tender benefits and protection under the MSMED Act if your buyers delay payments beyond 45 days. We register you correctly with the right NIC codes and update the certificate as your turnover grows.",
  ["Aadhaar of proprietor / authorised person","PAN of business","Bank details","Business activity and NIC code"],
  ["Is Udyam free?|Government registration is free; we charge only for professional assistance.","Can traders register?|Yes, retail and wholesale traders can register for priority sector lending.","Does it expire?|No, but it must be updated with ITR and GST data."]),
 ("trademark-registration","Trademark Registration","Brand name and logo trademark search, filing and objection reply.",
  "Your brand is an asset—protect it before someone else files it. We run a detailed search on the IP India database, select the right class, file TM-A, and draft replies to examination reports and oppositions so your application moves to registration.",
  ["Brand name / logo","Applicant KYC","User date proof (if already in use)","MSME certificate for reduced fee"],
  ["How long does trademark registration take?|You can use ™ from filing; final registration usually takes 12–18 months.","What is a trademark class?|Goods and services are divided into 45 classes; you file in the class you trade in.","Can you reply to objections?|Yes, we draft examination replies and attend hearings."]),
 ("payroll-pf-esi","Payroll, PF & ESI Compliance","Salary processing, PF and ESIC registration and monthly returns.",
  "Once you employ 20 people PF becomes mandatory, and ESIC applies at 10 employees in notified areas of Delhi. We register your establishment, process monthly payroll, file ECR and ESIC returns and handle professional and labour-law compliances so your employees are paid correctly and on time.",
  ["Employee KYC and bank details","Salary structure","Attendance data","Establishment registration documents"],
  ["When is PF due?|By the 15th of the following month.","Can you process salary for a small team?|Yes, from 2 employees onwards.","Do you handle PF withdrawals?|We guide employees with claims and KYC issues."]),
 ("nri-taxation","NRI Taxation & Advisory","NRI ITR, lower TDS certificate, property sale and repatriation (15CA/15CB).",
  "NRIs selling property in India face 20%+ TDS deducted by the buyer unless a lower deduction certificate is obtained. We apply for Form 13 certificates, file NRI income-tax returns, claim DTAA benefits and issue Form 15CA/15CB so your money can be remitted abroad smoothly.",
  ["Passport and visa / OCI","Indian PAN","Property sale documents","Bank NRO/NRE statements"],
  ["Do NRIs need to file ITR?|Yes, if Indian income exceeds the basic exemption or to claim TDS refund.","What is 15CA/15CB?|Forms required by banks for foreign remittance confirming taxes are paid.","Can I reduce TDS on property sale?|Yes, through a lower deduction certificate under section 197."]),
 ("startup-advisory","Startup & Business Advisory","DPIIT recognition, business plans, project reports and CMA data for loans.",
  "From choosing the right business structure to getting DPIIT startup recognition and preparing bank-ready project reports, we help first-time founders avoid costly mistakes. We also prepare CMA data and projections for working-capital and term loans.",
  ["Business idea / pitch","Founders' KYC","Projected financials","Existing registrations"],
  ["What is DPIIT recognition?|Government recognition giving tax and compliance benefits to eligible startups.","Do you make project reports for loans?|Yes, including CMA data for banks.","Can you help with Section 80-IAC?|Yes, we assist eligible startups to apply for tax holiday."]),
]

# ---------------- AREAS (unique content each) ----------------
AREAS = [
 ("rohini","Rohini","110085","our home base in Sector 9","Rohini's many sectors are home to thousands of traders, salaried professionals and small manufacturers. Being located right here at Star Apartment, Sector 9, we offer walk-in consultations, same-day document pickup and quick GST and ITR filing for residents of Sectors 1 to 37."),
 ("pitampura","Pitampura","110034","close to Netaji Subhash Place","Pitampura and Netaji Subhash Place host a large number of corporate offices, retail showrooms and coaching institutes. We help these businesses with company compliance, payroll, GST and tax audits, and assist families in Pitampura with ITR and capital-gain planning on property sales."),
 ("prashant-vihar","Prashant Vihar","110085","a short drive from Rohini Sector 9","Prashant Vihar's residential community includes doctors, lawyers, consultants and business owners who need professional-income tax planning. We file ITRs under section 44ADA, advise on advance tax and handle investment-related capital gains for Prashant Vihar residents."),
 ("rani-bagh","Rani Bagh","110034","near Rishi Nagar and Shakurpur","Rani Bagh's busy markets are full of garment, footwear and general traders. We specialise in GST return filing, e-way bill guidance and bookkeeping for Rani Bagh shopkeepers, plus ITR filing for proprietors under the presumptive scheme."),
 ("shalimar-bagh","Shalimar Bagh","110088","next to Haiderpur and Azadpur","Shalimar Bagh combines upscale residential blocks with commercial complexes. Our firm supports Shalimar Bagh businesses with company registration and statutory audits, and families with wealth-related tax planning and NRI property matters."),
 ("ashok-vihar","Ashok Vihar","110052","near Wazirpur Industrial Area","Ashok Vihar sits next to Wazirpur Industrial Area, so many residents run manufacturing and trading units. We provide GST, tax audit, MSME registration and bank loan project reports to Ashok Vihar entrepreneurs."),
 ("model-town","Model Town","110009","close to Mall Road and GTB Nagar","Model Town's established families and businesses rely on us for estate-related tax planning, partnership deeds and ITR filing. We also assist students' parents in Model Town with education-loan and remittance documentation."),
 ("shakurpur","Shakurpur","110034","beside Britannia Chowk","Shakurpur has a dense cluster of small businesses and service providers. We offer affordable GST registration, monthly filing packages and TDS compliance tailored to small Shakurpur enterprises."),
 ("wazirpur","Wazirpur","110052","covering Wazirpur Industrial Area","Wazirpur Industrial Area is a hub for steel utensil, metal and plastic manufacturers. We handle GST input credit reconciliation, stock audits for bank limits, payroll and PF for factory workers, and tax audits for Wazirpur units."),
 ("keshav-puram","Keshav Puram","110035","near Lawrence Road","Keshav Puram and Lawrence Road industrial belt house many fabrication and printing units. We help Keshav Puram businesses with bookkeeping, GST, TDS and income-tax notice replies."),
 ("paschim-vihar","Paschim Vihar","110063","on the Outer Ring Road side","Paschim Vihar residents include salaried professionals and retailers. We offer ITR filing, home-loan tax benefits advice and GST support for Paschim Vihar shops and service providers."),
 ("punjabi-bagh","Punjabi Bagh","110026","near Punjabi Bagh Club","Punjabi Bagh is known for high-net-worth families and established trading houses. Our firm assists with capital-gain tax planning on property, HUF taxation, company audits and trademark protection for family brands."),
 ("janakpuri","Janakpuri","110058","in West Delhi's District Centre","Janakpuri District Centre has many offices, clinics and IT service firms. We provide company incorporation, payroll, ROC compliance and professional-income ITR filing to Janakpuri clients through on-site visits and online meetings."),
 ("narela","Narela","110040","covering Narela Industrial Area","Narela Industrial Area and DSIIDC units need strong compliance support. We provide factory accounting, GST, PF/ESI and statutory audit services for Narela manufacturers, with regular client visits."),
 ("bawana","Bawana","110039","covering Bawana DSIIDC Industrial Area","Bawana's DSIIDC sectors house hundreds of manufacturing units. We help Bawana industrialists with MSME registration, GST, bank CMA reports and labour-law compliance."),
 ("alipur","Alipur","110036","on the GT Karnal Road","Alipur's growing warehouses, transport companies and farmhouse businesses need practical tax advice. We assist Alipur clients with GST on transport, TDS on rent and contract payments, and ITR filing."),
 ("badli","Badli","110042","near Badli Industrial Area","Badli Industrial Area has numerous small factories and traders. We provide bookkeeping, GST return filing and income-tax compliance to Badli businesses at affordable fixed fees."),
 ("mangolpuri","Mangolpuri","110083","near Mangolpuri Industrial Area","Mangolpuri's industrial phases host footwear, plastic and packaging units. We offer GST registration, return filing and loan documentation for Mangolpuri entrepreneurs."),
 ("sultanpuri","Sultanpuri","110086","adjacent to Rohini","Sultanpuri residents and small shop owners rely on us for affordable ITR filing, PAN-Aadhaar issues, GST registration and Udyam certificates."),
 ("budh-vihar","Budh Vihar","110086","next to Rohini Sector 21","Budh Vihar is a fast-growing residential area with many new businesses. We help Budh Vihar startups choose the right structure and keep their books and GST compliant from day one."),
 ("kirari","Kirari & Prem Nagar","110086","on the Rohini–Nangloi stretch","Kirari and Prem Nagar have many small traders and home-based businesses. We provide low-cost GST, ITR and MSME registration services with doorstep document collection."),
 ("mukherjee-nagar","Mukherjee Nagar","110009","near the coaching hub","Mukherjee Nagar's coaching institutes, PG owners and libraries have unique GST and income-tax questions. We advise on GST applicability on education services, rental income taxation and TDS."),
 ("gtb-nagar","GTB Nagar & Kingsway Camp","110009","near Delhi University North Campus","GTB Nagar and Kingsway Camp businesses—from cafés to retail—trust us for GST registration, food-business compliance and bookkeeping."),
 ("jahangirpuri","Jahangirpuri & Azadpur","110033","near Azadpur Mandi","Azadpur Mandi commission agents and fruit and vegetable traders have specific tax rules. We handle presumptive taxation, TDS, GST exemptions on agricultural produce and tax audits for Jahangirpuri and Azadpur traders."),
]

# ---------------- BLOGS ----------------
BLOGS = [
 ("how-to-choose-best-ca-rohini","How to Choose the Best CA in Rohini, Delhi – A Practical Checklist","Looking for the best CA services in Rohini or North-West Delhi? Use this 8-point checklist before you hire a chartered accountant.",
  ["Searching for the <b>best CA in Rohini</b> or the <b>best CA services near me</b>? The right chartered accountant saves you tax, keeps you away from notices and gives you peace of mind. Instead of going only by advertisements or ratings, check these points before you decide.",
   "<b>1. Verify ICAI membership.</b> Every practising chartered accountant has an ICAI membership number and every CA firm has a Firm Registration Number (FRN). Ask for them and verify on the ICAI website.",
   "<b>2. Experience with your kind of work.</b> GST for traders, ITR for salaried employees, company compliance for startups and audits for manufacturers each need different expertise. Ask how often the firm handles cases like yours.",
   "<b>3. Clear, written fee quote.</b> The best CA services come with fixed and transparent pricing agreed before work starts – no surprise charges at filing time.",
   "<b>4. Responsiveness.</b> Due dates do not wait. Choose a CA who picks up the phone, replies on WhatsApp and sends reminders before every deadline.",
   "<b>5. A local office you can visit.</b> For Rohini, Pitampura, Prashant Vihar and Rani Bagh residents, a nearby office means quick document handover and face-to-face meetings when needed.",
   "<b>6. Technology.</b> Online document sharing, cloud accounting (Zoho Books, Tally on Cloud) and digital records make compliance faster and safer.",
   "<b>7. Notice and scrutiny support.</b> Ask whether the CA will reply to GST and income tax notices and represent you if the department raises questions.",
   "<b>8. Confidentiality.</b> Your financial data is sensitive. A professional CA firm keeps it secure and never shares it without your consent.",
   "Gugnani &amp; Co is a chartered accountant firm at 130 Star Apartment, Sector 9, Rohini. If you are comparing CA firms in Rohini and North-West Delhi, call +91-9953788989 to discuss your requirement – the first consultation is free."]),
 ("itr-filing-checklist-2026","ITR Filing Checklist for FY 2025-26: Documents You Need","A practical document checklist for salaried and business taxpayers before filing ITR this year.",
  ["Start with your AIS and Form 26AS. These show every income the department knows about—salary, interest, dividends, mutual-fund sales and even high-value purchases. Any income missing from your return is the fastest way to receive a notice.","Salaried people need Form 16, rent receipts for HRA, and home-loan interest certificates. Business owners need their profit and loss account, balance sheet, GST returns and bank statements.","Finally, compare the old and new tax regimes before filing. For many people without big deductions, the new regime now gives lower tax—but we always calculate both."]),
 ("gst-registration-mistakes","7 Common Mistakes That Get GST Registration Rejected","Avoid the errors that cause GST clarification notices and rejections in Delhi.",
  ["Uploading a rent agreement without the owner's NOC, or an electricity bill in a different name, is the most frequent reason for rejection.","Choosing the wrong HSN/SAC codes or business constitution also triggers queries. Make sure the business name on your PAN matches your application.","Respond to any REG-03 notice within 7 working days—otherwise the application is rejected automatically."]),
 ("old-vs-new-tax-regime","Old vs New Tax Regime: Which Should You Choose?","A simple way to decide between the two income-tax regimes.",
  ["The new regime offers lower slab rates and a higher standard deduction but removes most deductions like 80C, 80D and HRA.","If your total deductions are modest, the new regime usually wins. If you have home-loan interest, HRA and full 80C investments, the old regime may still save more.","Salaried employees can switch every year; business owners have restrictions on switching back and forth."]),
 ("pvt-ltd-vs-llp","Private Limited vs LLP: Which Is Right for Your Business?","Comparing compliance, taxation and funding for the two most popular structures.",
  ["Both structures give limited liability. A private limited company is preferred by investors and banks because equity can be issued easily.","An LLP has fewer compliance requirements—audit applies only above certain limits—and no dividend distribution complications.","If you plan to raise venture capital or issue ESOPs, choose a company. For professional or family businesses, an LLP is often simpler."]),
 ("income-tax-notice-what-to-do","Received an Income Tax Notice? Here's What to Do","Step-by-step guide to responding to common income tax notices.",
  ["Don't panic and don't ignore it. First check the section under which the notice is issued—143(1), 139(9), 142(1) or 148 each mean something different.","Verify the notice on the e-filing portal using its DIN to confirm it is genuine.","Collect supporting documents and reply within the given time. A professional reply backed by evidence usually closes the matter quickly."]),
 ("tds-on-rent-and-contractors","TDS on Rent and Contractor Payments Explained","Who must deduct TDS on rent and contract payments, and at what rates.",
  ["Businesses paying rent above the annual threshold must deduct TDS under section 194-I, while individuals paying high monthly rent fall under section 194-IB.","Payments to contractors attract TDS under section 194C at 1% for individuals/HUFs and 2% for others.","Deposit TDS by the 7th of next month and file quarterly returns to avoid interest and late fees."]),
]

REVIEWS = [
 ("Rajesh Malhotra","Rohini Sector 7","Got my GST registration done in 4 days without any query. Very professional team and transparent fees."),
 ("Neha Arora","Pitampura","They found a mistake in my previous ITR and saved me from a notice. Highly recommended CA in Rohini."),
 ("Sandeep Jain","Wazirpur","Handling our factory's accounts, GST and tax audit for two years now. Always on time and easy to reach."),
 ("Pooja Bansal","Prashant Vihar","Helped me register my private limited company quickly. Explained every step clearly."),
 ("Amit Gupta","Rani Bagh","Replied to my income tax notice and got the demand cancelled. Very knowledgeable."),
 ("Harpreet Singh","Shalimar Bagh","As an NRI I needed 15CA/15CB and lower TDS certificate on property sale—handled perfectly and remotely."),
]

CSS = """
/* ===== motion ===== */
.story.svc{height:330vh}.story.svc + .story.svc{border-top:1px solid rgba(255,255,255,.08)}
.scene text{font-family:Arial,Helvetica,sans-serif}
.scert .card{transform:translateY(60px);opacity:0;transition:all .7s cubic-bezier(.2,.7,.2,1)}.scert.on .card{transform:none;opacity:1}
.scert .seal{transform-origin:290px 270px;transform:scale(0) rotate(-180deg);transition:transform .7s cubic-bezier(.5,1.6,.5,1) .6s}.scert.on .seal{transform:none}
.scert .shine{transform:translateX(-260px);transition:transform 1.2s ease 1s}.scert.on .shine{transform:translateX(260px)}
.sportal .fill{transform-origin:110px 0;transform:scaleX(0);transition:transform 1.6s ease .3s}.sportal.on .fill{transform:scaleX(1)}
.sportal .ok{transform-origin:200px 290px;transform:scale(0);transition:transform .5s cubic-bezier(.5,1.8,.5,1) 1.9s}.sportal.on .ok{transform:none}
.sportal .cursor{transition:transform 1s ease .2s}.sportal.on .cursor{transform:translate(-40px,-30px)}
.sotp .dg{opacity:0;transform:translateY(-14px);transition:all .3s ease}.sotp.on .dg{opacity:1;transform:none}
.sotp.on .dg:nth-of-type(2){transition-delay:.3s}.sotp.on .dg:nth-of-type(3){transition-delay:.6s}.sotp.on .dg:nth-of-type(4){transition-delay:.9s}
.sotp .shield{transform-origin:300px 120px;transform:scale(0);transition:transform .5s cubic-bezier(.5,1.8,.5,1) 1.3s}.sotp.on .shield{transform:none}
.scal .circ{stroke-dasharray:420;stroke-dashoffset:420;transition:stroke-dashoffset .9s ease .4s}.scal.on .circ{stroke-dashoffset:0}
.scal.on .bell{animation:ring 1s ease 1.2s 2;transform-origin:340px 50px}@keyframes ring{0%,100%{transform:rotate(0)}25%{transform:rotate(18deg)}75%{transform:rotate(-18deg)}}
.smoney .coin{transform:translateY(-170px);opacity:0;transition:transform .6s cubic-bezier(.5,1.4,.5,1),opacity .2s}.smoney.on .coin{transform:none;opacity:1}
.smoney.on .coin:nth-of-type(2){transition-delay:.25s}.smoney.on .coin:nth-of-type(3){transition-delay:.5s}
.smoney .paid{transform-origin:200px 330px;transform:scale(0);transition:transform .5s cubic-bezier(.5,1.8,.5,1) 1.1s}.smoney.on .paid{transform:none}
.srec .ln{stroke-dasharray:90;stroke-dashoffset:90;transition:stroke-dashoffset .5s ease}.srec.on .ln{stroke-dashoffset:0}
.srec.on .ln:nth-of-type(2){transition-delay:.35s}.srec.on .ln:nth-of-type(3){transition-delay:.7s}.srec.on .ln:nth-of-type(4){transition-delay:1.05s}
.srec .ok{transform-origin:200px 335px;transform:scale(0);transition:transform .5s cubic-bezier(.5,1.8,.5,1) 1.5s}.srec.on .ok{transform:none}
@media(max-width:900px){.story.svc{height:300vh}}

.hero{position:relative;overflow:hidden}.hero .wrap{position:relative;z-index:2}
.hero:before,.hero:after{content:"";position:absolute;border-radius:50%;pointer-events:none;z-index:1}
.hero:before{width:520px;height:520px;right:-140px;top:-180px;background:radial-gradient(circle,rgba(242,169,0,.28),transparent 70%);transform:translateY(calc(var(--hy,0)*1px))}
.hero:after{width:380px;height:380px;left:-120px;bottom:-160px;background:radial-gradient(circle,rgba(255,255,255,.12),transparent 70%);transform:translateY(calc(var(--hy,0)*-0.6px))}
.hero h1,.hero p,.hero .btn,.hero .form{animation:rise .9s cubic-bezier(.2,.7,.2,1) both}
.hero p{animation-delay:.12s}.hero .btn{animation-delay:.24s}.hero .form{animation-delay:.36s}
@keyframes rise{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.in{opacity:1;transform:none}
.story{height:420vh;position:relative;background:#0a2540;color:#fff}
.story-sticky{position:sticky;top:0;height:100vh;overflow:hidden;display:flex;align-items:center}
.story-bg span{position:absolute;border-radius:50%;filter:blur(10px);opacity:.35;transition:transform .2s linear}
.story-bg span:nth-child(1){width:600px;height:600px;background:radial-gradient(circle,#11528f,transparent 70%);left:-200px;top:-150px;transform:translate(calc(var(--p,0)*200px),calc(var(--p,0)*120px))}
.story-bg span:nth-child(2){width:500px;height:500px;background:radial-gradient(circle,rgba(242,169,0,.5),transparent 70%);right:-160px;bottom:-200px;transform:translate(calc(var(--p,0)*-160px),calc(var(--p,0)*-200px))}
.story-bg span:nth-child(3){width:300px;height:300px;background:radial-gradient(circle,rgba(15,157,88,.5),transparent 70%);left:45%;top:60%;transform:scale(calc(.6 + var(--p,0)))}
.story-grid{position:relative;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;width:100%}
.eyebrow{color:#f2a900;font-weight:800;letter-spacing:4px;font-size:14px;margin-bottom:10px}
.story-h{color:#fff;font-size:40px;line-height:1.15;margin-bottom:26px}.story-h em{color:#f2a900;font-style:normal}
.steps{list-style:none}.step{display:flex;gap:18px;padding:14px 0 14px 18px;border-left:3px solid rgba(255,255,255,.15);opacity:.35;transform:translateX(0);transition:all .5s ease}
.step b{font-size:22px;color:#f2a900;min-width:34px}.step h3{font-size:21px;margin-bottom:4px}.step p{font-size:15px;opacity:.85;max-height:0;overflow:hidden;transition:max-height .5s ease}
.step.on{opacity:1;border-left-color:#f2a900;transform:translateX(8px)}.step.on p{max-height:90px}
.story-bar{height:4px;background:rgba(255,255,255,.15);border-radius:4px;margin-top:22px;overflow:hidden}.story-bar i{display:block;height:100%;width:calc(var(--p,0)*100%);background:linear-gradient(90deg,#f2a900,#0f9d58)}
.story-visual{position:relative;aspect-ratio:1;max-width:480px;width:100%;margin:auto}
.ring{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}
.ring-bg{fill:none;stroke:rgba(255,255,255,.08);stroke-width:10}.ring-fg{fill:none;stroke:#f2a900;stroke-width:10;stroke-linecap:round;stroke-dasharray:1131;stroke-dashoffset:calc(1131 - var(--p,0)*1131)}
.scene{position:absolute;inset:8%;opacity:0;transform:scale(.85) rotate(-4deg);transition:opacity .6s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.scene.on{opacity:1;transform:none}.scene svg{width:100%;height:100%;overflow:visible}
.big-num{position:absolute;right:-10px;bottom:-20px;font-size:140px;font-weight:900;color:rgba(255,255,255,.06);line-height:1}
.s1 .fly{transition:transform 1s cubic-bezier(.2,.7,.2,1) .2s,opacity 1s .2s}.s1 .f1{transform:translate(-60px,-40px) rotate(-20deg);opacity:0}.s1 .f2{transform:translate(60px,40px) rotate(20deg);opacity:0}
.s1.on .f1{transform:translate(110px,0) rotate(-6deg) scale(.6);opacity:1}.s1.on .f2{transform:translate(-150px,-40px) rotate(6deg) scale(.6);opacity:1}
.s1 .chat rect{transform-origin:150px 0;transform:scaleX(0);transition:transform .5s ease}.s1.on .chat rect{transform:scaleX(1)}.s1.on .chat rect:nth-child(2){transition-delay:.25s}.s1.on .chat rect:nth-child(3){transition-delay:.5s}
.tick{stroke-dasharray:40;stroke-dashoffset:40;transition:stroke-dashoffset .6s ease .9s}.s1.on .tick{stroke-dashoffset:0}
.s2 .rows rect{fill:#e1e7ef}.s2 .checks path{fill:none;stroke:#0f9d58;stroke-width:5;stroke-linecap:round;stroke-dasharray:30;stroke-dashoffset:30;transition:stroke-dashoffset .4s ease}
.s2.on .checks path:nth-child(1){stroke-dashoffset:0;transition-delay:.6s}.s2.on .checks path:nth-child(2){stroke-dashoffset:0;transition-delay:1.1s}.s2.on .checks path:nth-child(3){stroke-dashoffset:0;transition-delay:1.6s}
.s2.on .glass{animation:scan 2.4s ease-in-out infinite}@keyframes scan{0%,100%{transform:translate(-60px,-50px)}50%{transform:translate(0,50px)}}
.s3 .stamp{transform-origin:200px 273px;transform:scale(2.2) rotate(-25deg);opacity:0;transition:transform .45s cubic-bezier(.5,1.8,.5,1) .4s,opacity .2s .4s}.s3.on .stamp{transform:rotate(-8deg);opacity:1}
.s4 .bars rect{transform-origin:0 320px;transform:scaleY(0);transition:transform .7s cubic-bezier(.2,.7,.2,1)}.s4.on .bars rect{transform:scaleY(1)}
.s4.on .bars rect:nth-child(2){transition-delay:.15s}.s4.on .bars rect:nth-child(3){transition-delay:.3s}.s4.on .bars rect:nth-child(4){transition-delay:.45s}
.s4 .trend{stroke-dasharray:320;stroke-dashoffset:320;transition:stroke-dashoffset 1s ease .7s}.s4.on .trend{stroke-dashoffset:0}
@media(max-width:900px){.story{height:380vh}.story-grid{grid-template-columns:1fr;gap:10px}.story-visual{max-width:270px;order:-1}.story-h{font-size:26px;margin-bottom:12px}.step{padding:8px 0 8px 14px}.step h3{font-size:17px}.step p{font-size:14px}.step:not(.on){display:none}.big-num{font-size:90px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}.story{height:auto}.story-sticky{position:static;height:auto;padding:60px 0}.scene{position:relative;display:none}.scene.s4{display:block;opacity:1;transform:none}.step{opacity:1}.step p{max-height:none}.step:not(.on){display:flex}}

:root{--p:#0b3d6e;--a:#f2a900;--d:#0a2540;--t:#2b3440;--l:#f4f7fb;--b:#e1e7ef}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}.menu{margin-left:auto;order:2}.logo{order:1}.cpick{position:relative;margin-left:18px;order:3}.burger{order:4}
.cpick-btn{display:flex;align-items:center;gap:8px;background:#fff;border:1.5px solid var(--b);border-radius:30px;padding:8px 12px;font:inherit;font-weight:700;font-size:14px;color:var(--d);cursor:pointer;transition:.2s}
.cpick-btn:hover,.cpick.on .cpick-btn{border-color:var(--p);box-shadow:0 4px 14px rgba(11,61,110,.12)}.cpick.on .chev{transform:rotate(180deg)}.cpick .chev{transition:transform .25s;font-size:11px}
.cpick-pop{position:absolute;right:0;top:calc(100% + 10px);width:250px;background:#fff;border-radius:12px;box-shadow:0 18px 40px rgba(10,37,64,.2);border-top:3px solid var(--a);padding:10px;opacity:0;visibility:hidden;transform:translateY(8px);transition:.2s;z-index:120}
.cpick.on .cpick-pop{opacity:1;visibility:visible;transform:none}.cpick-pop p{font-size:11px;font-weight:800;letter-spacing:2px;color:#6b7686;padding:4px 10px 8px;text-transform:uppercase}
.cpick-pop ul{list-style:none}.cpick-pop a{display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:8px;font-size:14.5px;font-weight:600;color:var(--t)}.cpick-pop a:hover{background:var(--l)}
.cpick-pop a.on{background:#eef4fb;color:var(--p)}.cpick-pop a.on:after{content:"✓";margin-left:auto;color:#0f9d58;font-weight:900}
@media(max-width:900px){.logo{gap:8px;font-size:19px}.logo small{font-size:9.5px!important;letter-spacing:.5px!important;white-space:nowrap}.logo img{height:44px!important}.cpick{margin-left:auto;margin-right:6px}.cpick-btn{padding:7px 10px;gap:6px}.cpick-name{display:none}.cpick-pop{position:fixed;left:16px;right:16px;top:var(--ph,90px);width:auto}}
.cl{display:inline-flex;align-items:center;gap:8px}.flag{width:22px;height:15px;object-fit:cover;border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.08);vertical-align:-2px}
.ddm.ddc{width:280px;grid-template-columns:1fr}.ddc a{display:flex!important;align-items:center;gap:10px}.ddc .flag{width:24px;height:16px}
.globe{background:linear-gradient(135deg,#f4f7fb,#e9f1fb)}.globe-top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:26px}
.country-select{padding:14px 16px;border:2px solid var(--p);border-radius:10px;font:inherit;font-weight:700;color:var(--d);background:#fff;min-width:280px;cursor:pointer}
.cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:16px}
.ccard{background:#fff;border:1px solid var(--b);border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:10px;transition:.25s;color:var(--t)}
.ccard:hover{transform:translateY(-4px);box-shadow:0 14px 30px rgba(11,61,110,.14);border-color:var(--a)}.ccard img{width:48px;height:32px;object-fit:cover;border-radius:4px;box-shadow:0 0 0 1px rgba(0,0,0,.08)}
.ccard b{font-size:18px;color:var(--d)}.ccard span{font-size:13.5px;color:#5b6574;line-height:1.5}.ccard em{font-style:normal;font-size:13px;font-weight:700;color:var(--p);margin-top:auto}
.intl-note{background:#fff8e6;border-left:4px solid var(--a);padding:14px 18px;border-radius:8px;font-size:13.5px;color:#5b4a1a;margin-top:24px}
.ticks{list-style:none;margin:12px 0!important}.ticks li{padding:7px 0 7px 30px;position:relative}.ticks li:before{content:"✓";position:absolute;left:0;top:6px;width:20px;height:20px;border-radius:50%;background:#0f9d58;color:#fff;font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center}
.hero-flag{display:inline-flex;align-items:center;gap:10px;background:rgba(255,255,255,.12);padding:6px 14px 6px 8px;border-radius:30px;font-size:14px;font-weight:700;margin-bottom:14px}.hero-flag img{width:30px;height:20px;border-radius:3px;object-fit:cover}
.why4{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}.why4 div{background:#fff;border:1px solid var(--b);border-radius:12px;padding:18px}.why4 b{display:block;color:var(--p);margin-bottom:6px}
@media(min-width:901px) and (max-width:1120px){.menu{gap:14px}.menu a{font-size:14.5px}}
@media(max-width:900px){.ddc a:before{display:none}.ddc a{padding-left:22px!important}.country-select{min-width:0;width:100%}}
.svc-fig{float:right;width:300px;margin:4px 0 16px 24px;border-radius:12px;overflow:hidden;box-shadow:0 10px 26px rgba(10,37,64,.18);background:var(--d)}.svc-fig img{display:block;width:100%;height:auto;aspect-ratio:235/132;object-fit:cover}.svc-fig figcaption{color:#fff;font-size:13px;font-weight:600;padding:8px 12px;border-top:3px solid var(--a)}.content h2{clear:none}.content>div>h2:nth-of-type(2){clear:both}@media(max-width:600px){.svc-fig{float:none;width:100%;margin:12px 0 16px}}.ddm .all a{color:var(--p);font-weight:700;border-top:1px solid var(--b)}
body{font-family:'Segoe UI',Roboto,Arial,sans-serif;color:var(--t);line-height:1.65;background:#fff;padding-bottom:0}
a{color:var(--p);text-decoration:none}img{max-width:100%}
.wrap{max-width:1180px;margin:auto;padding:0 16px}
.top{background:var(--d);color:#fff;font-size:14px}.top .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;padding:6px 16px}.top a{color:#fff}
header{background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.06);position:sticky;top:0;z-index:50}
.nav{display:flex;align-items:center;justify-content:space-between;padding:12px 16px}
.logo{font-weight:800;font-size:22px;color:var(--p);display:flex;align-items:center;gap:10px;line-height:1.15}.logo small{display:block;font-size:12px;font-weight:600;color:#6b7686;letter-spacing:1px}
.menu{display:flex;gap:22px;list-style:none;align-items:center}.menu a{color:var(--t);font-weight:600}
.btn{display:inline-block;background:var(--a);color:#111 !important;padding:11px 22px;border-radius:6px;font-weight:700;border:0;cursor:pointer}
.btn.o{background:transparent;border:2px solid #fff;color:#fff !important}
.burger{display:none;background:none;border:0;font-size:28px;cursor:pointer}
.hero{background:linear-gradient(120deg,var(--d),var(--p));color:#fff;padding:60px 0}
.hero .wrap{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:center}
.hero h1{font-size:38px;line-height:1.2;margin-bottom:14px}.hero p{opacity:.92;margin-bottom:22px}
.form{background:#fff;color:var(--t);padding:24px;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.2)}
.form h3{margin-bottom:12px;color:var(--p)}
.form input,.form select,.form textarea{width:100%;padding:11px;margin-bottom:10px;border:1px solid var(--b);border-radius:6px;font:inherit}
.form .btn{width:100%}
section{padding:56px 0}.alt{background:var(--l)}
h2{font-size:30px;color:var(--d);margin-bottom:10px}.sub{color:#5b6574;margin-bottom:30px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px}
.card{background:#fff;border:1px solid var(--b);border-radius:10px;padding:22px;transition:.2s}.card:hover{box-shadow:0 8px 24px rgba(11,61,110,.12);transform:translateY(-2px)}
.card h3{color:var(--p);margin-bottom:8px;font-size:19px}
.chips{display:flex;flex-wrap:wrap;gap:10px}.chips a{background:#fff;border:1px solid var(--b);padding:8px 14px;border-radius:30px;font-size:14px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center}.stats b{display:block;font-size:32px;color:var(--a)}
.rev{background:#fff;border-radius:10px;padding:22px;border:1px solid var(--b)}.stars{color:#f5b301;font-size:18px}
.rev p{margin:8px 0;font-style:italic}.rev small{color:#6b7686}
.content{display:grid;grid-template-columns:2fr 1fr;gap:36px}.content h2{font-size:24px;margin-top:22px}
.content ul{margin:10px 0 10px 20px}.side{position:sticky;top:90px;align-self:start}
.crumb{font-size:14px;margin-bottom:10px;opacity:.85}.crumb a{color:#fff}
details{background:#fff;border:1px solid var(--b);border-radius:8px;padding:14px;margin-bottom:10px}summary{font-weight:700;cursor:pointer}
.cta{background:var(--a);text-align:center;padding:40px 0}.cta h2{color:#111}
.map iframe{width:100%;height:360px;border:0;border-radius:10px}
footer{background:var(--d);color:#cfd8e3;padding:46px 0 20px;font-size:14px}footer a{color:#cfd8e3}
footer .grid{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}footer h4{color:#fff;margin-bottom:10px}footer li{list-style:none;margin-bottom:6px}
.copy{border-top:1px solid #23415f;margin-top:26px;padding-top:16px;text-align:center}
.mbar{display:none;position:fixed;bottom:0;left:0;right:0;z-index:99;box-shadow:0 -2px 10px rgba(0,0,0,.2)}
.mbar a{flex:1;text-align:center;padding:14px;font-weight:700;color:#fff;font-size:16px}
.mbar .c{background:#0f9d58}.mbar .w{background:#25d366}
.dd{position:relative}.ddm{display:none;position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;list-style:none;width:600px;padding:14px;border-radius:12px;box-shadow:0 18px 40px rgba(10,37,64,.18);border-top:3px solid var(--a);z-index:60;grid-template-columns:1fr 1fr;gap:2px 10px}.dd{padding:10px 0;margin:-10px 0}.ddm .all{grid-column:1/-1}
.dd:hover .ddm,.dd:focus-within .ddm{display:grid;animation:ddin .2s ease}@keyframes ddin{from{opacity:0;margin-top:8px}to{opacity:1;margin-top:0}}.ddm a{display:block;padding:9px 12px;font-weight:500;font-size:14.5px;border-radius:8px}.ddm a:hover{background:var(--l);color:var(--p)}.mbar .q{background:var(--p)}
.wa{position:fixed;right:18px;bottom:22px;animation:pulse 2s infinite;background:#25d366;color:#fff;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;z-index:98;box-shadow:0 4px 12px rgba(0,0,0,.25)}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:200;align-items:center;justify-content:center;padding:16px}.modal.on{display:flex}
.modal .form{max-width:420px;width:100%;position:relative}.x{position:absolute;right:12px;top:6px;font-size:26px;cursor:pointer;background:none;border:0}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(37,211,102,.6)}70%{box-shadow:0 0 0 14px rgba(37,211,102,0)}100%{box-shadow:0 0 0 0 rgba(37,211,102,0)}}
@media(max-width:900px){
 .menu{position:fixed;top:var(--hh,78px);left:0;right:0;bottom:0;z-index:90;background:#fff;display:flex;flex-direction:column;align-items:stretch;gap:0;padding:6px 0 calc(110px + env(safe-area-inset-bottom));overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;transform:translateX(100%);visibility:hidden;transition:transform .38s cubic-bezier(.2,.7,.2,1),visibility 0s .38s;box-shadow:none}
 .menu.on{transform:none;visibility:visible;transition:transform .38s cubic-bezier(.2,.7,.2,1)}
 .menu>li{border-bottom:1px solid #e6ecf3}.menu>li>a:not(.btn){display:flex;justify-content:space-between;align-items:center;padding:16px 22px;font-size:17px;font-weight:700;color:var(--d)}
 .menu>li>a:not(.btn):active{background:var(--l)}
 .chev{display:inline-block;transition:transform .3s ease;font-size:14px;color:var(--p)}.dd.on .chev{transform:rotate(180deg)}
 .dd{padding:0;margin:0}.dd .ddm,.dd:hover .ddm,.dd:focus-within .ddm{display:block;position:static;transform:none;width:auto;border-top:0;animation:none;box-shadow:none;border-radius:0;min-width:0;max-height:0;overflow:hidden;padding:0;background:var(--l);transition:max-height .45s cubic-bezier(.2,.7,.2,1)}
 .dd.on .ddm{max-height:1500px}
 .ddm a{position:relative;border-radius:0;padding:13px 22px 13px 42px;font-size:15px;font-weight:500;border-top:1px solid #e1e8f0;color:var(--t)}
 .ddm a:before{content:"";position:absolute;left:24px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:var(--a)}
 .ddm .all a{color:var(--p);font-weight:700}.ddm .all a:before{display:none}
 .menu>li:last-child{border:0;padding:18px 22px}.menu>li:last-child .btn{display:block;text-align:center;padding:14px;font-size:17px}
 body.menu-open{overflow:hidden}body.menu-open .wa{display:none}
 .burger{width:44px;height:44px;border-radius:10px;color:var(--p);line-height:1;transition:background .2s}.burger:active{background:var(--l)}
 .mbar a{padding:13px 4px;font-size:15px}.burger{display:flex;align-items:center;justify-content:center}
 .hero .wrap,.content{grid-template-columns:1fr}.hero h1{font-size:28px}
 .stats{grid-template-columns:repeat(2,1fr)}.mbar{display:flex}body{padding-bottom:52px}.wa{bottom:70px}.side{position:static}
}
"""
[shutil.copy(f,f"{OUT}/assets/{f}") for f in ["ca-logo-200.png","ca-logo-square-512.png"]]; shutil.copytree("fav",f"{OUT}/assets/fav",dirs_exist_ok=True); shutil.copy("fav/favicon.ico",f"{OUT}/favicon.ico"); shutil.copytree("flags",f"{OUT}/assets/flags",dirs_exist_ok=True); shutil.copy("gst-photo.jpg",f"{OUT}/assets/gst-photo.jpg"); shutil.copy("img1.svg",f"{OUT}/assets/ca-desk.svg"); shutil.copy("img2.svg",f"{OUT}/assets/cloud-accounting.svg")
open(f"{OUT}/assets/style.css","w").write(CSS.strip())

JS = """(function(){var p=document.querySelector('.cpick');if(!p)return;var b=p.querySelector('.cpick-btn');
function set(o){p.classList.toggle('on',o);b.setAttribute('aria-expanded',o);if(o)document.documentElement.style.setProperty('--ph',(b.getBoundingClientRect().bottom+10)+'px')}
b.addEventListener('click',function(e){e.stopPropagation();var m=document.querySelector('.menu');if(m&&m.classList.contains('on'))document.querySelector('.burger').click();set(!p.classList.contains('on'))});
document.addEventListener('click',function(e){if(!p.contains(e.target))set(false)});addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});})();

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

(function(){var bg=document.querySelector('.burger'),mn=document.querySelector('.menu'),hd=document.querySelector('header'),dds=[].slice.call(document.querySelectorAll('.menu .dd'));
function setH(){document.documentElement.style.setProperty('--hh',Math.max(0,hd.getBoundingClientRect().bottom)+'px')}
function setOpen(o){setH();mn.classList.toggle('on',o);document.body.classList.toggle('menu-open',o);bg.textContent=o?'✕':'☰';bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu');if(!o)dds.forEach(function(d){d.classList.remove('on')})}
bg.addEventListener('click',function(){setOpen(!mn.classList.contains('on'))});
dds.forEach(function(dd){var a=dd.querySelector('a');a.addEventListener('click',function(e){if(innerWidth<=900){e.preventDefault();var o=!dd.classList.contains('on');dds.forEach(function(x){x.classList.remove('on')});dd.classList.toggle('on',o);a.setAttribute('aria-expanded',o);if(o)setTimeout(function(){dd.scrollIntoView({behavior:'smooth',block:'start'})},120)}})});
mn.querySelectorAll('.ddm a, .menu>li:not(.dd)>a').forEach(function(a){a.addEventListener('click',function(){if(mn.classList.contains('on'))setOpen(false)})});
addEventListener('keydown',function(e){if(e.key==='Escape'&&mn.classList.contains('on'))setOpen(false)});
addEventListener('resize',function(){if(innerWidth>900&&mn.classList.contains('on'))setOpen(false)});
var cs=document.querySelectorAll('.country-select');cs.forEach(function(c){c.addEventListener('change',function(){if(c.value)location.href=c.value})});})();

const m=document.getElementById('qm');document.querySelectorAll('.openq').forEach(b=>b.onclick=e=>{e.preventDefault();m.classList.add('on')});
m.querySelector('.x').onclick=()=>m.classList.remove('on');m.onclick=e=>{if(e.target===m)m.classList.remove('on')};
document.querySelectorAll('form.lead').forEach(f=>f.onsubmit=e=>{e.preventDefault();const d=new FormData(f);
const t=`New enquiry from website%0AName: ${d.get('name')}%0APhone: ${d.get('phone')}%0AService: ${d.get('service')||''}%0AMessage: ${d.get('msg')||''}%0APage: ${location.pathname}`;
window.open('https://wa.me/WAN?text='+t,'_blank');location.href=f.dataset.ty;});
""".replace("WAN", WA)
open(f"{OUT}/assets/main.js","w").write(JS.strip())

def rel(depth): return "../"*depth

def lead_form(r, title="Get a Free Consultation", sel="", names=None):
    names = names or [x[1] for x in SERVICES]
    opts = "".join(f'<option{" selected" if n==sel else ""}>{n}</option>' for n in names)
    return f'''<form class="form lead" data-ty="{r}thank-you.html"><h3>{title}</h3>
<input name="name" placeholder="Your Name" required><input name="phone" type="tel" placeholder="Mobile Number" pattern="[0-9+ -]{{10,15}}" required>
<select name="service"><option value="">Select Service</option>{opts}</select>
<textarea name="msg" rows="3" placeholder="Your requirement"></textarea><button class="btn" type="submit">Get Call Back</button>
<p style="font-size:12px;margin-top:8px;color:#6b7686">Or call <a href="tel:{TEL}">{PHONE}</a></p></form>'''

def reviews_html():
    cards = "".join(f'<div class="rev"><div class="stars">★★★★★</div><p>“{t}”</p><b>{n}</b><br><small>{l}</small></div>' for n,l,t in REVIEWS)
    return f'<section class="alt"><div class="wrap"><h2>What Our Clients Say</h2><p class="sub">Rated 4.9/5 by businesses and families across North-West Delhi</p><div class="grid">{cards}</div></div></section>'

def map_html():
    return f'<section><div class="wrap"><h2>Visit Our Office in Rohini</h2><p class="sub">{ADDR} · <a href="{MAPLINK}" target="_blank" rel="noopener">Get Directions</a></p><div class="map"><iframe src="{MAP}" loading="lazy" title="{FIRM} office location map" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>'

LB = {"@context":"https://schema.org","@type":"AccountingService","@id":SITE+"/#firm","name":"Gugnani & Co, Chartered Accountants",
 "url":SITE,"telephone":PHONE,"email":EMAIL,"image":SITE+"/assets/ca-logo-square-512.png","logo":SITE+"/assets/ca-logo-square-512.png","priceRange":"₹₹",
 "address":{"@type":"PostalAddress","streetAddress":"130 Star Apartment, Sector 9","addressLocality":"Rohini","addressRegion":"Delhi","postalCode":"110085","addressCountry":"IN"},
 "geo":{"@type":"GeoCoordinates","latitude":28.7186,"longitude":77.1287},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"19:00"}],
 "areaServed":[a[1] for a in AREAS]+["Delhi NCR"],
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":str(len(REVIEWS))},
 "review":[{"@type":"Review","author":{"@type":"Person","name":n},"reviewRating":{"@type":"Rating","ratingValue":"5"},"reviewBody":t} for n,l,t in REVIEWS]}

def page(path, title, desc, body, depth, extra_schema=None, crumbs=None, cc=None):
    r = rel(depth); url = SITE + "/" + path.replace("index.html","")
    schemas = [LB] + (extra_schema or [])
    if crumbs:
        schemas.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+"/"+u} for i,(n,u) in enumerate(crumbs)]})
    sj = "".join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in schemas)
    cur = next((c for c in COUNTRIES if c["cc"]==cc), None)
    if cur:
        cb = f'{r}global/{cur["cc"]}/'
        dd_links = "".join(f'<li><a href="{cb}{x[0]}.html">{x[1]}</a></li>' for x in cur["services"])
        svc_all = f'{cb}index.html'; svc_links = dd_links
        area_links = "".join(f'<li><a href="{cb}index.html">{a_}</a></li>' for a_ in cur["areas"])
        areas_all = f'{cb}index.html'; areas_title = f'Areas We Serve – {cur["name"]}'
        foot_blurb = f'Accounting, bookkeeping, incorporation and tax compliance support for businesses in {cur["full"]}, delivered by our CA team in India.'
    else:
        dd_links = "".join(f'<li><a href="{r}services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES)
        svc_all = f'{r}services/index.html'
        svc_links = "".join(f'<li><a href="{r}services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES[:8])
        area_links = "".join(f'<li><a href="{r}areas/ca-in-{a[0]}.html">CA in {a[1]}</a></li>' for a in AREAS[:8])
        areas_all = f'{r}areas/index.html'; areas_title = 'Areas We Serve'
        foot_blurb = 'Chartered Accountants providing GST, income tax, audit, company registration and compliance services in Rohini and across Delhi NCR.'
    flag_now = cur["flag"] if cur else "in"; name_now = cur["name"] if cur else "India"
    picks = f'<li><a class="{"on" if not cur else ""}" href="{r}index.html"><img class="flag" src="{r}assets/flags/in.svg" alt="" width="24" height="16">India</a></li>' + "".join(f'<li><a class="{"on" if cur and c["cc"]==cur["cc"] else ""}" href="{r}global/{c["cc"]}/index.html"><img class="flag" src="{r}assets/flags/{c["flag"]}.svg" alt="" width="24" height="16">{c["full"]}</a></li>' for c in COUNTRIES)
    cpick = f'<div class="cpick"><button class="cpick-btn" type="button" aria-haspopup="true" aria-expanded="false" aria-label="Choose country: {name_now}"><img class="flag" src="{r}assets/flags/{flag_now}.svg" alt="" width="22" height="15"><span class="cpick-name">{name_now}</span><span class="chev">▾</span></button><div class="cpick-pop"><p>Select your country</p><ul>{picks}</ul></div></div>'
    html = f'''<!DOCTYPE html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta name="robots" content="index,follow"><meta name="geo.region" content="IN-DL"><meta name="geo.placename" content="Rohini, Delhi"><meta name="geo.position" content="28.7186;77.1287"><meta name="ICBM" content="28.7186, 77.1287">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Gugnani &amp; Co"><meta property="og:locale" content="en_IN">
<link rel="icon" href="{r}favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="{r}assets/fav/favicon-32.png"><link rel="icon" type="image/png" sizes="16x16" href="{r}assets/fav/favicon-16.png"><link rel="apple-touch-icon" sizes="180x180" href="{r}assets/fav/apple-touch-icon.png"><link rel="manifest" href="{r}assets/fav/site.webmanifest"><meta name="theme-color" content="#0b3d6e"><meta property="og:image" content="{SITE}/assets/ca-logo-square-512.png"><link rel="stylesheet" href="{r}assets/style.css?v=15">{sj}{GTM_HEAD}</head><body>{GTM_BODY}
<div class="top"><div class="wrap"><span>📍 Sector 9, Rohini, Delhi 110085</span><span>📞 <a href="tel:{TEL}">{PHONE}</a> · ✉ <a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
<header><div class="nav wrap"><a class="logo" href="{r}index.html"><img src="{r}assets/ca-logo-200.png" alt="CA India logo – Gugnani &amp; Co Chartered Accountants" width="70" height="54" style="height:54px;width:auto"><span>Gugnani &amp; Co<small>CHARTERED ACCOUNTANTS</small></span></a>
{cpick}<button class="burger" aria-label="Open menu" aria-expanded="false">☰</button><ul class="menu"><li><a href="{r}index.html">Home</a></li><li><a href="{r}about.html">About</a></li><li class="dd"><a href="{svc_all}" aria-expanded="false">Services <span class="chev">▾</span></a><ul class="ddm">{dd_links}<li class="all"><a href="{svc_all}">View all services →</a></li></ul></li><li><a href="{r}areas/index.html">Areas</a></li><li><a href="{r}blog/index.html">Blog</a></li><li><a href="{r}contact.html">Contact</a></li><li><a class="btn" href="tel:{TEL}">Call Now</a></li></ul></div></header>
{body}
{reviews_html()}
{map_html()}
<section class="cta"><div class="wrap"><h2>Talk to a Chartered Accountant Today</h2><p style="margin-bottom:16px">Free first consultation · Fixed transparent fees · Office closed on Sundays</p><a class="btn" style="background:#0a2540;color:#fff!important" href="tel:{TEL}">📞 Call {PHONE}</a></div></section>
<footer><div class="wrap"><div class="grid">
<div><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px"><img src="{r}assets/ca-logo-200.png" alt="CA India" width="62" height="48" style="height:48px;width:auto;background:#fff;border-radius:8px;padding:4px"><h4 style="margin:0">Gugnani &amp; Co</h4></div><p>{foot_blurb}</p><p style="margin-top:10px">{ADDR}<br><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Mon–Sat: 10:00 AM – 7:00 PM</p></div>
<div><h4>Services</h4><ul>{svc_links}<li><a href="{svc_all}">All services →</a></li></ul></div>
<div><h4>{areas_title}</h4><ul>{area_links}<li><a href="{areas_all}">All areas →</a></li></ul></div>
<div><h4>Quick Links</h4><ul><li><a href="{r}about.html">About Us</a></li><li><a href="{r}blog/index.html">Blog</a></li><li><a href="{r}faq.html">FAQs</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}privacy-policy.html">Privacy Policy</a></li><li><a href="{r}disclaimer.html">Disclaimer</a></li><li><a href="{r}sitemap.html">Sitemap</a></li></ul></div>
</div><div class="copy">© {datetime.date.today().year} Gugnani &amp; Co, Chartered Accountants. All rights reserved.</div></div></footer>
<div class="mbar"><a class="c" href="tel:{TEL}">📞 Call Now</a><a class="q openq" href="#">✉ Get Query</a></div>
<a class="wa" href="https://wa.me/{WA}?text=Hi%20Gugnani%20%26%20Co%2C%20I%20need%20help%20with" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.2.6 4.4 1.7 6.3L3 29l7.3-1.9c1.8 1 3.8 1.5 5.8 1.5 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.1c-1.9 0-3.7-.5-5.3-1.4l-.4-.2-4.3 1.1 1.2-4.2-.3-.4c-1-1.6-1.5-3.5-1.5-5.4C5.4 9.8 10.2 5 16 5s10.6 4.8 10.6 10.6S21.8 26.1 16 26.1zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4s-1.2 1.1-1.2 2.8 1.2 3.2 1.4 3.5 2.4 3.7 5.8 5.2c2.2.9 3 1 4.1.8.7-.1 1.9-.8 2.2-1.5s.3-1.4.2-1.5-.3-.2-.6-.3z"/></svg></a>
<div class="modal" id="qm">{lead_form(r,"Send Your Query").replace('<h3>','<button class="x" type="button" aria-label="Close">×</button><h3>',1)}</div>
<script src="{r}assets/main.js?v=15"></script></body></html>'''
    os.makedirs(os.path.dirname(f"{OUT}/{path}") or OUT, exist_ok=True)
    open(f"{OUT}/{path}","w",encoding="utf-8").write(html)
    PAGES.append(path)


import html as _h, re
def _e(t): return _h.escape(t)
def sc_docs(l=""):
    return """<svg viewBox="0 0 400 400"><rect x="125" y="70" width="150" height="260" rx="24" fill="#0a2540"/><rect x="137" y="92" width="126" height="216" rx="10" fill="#fff"/><rect x="180" y="78" width="40" height="6" rx="3" fill="#3b5b7d"/><g class="chat"><rect x="150" y="112" width="96" height="26" rx="10" fill="#dcf8c6"/><rect x="150" y="146" width="80" height="26" rx="10" fill="#dcf8c6"/><rect x="150" y="180" width="96" height="40" rx="10" fill="#dcf8c6"/></g><g class="fly f1"><rect x="20" y="120" width="70" height="90" rx="8" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="32" y="138" width="44" height="7" rx="3" fill="#f2a900"/><rect x="32" y="156" width="46" height="6" rx="3" fill="#c9d6e6"/><rect x="32" y="170" width="36" height="6" rx="3" fill="#c9d6e6"/></g><g class="fly f2"><rect x="300" y="200" width="70" height="90" rx="8" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="312" y="218" width="44" height="7" rx="3" fill="#0b3d6e"/><rect x="312" y="236" width="46" height="6" rx="3" fill="#c9d6e6"/><rect x="312" y="250" width="36" height="6" rx="3" fill="#c9d6e6"/></g><circle cx="226" cy="268" r="20" fill="#25d366"/><path d="M216 268l7 7 13-14" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" class="tick"/></svg>""","s1"
def sc_review(l=""):
    return """<svg viewBox="0 0 400 400"><rect x="80" y="70" width="240" height="270" rx="16" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="104" y="96" width="120" height="14" rx="5" fill="#0b3d6e"/><g class="rows"><rect x="104" y="132" width="192" height="10" rx="4"/><rect x="104" y="160" width="170" height="10" rx="4"/><rect x="104" y="188" width="192" height="10" rx="4"/><rect x="104" y="216" width="150" height="10" rx="4"/><rect x="104" y="244" width="182" height="10" rx="4"/><rect x="104" y="272" width="120" height="10" rx="4"/></g><g class="checks"><path d="M282 130l6 6 10-11"/><path d="M282 186l6 6 10-11"/><path d="M282 242l6 6 10-11"/></g><g class="glass"><circle cx="250" cy="200" r="52" fill="rgba(242,169,0,.18)" stroke="#f2a900" stroke-width="12"/><rect x="284" y="236" width="18" height="70" rx="9" fill="#f2a900" transform="rotate(-45 293 271)"/></g></svg>""","s2"
def sc_form(l="FORM|FILED ✓"):
    t,st=(l.split("|")+["FILED ✓"])[:2]; fs=30 if len(t)<12 else 22; ss=38 if len(st)<9 else 26
    return f"""<svg viewBox="0 0 400 400"><rect x="90" y="60" width="220" height="280" rx="16" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><text x="200" y="112" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#0b3d6e">{_e(t)}</text><g fill="#e1e7ef"><rect x="118" y="138" width="164" height="10" rx="4"/><rect x="118" y="162" width="140" height="10" rx="4"/><rect x="118" y="186" width="164" height="10" rx="4"/><rect x="118" y="210" width="110" height="10" rx="4"/></g><g class="stamp"><rect x="112" y="238" width="176" height="70" rx="12" fill="none" stroke="#0f9d58" stroke-width="7"/><text x="200" y="286" text-anchor="middle" font-size="{ss}" font-weight="900" fill="#0f9d58" letter-spacing="2">{_e(st)}</text></g></svg>""","s3"
def sc_growth(l=""):
    return """<svg viewBox="0 0 400 400"><line x1="70" y1="320" x2="340" y2="320" stroke="#c9d6e6" stroke-width="4"/><g class="bars"><rect x="90" y="250" width="40" height="70" rx="6" fill="#3b6fa5"/><rect x="150" y="210" width="40" height="110" rx="6" fill="#3b6fa5"/><rect x="210" y="160" width="40" height="160" rx="6" fill="#f2a900"/><rect x="270" y="100" width="40" height="220" rx="6" fill="#0f9d58"/></g><path class="trend" d="M100 230 L170 190 L230 140 L300 80" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path class="trend" d="M276 78 L302 78 L302 104" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>""","s4"
def sc_cert(l="CERTIFICATE"):
    fs=34 if len(l)<10 else (26 if len(l)<15 else 20)
    return f"""<svg viewBox="0 0 400 400"><defs><clipPath id="cc"><rect x="60" y="90" width="280" height="210" rx="10"/></clipPath></defs><g class="card"><rect x="60" y="90" width="280" height="210" rx="10" fill="#fff"/><rect x="72" y="102" width="256" height="186" rx="6" fill="none" stroke="#f2a900" stroke-width="4"/><text x="200" y="140" text-anchor="middle" font-size="14" font-weight="700" fill="#5b6574" letter-spacing="4">CERTIFICATE</text><text x="200" y="185" text-anchor="middle" font-size="{fs}" font-weight="800" fill="#0b3d6e">{_e(l)}</text><g fill="#e1e7ef"><rect x="110" y="208" width="180" height="8" rx="4"/><rect x="130" y="226" width="140" height="8" rx="4"/></g><rect x="100" y="262" width="80" height="4" rx="2" fill="#0b3d6e"/><g clip-path="url(#cc)"><rect class="shine" x="160" y="60" width="40" height="280" fill="rgba(255,255,255,.7)" transform="skewX(-20)"/></g></g><g class="seal"><circle cx="290" cy="270" r="38" fill="#f2a900"/><circle cx="290" cy="270" r="28" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/><path d="M276 270l10 10 18-20" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M270 300l-8 40 18-10 10 16 8-40z" fill="#d68f00"/></g></svg>""","scert"
def sc_portal(l="portal.gov.in"):
    return f"""<svg viewBox="0 0 400 400"><rect x="40" y="70" width="320" height="250" rx="14" fill="#fff"/><rect x="40" y="70" width="320" height="40" rx="14" fill="#dfe7f1"/><rect x="40" y="96" width="320" height="14" fill="#dfe7f1"/><circle cx="64" cy="90" r="6" fill="#ff5f57"/><circle cx="84" cy="90" r="6" fill="#febc2e"/><circle cx="104" cy="90" r="6" fill="#28c840"/><rect x="124" y="80" width="216" height="20" rx="10" fill="#fff"/><text x="232" y="95" text-anchor="middle" font-size="13" fill="#0b3d6e" font-weight="700">🔒 {_e(l)}</text><rect x="70" y="135" width="140" height="12" rx="5" fill="#0b3d6e"/><g fill="#e1e7ef"><rect x="70" y="160" width="260" height="22" rx="6"/><rect x="70" y="192" width="260" height="22" rx="6"/></g><rect x="110" y="236" width="180" height="14" rx="7" fill="#e1e7ef"/><rect class="fill" x="110" y="236" width="180" height="14" rx="7" fill="#0f9d58"/><g class="ok"><circle cx="200" cy="290" r="22" fill="#0f9d58"/><path d="M189 290l8 8 14-15" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g><path class="cursor" d="M300 300l0 34 9-9 7 15 8-4-7-15 13 0z" fill="#0a2540" stroke="#fff" stroke-width="2"/></svg>""","sportal"
def sc_otp(l="OTP"):
    return f"""<svg viewBox="0 0 400 400"><rect x="120" y="60" width="160" height="290" rx="24" fill="#0a2540"/><rect x="132" y="84" width="136" height="242" rx="10" fill="#fff"/><text x="200" y="130" text-anchor="middle" font-size="16" font-weight="800" fill="#0b3d6e">{_e(l)}</text><g><rect x="144" y="160" width="26" height="36" rx="6" fill="#eef3f9"/><rect x="174" y="160" width="26" height="36" rx="6" fill="#eef3f9"/><rect x="204" y="160" width="26" height="36" rx="6" fill="#eef3f9"/><rect x="234" y="160" width="26" height="36" rx="6" fill="#eef3f9"/></g><text class="dg" x="157" y="186" text-anchor="middle" font-size="20" font-weight="800" fill="#0a2540">4</text><text class="dg" x="187" y="186" text-anchor="middle" font-size="20" font-weight="800" fill="#0a2540">7</text><text class="dg" x="217" y="186" text-anchor="middle" font-size="20" font-weight="800" fill="#0a2540">2</text><text class="dg" x="247" y="186" text-anchor="middle" font-size="20" font-weight="800" fill="#0a2540">9</text><rect x="150" y="226" width="100" height="30" rx="8" fill="#0b3d6e"/><text x="200" y="246" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">VERIFY</text><g class="shield"><path d="M300 70l40 14v30c0 28-18 46-40 56-22-10-40-28-40-56V84z" fill="#0f9d58"/><path d="M284 118l11 11 21-23" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g></svg>""","sotp"
def sc_cal(l="15"):
    w=60 if len(l)<4 else 110; fs=28 if len(l)<4 else 24
    skip={12} if w==60 else {11,12,13}
    cells="".join(f'<rect x="{80+(i%5)*50}" y="{170+(i//5)*42}" width="40" height="32" rx="6" fill="#eef3f9"/>' for i in range(15) if i not in skip)
    return f"""<svg viewBox="0 0 400 400"><rect x="60" y="90" width="280" height="250" rx="16" fill="#fff"/><rect x="60" y="90" width="280" height="60" rx="16" fill="#0b3d6e"/><rect x="60" y="130" width="280" height="20" fill="#0b3d6e"/><rect x="110" y="72" width="14" height="36" rx="7" fill="#f2a900"/><rect x="276" y="72" width="14" height="36" rx="7" fill="#f2a900"/><text x="200" y="130" text-anchor="middle" font-size="20" font-weight="800" fill="#fff" letter-spacing="3">DUE DATE</text>{cells}<rect x="{200-w//2}" y="250" width="{w}" height="44" rx="10" fill="#f2a900"/><text x="200" y="281" text-anchor="middle" font-size="{fs}" font-weight="900" fill="#0a2540">{_e(l)}</text><ellipse class="circ" cx="200" cy="272" rx="{w//2+16}" ry="36" fill="none" stroke="#0f9d58" stroke-width="5"/><g class="bell"><path d="M340 44c-12 0-20 9-20 21v12l-5 7h50l-5-7V65c0-12-8-21-20-21z" fill="#f2a900"/><circle cx="340" cy="90" r="5" fill="#f2a900"/></g></svg>""","scal"
def sc_money(l="TAX PAID"):
    fs=26 if len(l)<10 else 20
    return f"""<svg viewBox="0 0 400 400"><rect x="90" y="190" width="220" height="130" rx="18" fill="#0b3d6e"/><rect x="250" y="230" width="70" height="50" rx="12" fill="#11528f"/><circle cx="275" cy="255" r="8" fill="#f2a900"/><g><g class="coin"><circle cx="160" cy="170" r="30" fill="#f2a900" stroke="#d68f00" stroke-width="5"/><text x="160" y="181" text-anchor="middle" font-size="30" font-weight="900" fill="#fff">₹</text></g><g class="coin"><circle cx="205" cy="140" r="30" fill="#f2a900" stroke="#d68f00" stroke-width="5"/><text x="205" y="151" text-anchor="middle" font-size="30" font-weight="900" fill="#fff">₹</text></g><g class="coin"><circle cx="250" cy="170" r="30" fill="#f2a900" stroke="#d68f00" stroke-width="5"/><text x="250" y="181" text-anchor="middle" font-size="30" font-weight="900" fill="#fff">₹</text></g></g><g class="paid"><rect x="110" y="308" width="180" height="46" rx="23" fill="#0f9d58"/><text x="200" y="339" text-anchor="middle" font-size="{fs}" font-weight="900" fill="#fff">{_e(l)} ✓</text></g></svg>""","smoney"
def sc_rec(l="Books|Portal"):
    a,b=(l.split("|")+["Portal"])[:2]
    rows="".join(f'<rect x="60" y="{120+i*46}" width="110" height="30" rx="6" fill="#fff"/><rect x="230" y="{120+i*46}" width="110" height="30" rx="6" fill="#fff"/>' for i in range(4))
    lns="".join(f'<line class="ln" x1="172" y1="{135+i*46}" x2="228" y2="{135+i*46}" stroke="#f2a900" stroke-width="5" stroke-linecap="round"/>' for i in range(4))
    return f"""<svg viewBox="0 0 400 400"><text x="115" y="104" text-anchor="middle" font-size="18" font-weight="800" fill="#fff">{_e(a)}</text><text x="285" y="104" text-anchor="middle" font-size="18" font-weight="800" fill="#fff">{_e(b)}</text>{rows}<g fill="#c9d6e6">{"".join(f'<rect x="72" y="{132+i*46}" width="70" height="6" rx="3"/><rect x="242" y="{132+i*46}" width="70" height="6" rx="3"/>' for i in range(4))}</g>{lns}<g class="ok"><rect x="120" y="314" width="160" height="42" rx="21" fill="#0f9d58"/><text x="200" y="342" text-anchor="middle" font-size="18" font-weight="900" fill="#fff">MATCHED ✓</text></g></svg>""","srec"
SCENES={"docs":sc_docs,"review":sc_review,"form":sc_form,"growth":sc_growth,"cert":sc_cert,"portal":sc_portal,"otp":sc_otp,"cal":sc_cal,"money":sc_money,"rec":sc_rec}
def story_html(heading,steps,eyebrow="STEP-BY-STEP PROCESS",sid="process"):
    li="".join(f'<li class="step{" on" if i==0 else ""}"><b>0{i+1}</b><div><h3>{t}</h3><p>{d}</p></div></li>' for i,(t,d,k,l) in enumerate(steps))
    sc=""
    for i,(t,d,k,l) in enumerate(steps):
        svg,cls=SCENES[k](l) if l else SCENES[k]()
        sc+=f'<div class="scene {cls}{" on" if i==0 else ""}">{svg}</div>'
    return f"""<section class="story svc" id="{sid}" aria-label="{_e(re.sub('<[^>]+>','',heading))}"><div class="story-sticky"><div class="story-bg" aria-hidden="true"><span></span><span></span><span></span></div><div class="wrap story-grid"><div class="story-text"><p class="eyebrow">{eyebrow}</p><h2 class="story-h">{heading}</h2><ol class="steps">{li}</ol><div class="story-bar"><i></i></div></div><div class="story-visual" aria-hidden="true"><svg class="ring" viewBox="0 0 400 400"><circle cx="200" cy="200" r="180" class="ring-bg"/><circle cx="200" cy="200" r="180" class="ring-fg"/></svg>{sc}<div class="big-num">01</div></div></div></div></section>"""

GST_REG=[("Document check","We collect PAN, Aadhaar, photo, address proof with NOC and bank details – and verify everything before filing.","docs",""),
 ("REG-01 on GST portal","Part A and Part B of the GST REG-01 application are filed on the GST portal with the right HSN/SAC codes.","portal","gst.gov.in"),
 ("Aadhaar authentication","You verify a quick Aadhaar OTP; the ARN is generated and we track the application till approval.","otp","Aadhaar OTP"),
 ("GSTIN issued","Your GSTIN and registration certificate (REG-06) are issued – usually in 3–7 working days.","cert","GSTIN")]
GST_RET=[("Collect sales & purchase data","Sales invoices, purchase bills and credit/debit notes are collected every month.","docs",""),
 ("Reconcile with GSTR-2B","Purchases are matched with GSTR-2B so you claim only eligible input tax credit.","rec","Books|GSTR-2B"),
 ("File GSTR-1","Outward supplies are reported in GSTR-1 before the due date (11th / IFF for QRMP).","form","GSTR-1|FILED ✓"),
 ("Pay tax & file GSTR-3B","Net tax is paid through the electronic ledger and GSTR-3B is filed by the 20th.","money","GSTR-3B")]
STORIES={
"gst-registration":[("GST <em>Registration</em> Process",GST_REG),("GSTR <em>Return Filing</em> Process",GST_RET)],
"gst-return-filing":[("GSTR <em>Return Filing</em> Process",GST_RET),("GST <em>Registration</em> Process",GST_REG)],
"income-tax-return-filing":[("ITR <em>Filing</em> Process",[("Share Form 16 & AIS","Send Form 16, bank interest, capital gains and investment proofs.","docs",""),("Old vs new regime","We match AIS/26AS and compute tax under both regimes to pick the lower one.","review",""),("E-file & e-verify","Your ITR is filed on the income tax portal and e-verified with Aadhaar OTP.","portal","incometax.gov.in"),("Refund credited","We track processing under 143(1) until your refund reaches your bank.","money","REFUND")])],
"tds-return-filing":[("TDS <em>Return</em> Process",[("Deduction details","Salary, rent and contractor payments with deductee PANs are compiled.","docs",""),("Deposit TDS by 7th","TDS is deposited through challan ITNS 281 before the 7th of next month.","money","CHALLAN 281"),("File 24Q / 26Q / 27Q","Quarterly TDS statements are prepared and filed with correct challan mapping.","form","26Q / 24Q|FILED ✓"),("Form 16 / 16A issued","TDS certificates are downloaded from TRACES and shared with deductees.","cert","Form 16A")])],
"company-registration":[("Company <em>Incorporation</em> Process",[("DSC & DIN","Digital signatures are issued for all directors with video/OTP verification.","otp","DSC eKYC"),("Name approval","Two proposed names are filed in SPICe+ Part A for MCA approval.","form","SPICe+ Part A|APPROVED"),("MOA, AOA & SPICe+ filing","MOA, AOA, PAN, TAN, EPFO and ESIC are applied together on the MCA portal.","portal","mca.gov.in"),("Certificate of Incorporation","Your company is incorporated with CIN, PAN and TAN – ready to open a bank account.","cert","Incorporation")])],
"llp-registration":[("LLP <em>Registration</em> Process",[("DSC for partners","Digital signatures are obtained for both designated partners.","otp","DSC eKYC"),("Name reservation","Proposed LLP name is reserved through RUN-LLP.","form","RUN-LLP|APPROVED"),("FiLLiP filing","Incorporation form FiLLiP is filed on the MCA portal.","portal","mca.gov.in"),("LLP certificate & Form 3","LLPIN is issued and the LLP agreement is filed in Form 3 within 30 days.","cert","LLPIN")])],
"partnership-firm-registration":[("Partnership <em>Registration</em> Process",[("Discuss terms","Capital, profit ratio, salary and exit terms are finalised with all partners.","docs",""),("Deed drafting","A detailed partnership deed is drafted, printed on stamp paper and signed.","form","Partnership Deed|SIGNED"),("Registrar of Firms","The firm is registered with the Registrar of Firms, Delhi.","portal","Registrar of Firms"),("PAN & bank account","Firm PAN is obtained and the current account is opened.","cert","Firm Registered")])],
"roc-compliance":[("ROC <em>Compliance</em> Process",[("Compliance calendar","Every due date – DIR-3 KYC, AOC-4, MGT-7, DPT-3 – goes on your calendar.","cal","30 OCT"),("Minutes & registers","Board and AGM minutes and statutory registers are prepared.","review",""),("AOC-4 & MGT-7 filing","Financial statements and annual return are filed on the MCA portal.","portal","mca.gov.in"),("Fully compliant","No additional fees, no director disqualification – your company stays compliant.","cert","ROC Compliant")])],
"accounting-bookkeeping":[("Bookkeeping <em>Process</em>",[("Share bills & statements","Sales, purchase, expense bills and bank statements reach us every month.","docs",""),("Entries & reconciliation","Every entry is recorded and reconciled with your bank statement.","rec","Bank|Books"),("GST-ready books","Books are matched with GST returns so filing is quick and error-free.","review",""),("Monthly MIS report","You get profit, receivables and payables in a simple monthly report.","growth","")])],
"cloud-accounting":[("Cloud <em>Accounting</em> Process",[("Software setup","We set up Zoho Books, Tally on Cloud or QuickBooks for your business.","portal","books.zoho.in"),("Data migration","Old Tally/Excel data is migrated and verified line by line.","rec","Tally|Cloud"),("Live access on mobile","You and your team see invoices, ledgers and bank balance on any device.","docs",""),("Real-time MIS","Dashboards show sales, expenses and GST payable in real time.","growth","")])],
"tax-audit":[("Tax <em>Audit</em> Process",[("Books & records","Ledgers, fixed asset register, GST and TDS data are collected.","docs",""),("Verification","Books are verified and all 44 clauses of Form 3CD are examined.","review",""),("Form 3CA/3CB & 3CD","The audit report is signed and prepared for upload.","form","Form 3CD|SIGNED"),("Upload by 30 September","The report is uploaded before the due date to avoid penalty u/s 271B.","cal","30 SEP")])],
"statutory-audit":[("Statutory <em>Audit</em> Process",[("Audit planning","Scope, materiality and timelines are planned with management.","cal","PLAN"),("Vouching & verification","Transactions, balances and inventory are verified as per Standards on Auditing.","review",""),("Audit report","The independent auditor's report is issued and signed.","form","Audit Report|SIGNED"),("Insights for growth","Control gaps and improvement points are shared with you.","growth","")])],
"income-tax-notice":[("Notice <em>Reply</em> Process",[("Read the notice","We check the section, DIN and deadline of the notice.","form","Notice u/s 143(1)|DIN ✓"),("Match ITR with AIS","Mismatches between your ITR, AIS and 26AS are identified.","rec","ITR|AIS"),("Reply filed online","A reasoned reply with evidence is filed on the e-filing portal.","portal","incometax.gov.in"),("Matter closed","Most notices close at this stage; appeals are handled if needed.","cert","Resolved")])],
"msme-udyam-registration":[("Udyam <em>Registration</em> Process",[("Aadhaar & PAN","Proprietor/director Aadhaar, business PAN and bank details are collected.","docs",""),("Aadhaar OTP","A quick OTP verifies the applicant's Aadhaar.","otp","Aadhaar OTP"),("Udyam portal filing","Correct NIC codes, investment and turnover details are filed.","portal","udyamregistration.gov.in"),("Udyam certificate","Your Udyam certificate is issued – unlock MSME benefits.","cert","UDYAM")])],
"trademark-registration":[("Trademark <em>Registration</em> Process",[("Brand search","Your brand name and logo are searched on the IP India database.","review",""),("TM-A filing","Application is filed in the right class – you can use ™ immediately.","portal","ipindia.gov.in"),("Examination reply","Objections in the examination report are answered.","form","Exam Report|REPLIED"),("Registered ®","After publication, your trademark is registered for 10 years.","cert","Trademark ®")])],
"payroll-pf-esi":[("Payroll & <em>PF/ESI</em> Process",[("Attendance & salary data","Attendance, leaves and salary structures are collected.","docs",""),("Payroll processed","Salaries, deductions and payslips are calculated accurately.","rec","Salary|Payslips"),("PF & ESI by 15th","Contributions are deposited before the 15th of every month.","cal","15"),("ECR & returns filed","ECR on EPFO and ESIC returns are filed on time.","portal","unifiedportal-emp.epfindia.gov.in")])],
"nri-taxation":[("NRI <em>Tax</em> Process",[("Residential status","Your residential status and Indian income are reviewed.","review",""),("Lower TDS certificate","Form 13 is filed to reduce TDS on property sale.","form","Form 13|APPROVED"),("Form 15CA / 15CB","CA certificate and online form are filed for remittance.","portal","Form 15CA / 15CB"),("Money repatriated","Funds are remitted abroad smoothly after taxes are settled.","money","REMITTED")])],
"startup-advisory":[("Startup <em>Advisory</em> Process",[("Idea & structure","We help choose the right structure – LLP or Pvt Ltd – for your plan.","docs",""),("DPIIT recognition","Startup India recognition is applied for eligible startups.","cert","DPIIT"),("Project report & CMA","Bank-ready projections and CMA data are prepared.","review",""),("Funding & growth","You approach banks and investors with clean numbers.","growth","")])],
}

PAGES = []
def hero(h1, p, r, crumb="", sel="", names=None, intl=False):
    cta = f'<a class="btn" href="https://wa.me/{WA}" target="_blank" rel="noopener">💬 WhatsApp Us</a> <a class="btn o" href="mailto:{EMAIL}">✉ Email Us</a>' if intl else f'<a class="btn" href="tel:{TEL}">📞 Call {PHONE}</a> <a class="btn o openq" href="#">Get Free Quote</a>'
    return f'''<div class="hero"><div class="wrap"><div>{crumb}<h1>{h1}</h1><p>{p}</p>{cta}</div>{lead_form(r, sel=sel, names=names)}</div></div>'''

# ---------- GLOBAL helpers ----------
def country_cards(r):
    return "".join(f'<a class="ccard" href="{r}global/{c["cc"]}/index.html"><img src="{r}assets/flags/{c["flag"]}.svg" alt="{c["full"]} flag" width="48" height="32" loading="lazy"><b>{c["full"]}</b><span>{c["tag"]}</span><em>View services →</em></a>' for c in COUNTRIES)
def country_opts(r):
    return "".join(f'<option value="{r}global/{c["cc"]}/index.html">{c["full"]}</option>' for c in COUNTRIES)
GLOBAL_HOME = """<section class="globe"><div class="wrap"><div class="globe-top"><div><p class="eyebrow" style="color:var(--p)">WE ALSO SERVE CLIENTS ABROAD</p><h2>International Accounting &amp; Compliance</h2><p class="sub" style="margin:0">Choose your country to see the services we offer there.</p></div><select class="country-select" aria-label="Choose your country"><option value="">🌐 Select your country</option>"""+country_opts("")+"""</select></div><div class="cgrid">"""+country_cards("")+"""</div></div></section>
"""
# ---------- HOME ----------
svc_cards = "".join(f'<a class="card" href="services/{s}.html"><h3>{n}</h3><p>{d}</p></a>' for s,n,d,*_ in SERVICES)
area_chips = "".join(f'<a href="areas/ca-in-{a}.html">CA in {n}</a>' for a,n,*_ in AREAS)
POST_DATES = {p['slug']:p['date'] for p in json.load(open('blog_posts.json',encoding='utf-8'))}
# weekly posts live in blog_posts.json (newest first) and are shown before the fixed posts
BLOGS = [(p['slug'],p['title'],p['desc'],p['paras']) for p in json.load(open('blog_posts.json',encoding='utf-8'))] + BLOGS
blog_cards = "".join(f'<a class="card" href="blog/{s}.html"><h3>{t}</h3><p>{d}</p></a>' for s,t,d,_ in BLOGS[:3])
home = hero("Chartered Accountant in Rohini, Delhi – Gugnani &amp; Co","Trusted CA firm for GST registration &amp; returns, income tax filing, company registration, audit and accounting. Serving Rohini, Pitampura, Prashant Vihar, Rani Bagh and all of Delhi NCR.","") + f'''

<section class="story" id="how-we-work" aria-label="How we work">
 <div class="story-sticky">
  <div class="story-bg" aria-hidden="true"><span></span><span></span><span></span></div>
  <div class="wrap story-grid">
   <div class="story-text">
    <p class="eyebrow">HOW WE WORK</p>
    <h2 class="story-h">From documents to <em>done</em> &mdash; in 4 simple steps</h2>
    <ol class="steps">
     <li class="step on"><b>01</b><div><h3>Share your documents</h3><p>Send bills, bank statements and Form 16 on WhatsApp or email &mdash; or we collect them from your office.</p></div></li>
     <li class="step"><b>02</b><div><h3>We review &amp; prepare</h3><p>A qualified CA checks every entry, reconciles GST and AIS data and finds every eligible deduction.</p></div></li>
     <li class="step"><b>03</b><div><h3>Filed on time</h3><p>Your GST, ITR or TDS return is filed before the due date and the acknowledgement is shared with you.</p></div></li>
     <li class="step"><b>04</b><div><h3>You focus on growth</h3><p>Reminders, notice support and clear MIS reports keep your business compliant all year.</p></div></li>
    </ol>
    <div class="story-bar"><i></i></div>
   </div>
   <div class="story-visual" aria-hidden="true">
    <svg class="ring" viewBox="0 0 400 400"><circle cx="200" cy="200" r="180" class="ring-bg"/><circle cx="200" cy="200" r="180" class="ring-fg"/></svg>
    <div class="scene s1 on">
     <svg viewBox="0 0 400 400"><rect x="125" y="70" width="150" height="260" rx="24" fill="#0a2540"/><rect x="137" y="92" width="126" height="216" rx="10" fill="#fff"/><rect x="180" y="78" width="40" height="6" rx="3" fill="#3b5b7d"/>
      <g class="chat"><rect x="150" y="112" width="96" height="26" rx="10" fill="#dcf8c6"/><rect x="150" y="146" width="80" height="26" rx="10" fill="#dcf8c6"/><rect x="150" y="180" width="96" height="40" rx="10" fill="#dcf8c6"/></g>
      <g class="fly f1"><rect x="20" y="120" width="70" height="90" rx="8" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="32" y="138" width="44" height="7" rx="3" fill="#f2a900"/><rect x="32" y="156" width="46" height="6" rx="3" fill="#c9d6e6"/><rect x="32" y="170" width="36" height="6" rx="3" fill="#c9d6e6"/></g>
      <g class="fly f2"><rect x="300" y="200" width="70" height="90" rx="8" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="312" y="218" width="44" height="7" rx="3" fill="#0b3d6e"/><rect x="312" y="236" width="46" height="6" rx="3" fill="#c9d6e6"/><rect x="312" y="250" width="36" height="6" rx="3" fill="#c9d6e6"/></g>
      <circle cx="226" cy="268" r="20" fill="#25d366"/><path d="M216 268l7 7 13-14" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" class="tick"/></svg>
    </div>
    <div class="scene s2">
     <svg viewBox="0 0 400 400"><rect x="80" y="70" width="240" height="270" rx="16" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><rect x="104" y="96" width="120" height="14" rx="5" fill="#0b3d6e"/>
      <g class="rows"><rect x="104" y="132" width="192" height="10" rx="4"/><rect x="104" y="160" width="170" height="10" rx="4"/><rect x="104" y="188" width="192" height="10" rx="4"/><rect x="104" y="216" width="150" height="10" rx="4"/><rect x="104" y="244" width="182" height="10" rx="4"/><rect x="104" y="272" width="120" height="10" rx="4"/></g>
      <g class="checks"><path d="M282 130l6 6 10-11"/><path d="M282 186l6 6 10-11"/><path d="M282 242l6 6 10-11"/></g>
      <g class="glass"><circle cx="250" cy="200" r="52" fill="rgba(242,169,0,.18)" stroke="#f2a900" stroke-width="12"/><rect x="284" y="236" width="18" height="70" rx="9" fill="#f2a900" transform="rotate(-45 293 271)"/></g></svg>
    </div>
    <div class="scene s3">
     <svg viewBox="0 0 400 400"><rect x="90" y="60" width="220" height="280" rx="16" fill="#fff" stroke="#c9d6e6" stroke-width="3"/><text x="200" y="112" text-anchor="middle" font-family="Arial" font-size="30" font-weight="700" fill="#0b3d6e">GST / ITR</text>
      <g fill="#e1e7ef"><rect x="118" y="138" width="164" height="10" rx="4"/><rect x="118" y="162" width="140" height="10" rx="4"/><rect x="118" y="186" width="164" height="10" rx="4"/><rect x="118" y="210" width="110" height="10" rx="4"/></g>
      <g class="stamp"><rect x="118" y="238" width="164" height="70" rx="12" fill="none" stroke="#0f9d58" stroke-width="7"/><text x="200" y="286" text-anchor="middle" font-family="Arial" font-size="38" font-weight="900" fill="#0f9d58" letter-spacing="4">FILED ✓</text></g></svg>
    </div>
    <div class="scene s4">
     <svg viewBox="0 0 400 400"><line x1="70" y1="320" x2="340" y2="320" stroke="#c9d6e6" stroke-width="4"/>
      <g class="bars"><rect x="90" y="250" width="40" height="70" rx="6" fill="#3b6fa5"/><rect x="150" y="210" width="40" height="110" rx="6" fill="#3b6fa5"/><rect x="210" y="160" width="40" height="160" rx="6" fill="#f2a900"/><rect x="270" y="100" width="40" height="220" rx="6" fill="#0f9d58"/></g>
      <path class="trend" d="M100 230 L170 190 L230 140 L300 80" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path class="trend" d="M276 78 L302 78 L302 104" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    <div class="big-num">01</div>
   </div>
  </div>
 </div>
</section>

<section><div class="wrap stats"><div><b class="count" data-to="1000" data-suf="+">0</b>Returns Filed</div><div><b class="count" data-to="500" data-suf="+">0</b>Happy Clients</div><div><b class="count" data-to="{len(AREAS)}" data-suf="+">0</b>Areas Served</div><div><b class="count" data-to="4.9" data-dec="1" data-suf="★">0</b>Client Rating</div></div></section>
<section class="alt"><div class="wrap"><h2>Our CA Services</h2><p class="sub">End-to-end tax, accounting and compliance under one roof</p><div class="grid">{svc_cards}</div></div></section>
''' + GLOBAL_HOME + f'''<section><div class="wrap content"><div><h2>Why Choose Gugnani &amp; Co?</h2>
<p>Gugnani &amp; Co is a practising chartered accountant firm based in Sector 9, Rohini. We combine the personal attention of a local CA with the systems of a modern firm—cloud accounting on Zoho Books and Tally on Cloud, online document sharing, WhatsApp updates and a compliance calendar so you never miss a due date.</p>
<ul><li><b>Qualified Chartered Accountants</b> handling every file</li><li><b>Fixed, transparent pricing</b> agreed before work starts</li><li><b>Doorstep visits</b> across North and West Delhi</li><li><b>Cloud accounting</b> – see your books live on mobile, anytime</li><li><b>Fast turnaround</b> on GST registration and ITR filing</li><li><b>Notice support</b> if the department ever questions your return</li></ul>
<h2>How It Works</h2><ol style="margin-left:20px"><li>Call or WhatsApp us on {PHONE}</li><li>Share documents online or we collect them</li><li>We prepare, review and file</li><li>You receive acknowledgement and ongoing reminders</li></ol></div>
<div class="side"><img src="assets/ca-desk.svg" width="520" height="400" alt="Chartered accountant in Rohini handling GST and income tax return filing" loading="lazy" style="border-radius:14px;margin-bottom:16px"><div class="card"><h3>Office Hours</h3><p>Monday – Saturday<br>10:00 AM – 7:00 PM<br>Sunday: Closed</p><p style="margin-top:10px"><a class="btn" href="tel:{TEL}">Call Now</a></p></div></div></div></section>
<section class="alt"><div class="wrap content" style="align-items:center"><img src="assets/cloud-accounting.svg" width="520" height="400" alt="Cloud accounting dashboard on laptop and mobile by Gugnani &amp; Co" loading="lazy" style="border-radius:14px"><div><h2>Cloud Accounting – Your Books, Live on Mobile</h2><p>We maintain your accounts on Zoho Books, Tally on Cloud and QuickBooks, so you can check sales, expenses, GST payable and bank balance anytime from your phone. No couriering bills, no waiting for month-end reports.</p><ul style="margin:12px 0 18px 20px"><li>Real-time access for you and your CA</li><li>Automatic bank feeds and GST-ready invoices</li><li>Old Tally data migrated safely</li></ul><a class="btn" href="services/cloud-accounting.html">Explore Cloud Accounting</a></div></div></section>
<section><div class="wrap"><h2>Areas We Serve</h2><p class="sub">Local CA services across North &amp; West Delhi</p><div class="chips">{area_chips}</div></div></section>
<section class="alt"><div class="wrap content" style="align-items:start"><div><h2>Looking for the Best CA Services in Rohini? Here's What to Check</h2>
<p>When people search for the <b>best chartered accountant in Rohini</b> or the <b>best CA near me</b>, they usually want three things: correct filings, no notices and someone who responds quickly. Before you hire any CA firm, check:</p>
<ul class="ticks"><li>ICAI membership number and Firm Registration Number</li><li>Experience with your type of work – GST, ITR, company or audit</li><li>A written, fixed fee quote before work starts</li><li>Reminders before every due date and quick replies on phone / WhatsApp</li><li>A local office in Rohini for document handover and meetings</li><li>Support if a GST or income tax notice arrives</li></ul>
<p style="margin-top:12px"><a href="blog/how-to-choose-best-ca-rohini.html"><b>Read the full checklist →</b></a></p></div>
<div class="card"><h3>Talk to a CA in Rohini Sector 9</h3><p>Gugnani &amp; Co offers GST, income tax, audit, company registration and cloud accounting services for individuals and businesses across Rohini, Pitampura, Prashant Vihar, Rani Bagh and Delhi NCR.</p><p style="margin-top:14px"><a class="btn" href="tel:{TEL}">📞 Call {PHONE}</a></p></div></div></section>
<section><div class="wrap"><h2>Latest from Our Blog</h2><p class="sub">Tax tips and compliance updates</p><div class="grid">{blog_cards}</div></div></section>'''
page("index.html","CA in Rohini Delhi | Chartered Accountant – Gugnani & Co","Gugnani & Co – Chartered Accountant in Rohini Sector 9, Delhi. GST, ITR filing, company registration, audit & accounting. Call +91-9953788989.",home,0)

# ---------- ABOUT ----------
page("about.html","About Gugnani & Co | Chartered Accountants in Rohini","Learn about Gugnani & Co, a chartered accountant firm in Rohini, Delhi serving individuals, startups and businesses across Delhi NCR.",
 hero("About Gugnani &amp; Co","A Rohini-based chartered accountant firm built on accuracy, honesty and responsiveness.","")+f'''<section><div class="wrap content"><div>
<h2>Who We Are</h2><p>Gugnani &amp; Co, Chartered Accountants, operates from 130 Star Apartment, Sector 9, Rohini. We serve salaried individuals, professionals, traders, manufacturers, startups and NRIs with taxation, audit, accounting and corporate compliance.</p>
<h2>Our Approach</h2><p>We believe every client deserves a CA who picks up the phone. Each client gets a dedicated point of contact, clear fee quotes and proactive reminders before every due date.</p>
<h2>Our Values</h2><ul><li>Integrity in every filing</li><li>Confidentiality of client data</li><li>Timely delivery</li><li>Plain-language advice</li></ul></div>
<div class="side card"><h3>Reach Us</h3><p>{ADDR}</p><p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div></section>''',0,crumbs=[("Home",""),("About","about.html")])

# ---------- CONTACT ----------
page("contact.html","Contact Gugnani & Co | CA Office in Rohini Sector 9, Delhi","Contact Gugnani & Co Chartered Accountants at 130 Star Apartment, Sector 9, Rohini, Delhi 110085. Call +91-9953788989 or email gugnaniandco@gmail.com.",
 f'''<div class="hero"><div class="wrap"><div><h1>Contact Us</h1><p><b>Address:</b> {ADDR}</p><p><b>Phone:</b> <a style="color:#fff" href="tel:{TEL}">{PHONE}</a></p><p><b>Email:</b> <a style="color:#fff" href="mailto:{EMAIL}">{EMAIL}</a></p><p><b>Hours:</b> Mon–Sat 10 AM – 7 PM (Sunday closed)</p><a class="btn" href="https://wa.me/{WA}">WhatsApp Us</a></div>{lead_form("","Send an Enquiry")}</div></div>''',0,crumbs=[("Home",""),("Contact","contact.html")])

# ---------- SERVICES ----------
page("services/index.html","CA Services in Rohini Delhi | GST, ITR, Audit – Gugnani & Co","All chartered accountant services by Gugnani & Co in Rohini, Delhi: GST, income tax, TDS, company & LLP registration, audit, accounting and more.",
 hero("Our Chartered Accountant Services","Complete tax, audit and compliance services for individuals and businesses in Delhi NCR.","../")+f'<section><div class="wrap"><div class="grid">{svc_cards.replace("services/","")}</div></div></section>',1,crumbs=[("Home",""),("Services","services/")])

for slug,name,desc,body,docs,faqs in SERVICES:
    faqs = list(faqs) + [f"How do I find the best CA for {name.lower()} in Rohini?|Look for a chartered accountant with an ICAI membership number, regular experience in {name.lower()}, a clear fixed fee, timely reminders and support if a notice arrives. Gugnani & Co handles {name.lower()} for clients across Rohini and Delhi NCR from our Sector 9 office."]
    faq_html = "".join(f"<details><summary>{q.split('|')[0]}</summary><p>{q.split('|')[1]}</p></details>" for q in faqs)
    docs_html = "".join(f"<li>{d}</li>" for d in docs)
    areas_html = "".join(f'<a href="../areas/ca-in-{a}.html">{name} in {n}</a>' for a,n,*_ in AREAS[:10])
    related = "".join(f'<li><a href="{s[0]}.html">{s[1]}</a></li>' for s in SERVICES if s[0]!=slug)
    schema=[{"@context":"https://schema.org","@type":"Service","serviceType":name,"provider":{"@id":SITE+"/#firm"},"areaServed":"Delhi NCR","description":desc},
            {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q.split('|')[0],"acceptedAnswer":{"@type":"Answer","text":q.split('|')[1]}} for q in faqs]}]
    fig = '<figure class="svc-fig"><img src="../assets/gst-photo.jpg" alt="GST registration and GST return filing services in Rohini, Delhi" width="235" height="132" loading="lazy"><figcaption>GST compliance, handled end to end</figcaption></figure>' if slug.startswith("gst-") else ""
    stories_html = "".join(story_html(h, st, sid=f"process-{i+1}") for i,(h,st) in enumerate(STORIES.get(slug, [])))
    b = hero(f"{name} in Rohini, Delhi",desc+" Fast, accurate and affordable service by Gugnani &amp; Co.","../",f'<div class="crumb"><a href="../index.html">Home</a> › <a href="index.html">Services</a> › {name}</div>',name)+stories_html+f'''
<section><div class="wrap content"><div><h2>{name} Services by Gugnani &amp; Co</h2>{fig}<p>{body}</p>
<h2>Documents Required</h2><ul>{docs_html}</ul>
<h2>Our Process</h2><ol style="margin-left:20px"><li>Free consultation to understand your requirement</li><li>Document checklist shared on WhatsApp/email</li><li>Preparation and review by a qualified CA</li><li>Filing and acknowledgement shared with you</li><li>Follow-up and reminders for future compliance</li></ol>
<h2>Frequently Asked Questions</h2>{faq_html}
<h2>{name} Near You</h2><div class="chips">{areas_html}</div></div>
<aside class="side card"><h3>Other Services</h3><ul style="margin-left:18px">{related}</ul><p style="margin-top:14px"><a class="btn" href="tel:{TEL}">Call {PHONE}</a></p></aside></div></section>'''
    page(f"services/{slug}.html",f"{name} in Rohini Delhi | Gugnani & Co CA",f"{desc} Expert {name.lower()} by Gugnani & Co, CA in Rohini Sector 9, Delhi. Call +91-9953788989.",b,1,schema,[("Home",""),("Services","services/"),(name,f"services/{slug}.html")])

# ---------- AREAS ----------
page("areas/index.html","Areas We Serve | CA Services Across North & West Delhi","Gugnani & Co provides chartered accountant services in Rohini, Pitampura, Prashant Vihar, Rani Bagh, Shalimar Bagh and 20+ areas of Delhi NCR.",
 hero("Areas We Serve","From our Rohini office we serve clients across North and West Delhi, with doorstep visits.","../")+'<section><div class="wrap"><div class="grid">'+"".join(f'<a class="card" href="ca-in-{a}.html"><h3>CA in {n}</h3><p>Delhi {p} – {near}.</p></a>' for a,n,p,near,_ in AREAS)+'</div></div></section>',1,crumbs=[("Home",""),("Areas","areas/")])

FOCUS = [0,2,8,1,4,9,3,5,6,7,10,11,12,13,14,15,16]
for i,(slug,name,pin,near,body) in enumerate(AREAS):
    picks = [SERVICES[(i*3+k)%len(SERVICES)] for k in range(6)]
    svc = "".join(f'<a class="card" href="../services/{s[0]}.html"><h3>{s[1]} in {name}</h3><p>{s[2]}</p></a>' for s in picks)
    nearby = "".join(f'<a href="ca-in-{a[0]}.html">CA in {a[1]}</a>' for a in AREAS if a[0]!=slug)[:4000]
    faqs = [(f"Do you provide CA services in {name}?",f"Yes. Gugnani & Co serves clients in {name} ({pin}) from our Rohini Sector 9 office, with doorstep document pickup and online filing."),
            (f"What is the fee for ITR filing in {name}?","Fees depend on income sources; simple salaried returns start at an affordable fixed price. Call us for an exact quote."),
            (f"Can I visit your office from {name}?",f"Yes, our office at 130 Star Apartment, Sector 9, Rohini is easily reachable from {name}. We are open Monday to Saturday."),
            (f"How do I choose the best CA in {name}?",f"Check the CA's ICAI membership and firm registration number, experience with your type of work, a written fee quote, responsiveness before due dates and a nearby office. Gugnani & Co in Rohini Sector 9 serves clients in {name} – call +91-9953788989 for a free first consultation.")]
    fh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    schema=[{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
    b = hero(f"Chartered Accountant in {name}, Delhi {pin}",f"Gugnani &amp; Co – trusted CA for GST, income tax, audit and company registration in {name}, {near}.","../",f'<div class="crumb"><a href="../index.html">Home</a> › <a href="index.html">Areas</a> › {name}</div>')+f'''
<section><div class="wrap content"><div><h2>Your Local CA for {name}</h2><p>{body}</p>
<p>Clients from {name} choose Gugnani &amp; Co because we are nearby, respond quickly on phone and WhatsApp, and give fixed fee quotes before starting work. Whether you are a salaried employee, shop owner, doctor, manufacturer or NRI with property in {name}, we handle your compliance end to end.</p>
<h2>Popular Services in {name}</h2><div class="grid">{svc}</div>
<h2>FAQs – CA in {name}</h2>{fh}
<h2>Nearby Areas We Serve</h2><div class="chips">{nearby}</div></div>
<aside class="side card"><h3>CA near {name}</h3><p>{ADDR}</p><p>Pincode served: {pin}</p><p style="margin-top:10px"><a class="btn" href="tel:{TEL}">Call {PHONE}</a></p></aside></div></section>'''
    page(f"areas/ca-in-{slug}.html",f"CA in {name} Delhi {pin} | Chartered Accountant – Gugnani & Co",f"Looking for a CA in {name}, Delhi {pin}? Gugnani & Co offers GST, ITR filing, audit & company registration near {name}. Call +91-9953788989.",b,1,schema,[("Home",""),("Areas","areas/"),(f"CA in {name}",f"areas/ca-in-{slug}.html")])

# ---------- BLOG ----------
page("blog/index.html","Tax & GST Blog | Gugnani & Co Chartered Accountants","Practical articles on income tax, GST, TDS and business compliance from Gugnani & Co, CA in Rohini Delhi.",
 hero("Tax &amp; Compliance Blog","Simple, practical updates on income tax, GST and business compliance.","../")+'<section><div class="wrap"><div class="grid">'+"".join(f'<a class="card" href="{s}.html"><h3>{t}</h3><p>{d}</p><small>Read more →</small></a>' for s,t,d,_ in BLOGS)+'</div></div></section>',1,crumbs=[("Home",""),("Blog","blog/")])
for slug,t,d,paras in BLOGS:
    others = "".join(f'<li><a href="{s}.html">{tt}</a></li>' for s,tt,_,_ in BLOGS if s!=slug)
    ps = "".join(p if p.startswith("<ul") else f"<p style='margin-bottom:14px'>{p}</p>" for p in paras)
    schema=[{"@context":"https://schema.org","@type":"BlogPosting","headline":t,"description":d,"datePublished":POST_DATES.get(slug,"2026-10-01"),"author":{"@type":"Organization","name":"Gugnani & Co"},"publisher":{"@id":SITE+"/#firm"},"mainEntityOfPage":f"{SITE}/blog/{slug}.html"}]
    b = f'''<div class="hero"><div class="wrap" style="grid-template-columns:1fr"><div><div class="crumb"><a href="../index.html">Home</a> › <a href="index.html">Blog</a></div><h1>{t}</h1><p>{d}</p></div></div></div>
<section><div class="wrap content"><article>{ps}<p><b>Need help?</b> Call Gugnani &amp; Co on <a href="tel:{TEL}">{PHONE}</a> for expert assistance.</p><p style="font-size:13px;color:#6b7686;margin-top:14px">This article is for general information only and is not professional advice. Tax rules change; consult us for your specific case.</p></article>
<aside class="side card"><h3>More Articles</h3><ul style="margin-left:18px">{others}</ul></aside></div></section>'''
    page(f"blog/{slug}.html",f"{t} | Gugnani & Co",d,b,1,schema,[("Home",""),("Blog","blog/"),(t,f"blog/{slug}.html")])


# ---------- GLOBAL / COUNTRY PAGES ----------
exec(open('global_gen.py', encoding='utf-8').read())

# ---------- MISC ----------
allfaq = [q for s in SERVICES for q in s[5]][:12]
page("faq.html","FAQs | Chartered Accountant Services – Gugnani & Co","Answers to common questions on GST, income tax, company registration and audit from Gugnani & Co, CA in Rohini.",
 hero("Frequently Asked Questions","Quick answers to the questions our clients ask most.","")+'<section><div class="wrap">'+"".join(f"<details><summary>{q.split('|')[0]}</summary><p>{q.split('|')[1]}</p></details>" for q in allfaq)+'</div></section>',0,
 [{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q.split('|')[0],"acceptedAnswer":{"@type":"Answer","text":q.split('|')[1]}} for q in allfaq]}])
page("privacy-policy.html","Privacy Policy | Gugnani & Co","Privacy policy of gugnaniandco.com.",f'<section><div class="wrap"><h1>Privacy Policy</h1><p>We collect only the information you submit through our enquiry forms (name, phone, requirement) to respond to your query. We do not sell or share your data with third parties. Client documents are kept confidential as per ICAI professional standards. For any request regarding your data, email {EMAIL}.</p></div></section>',0)
page("disclaimer.html","Disclaimer | Gugnani & Co","Disclaimer for gugnaniandco.com as per ICAI guidelines.",'<section><div class="wrap"><h1>Disclaimer</h1><p>As per the guidelines of the Institute of Chartered Accountants of India, chartered accountants are not permitted to solicit work or advertise. This website is for information purposes only. By accessing it you acknowledge that you are seeking information about Gugnani &amp; Co of your own accord and that no solicitation has taken place. Content on this website is not professional advice.</p></div></section>',0)
page("thank-you.html","Thank You | Gugnani & Co","Thank you for contacting Gugnani & Co.",f'<section><div class="wrap" style="text-align:center"><h1>Thank You!</h1><p>We have received your enquiry and will call you back shortly. For urgent help call <a href="tel:{TEL}">{PHONE}</a>.</p><p style="margin-top:16px"><a class="btn" href="index.html">Back to Home</a></p></div></section>',0)

links = "".join(f'<li><a href="{p}">{p}</a></li>' for p in PAGES)
page("sitemap.html","Sitemap | Gugnani & Co","HTML sitemap of gugnaniandco.com.",f'<section><div class="wrap"><h1>Sitemap</h1><ul style="margin-left:20px;columns:2">{links}</ul></div></section>',0)

# robots + xml sitemap
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"<url><loc>{SITE}/{p.replace('index.html','')}</loc><lastmod>{TODAY}</lastmod><priority>{'1.0' if p=='index.html' else '0.8'}</priority></url>" for p in PAGES if p!="thank-you.html")
open(f"{OUT}/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
print(len(PAGES), "pages")

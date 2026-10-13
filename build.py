#!/usr/bin/env python3
"""Static site generator for Safe and Secure Solutions, Tumakuru.
Edit the CONFIG block, run `python3 build.py`, upload the contents of ./dist
"""
import os, json, shutil, html
from urllib.parse import quote

# ============================== CONFIG ==============================
DOMAIN = "https://www.example.com"        # <-- your real domain, no trailing slash
BIZ = "Safe and Secure Solutions"
PHONE_DISPLAY = "97432 74005"
PHONE_TEL = "+919743274005"
WA_LINK = "https://wa.me/919743274005"
CITY = "Tumakuru"
STATE = "Karnataka"
ADDRESS_STREET = ""                       # <-- verified shop street address (leave "" until confirmed)
POSTAL_CODE = ""                          # <-- e.g. 572101 if confirmed
OPENING_HOURS_TEXT = ""                   # <-- e.g. "Mon-Sat 10:00 AM - 7:00 PM" (only if verified)
OPENING_HOURS_SCHEMA = []                 # <-- e.g. ["Mo-Sa 10:00-19:00"] (only if verified)
GOOGLE_MAP_EMBED_SRC = ""                 # <-- src URL from Google Maps > Share > Embed a map
GBP_URL = ""                              # <-- your Google Business Profile / Maps URL
GBP_REVIEW_URL = ""                       # <-- "Ask for reviews" link from your GBP
GA4_ID = ""                               # <-- e.g. G-XXXXXXXXXX
GSC_VERIFICATION = ""                     # <-- content value of google-site-verification meta tag
FORM_ENDPOINT = ""                        # <-- optional Formspree/Web3Forms URL for email delivery
SOCIAL_SAMEAS = []                        # <-- real profile URLs only
LASTMOD = "2026-10-13"
# ====================================================================

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
e = html.escape

def maps_search():
    return "https://www.google.com/maps/search/?api=1&query=" + quote(f"{BIZ} {CITY} {STATE}")
DIRECTIONS = GBP_URL or maps_search()
REVIEW = GBP_REVIEW_URL or GBP_URL or maps_search()

def wa(msg):
    return WA_LINK + "?text=" + quote(msg)

# --------------------------- SERVICE PAGES ---------------------------
SERVICES = [
 dict(
  slug="laptop-repair-tumkur", nav="Laptop Repair", icon="💻",
  title="Laptop Repair & Service Center in Tumkur (Tumakuru)",
  meta="Laptop service center in Tumkur: screen, keyboard, battery, charging, motherboard repair, SSD/RAM upgrades and Windows support. Call 97432 74005.",
  h1="Laptop Repair & Service Center in Tumkur (Tumakuru)",
  intro=[
   "If your laptop will not switch on, charges slowly, runs hot or has a cracked screen, Safe and Secure Solutions in Tumakuru (Tumkur) can inspect it and tell you what is wrong before any repair is done. We handle laptops used by students, home users, professionals and small offices.",
   "Our workshop covers both hardware and software faults, so you do not have to visit one shop for a screen and another for Windows. We are also an authorized service center for Dell, Lenovo and Acer; see the brand pages below for details."],
  problems_h="Common laptop problems we repair",
  problems=[
   "Laptop not turning on, or turning on with a black screen",
   "Charging problems: not charging, charging stops at a fixed percentage, loose charging port",
   "Cracked, flickering or lined display needing laptop screen replacement",
   "Keyboard keys not working, liquid spill damage, or laptop keyboard replacement",
   "Battery draining quickly or swollen battery needing laptop battery replacement",
   "Overheating, loud fan and a slow laptop that hangs or restarts",
   "Motherboard faults needing laptop motherboard repair in Tumkur",
   "Windows will not boot, corrupted OS, virus or malware problems"],
  process_h="How our laptop diagnosis and repair works",
  process=[
   ("Tell us the problem","Call, WhatsApp or walk in and describe the fault. Share the brand and model if you can."),
   ("Inspection and diagnosis","We check the laptop to find the actual cause, whether it is the adapter, battery, display, storage, memory or board."),
   ("Quotation before repair","We explain what needs to be repaired or replaced and the cost, so you can decide before work starts."),
   ("Repair and testing","After your approval, the repair is done and the laptop is tested before hand-over."),
   ("Collection","We hand back the laptop and explain what was done. Back up your data before submitting the device.")],
  brands_h="Laptop brands we service",
  brands="We service Dell, Lenovo and Acer as an authorized service center, and also work on other common laptop makes. Call or WhatsApp with your model to confirm what we can handle.",
  why=[
   "Hardware and software repair under one roof",
   "Authorized service for Dell, Lenovo and Acer",
   "Explanation of the fault and quotation before work begins",
   "Upgrades such as SSD and RAM to speed up older laptops",
   "Easy contact by call or WhatsApp"],
  faqs=[
   ("Where can I repair my laptop in Tumkur?","You can bring your laptop to Safe and Secure Solutions in Tumakuru, or call or WhatsApp 97432 74005 to describe the fault first."),
   ("Can you upgrade my laptop with an SSD or RAM?","In many laptops, yes. Upgrade options depend on the model, so share your laptop model and we will confirm what is compatible."),
   ("Will I get a quote before the repair starts?","Yes. We diagnose first and explain the repair and cost before proceeding."),
   ("Should I back up my data?","Yes, please back up important files before submitting any device. Some repairs and software fixes can affect stored data.")],
  related=["desktop-computer-repair-tumkur","dell-service-center-tumkur","lenovo-service-center-tumkur","acer-service-center-tumkur","computer-accessories-tumkur"],
  alt="Laptop being diagnosed at a computer repair workshop in Tumakuru"),
 dict(
  slug="desktop-computer-repair-tumkur", nav="Desktop & Computer Repair", icon="🖥️",
  title="Desktop & Computer Repair Shop in Tumkur (Tumakuru)",
  meta="Computer repair shop in Tumakuru for desktop troubleshooting, SMPS and motherboard faults, SSD/RAM upgrades, Windows install and office maintenance.",
  h1="Desktop & Computer Repair Services in Tumkur (Tumakuru)",
  intro=[
   "A desktop that will not start or keeps freezing can stop your work or your child's studies. Safe and Secure Solutions provides desktop and PC repair services in Tumakuru for homes, schools, shops and offices.",
   "We troubleshoot the whole system: power supply, motherboard, memory, storage, graphics and the operating system, and explain the problem in plain language."],
  problems_h="Desktop problems we troubleshoot",
  problems=[
   "Computer not starting, no display, or repeated beeping on start-up",
   "Desktop SMPS repair and replacement after power failures or surges",
   "Motherboard faults and desktop motherboard repair",
   "Slow performance, hanging, blue screen errors and random restarts",
   "Hard disk failure, noisy drives, or storage that needs an SSD",
   "RAM faults and memory upgrades",
   "Windows installation, driver issues, virus and malware cleanup",
   "Network, USB, audio and peripheral issues"],
  process_h="Our computer troubleshooting process",
  process=[
   ("Describe the symptoms","Tell us what happens when you switch the PC on: beeps, lights, error messages or nothing at all."),
   ("Hardware and software check","We test power, memory, storage and board, and check the operating system if the machine boots."),
   ("Clear explanation and quotation","You are told what has failed and what the repair or replacement involves before work proceeds."),
   ("Repair or upgrade","Approved work is carried out, such as SMPS replacement, SSD or RAM installation or Windows reinstallation."),
   ("Testing and hand-over","The system is checked before it is returned.")],
  brands_h="Computers and brands",
  brands="We work on branded and assembled desktops. Contact us with the make and model of your machine so we can confirm the repair or upgrade options.",
  why=[
   "Practical fault finding for assembled and branded desktops",
   "Maintenance support for offices with several computers",
   "Performance upgrades such as SSD and RAM",
   "Plain explanation of what failed and why",
   "Call or WhatsApp for quick enquiries"],
  faqs=[
   ("Do you provide desktop and computer repair services?","Yes. Safe and Secure Solutions repairs and services desktops and computers, including hardware faults, upgrades and Windows problems."),
   ("Can you maintain computers for my office?","We provide office computer maintenance support. Contact us with the number of systems and the kind of support you need so we can discuss options."),
   ("My computer is not starting. What should I do?","Switch it off, check the power cable and socket, and contact us with what you see. We can guide you or inspect the system."),
   ("Do you install Windows?","Yes, we provide Windows installation and troubleshooting. Back up your files before bringing the computer in.")],
  related=["laptop-repair-tumkur","computer-accessories-tumkur","printer-repair-tumkur"],
  alt="Desktop computer being serviced by a technician in Tumkur"),
 dict(
  slug="printer-repair-tumkur", nav="Printer Repair", icon="🖨️",
  title="Printer Repair & Service in Tumkur (Tumakuru)",
  meta="Printer service center in Tumakuru: inkjet and laser printer repair, paper jams, not-printing and ink problems, plus printer maintenance for offices.",
  h1="Printer Repair & Service in Tumkur (Tumakuru)",
  intro=[
   "When a printer stops printing, jams paper or produces faded pages, it slows down homes, schools and offices. Safe and Secure Solutions repairs and services printers in Tumakuru and helps you decide whether a repair is worthwhile.",
   "We work on inkjet and laser printers and are an authorized service center for TVS-e printers. Call or WhatsApp with the printer model and a short description of the fault."],
  problems_h="Printer problems we handle",
  problems=[
   "Printer not printing, not detected by the computer, or showing an error",
   "Paper jams, paper pick-up failure and roller issues",
   "Faded, streaky or blank prints and ink or toner problems",
   "Ink not flowing after long periods of disuse",
   "Printer connectivity and driver set-up",
   "Routine servicing and maintenance for office printers"],
  process_h="How printer repair works",
  process=[
   ("Share the model and fault","Tell us the printer brand, model and what is happening."),
   ("Inspection","We inspect the printer, cartridges and connections to find the cause."),
   ("Quotation","We explain the repair, any parts needed and the cost before proceeding."),
   ("Repair and test print","After approval, we repair the printer and run test prints.")],
  brands_h="Printer brands",
  brands="We service TVS-e printers as an authorized service center. For other brands such as Epson, HP, Canon and Brother, please call or WhatsApp with your exact model so we can confirm whether we can support it.",
  why=[
   "Authorized service for TVS-e printers",
   "Repair, cartridge refilling and maintenance in one place",
   "Honest advice on repair versus replacement",
   "Support for offices that print regularly",
   "Quick enquiry by call or WhatsApp"],
  faqs=[
   ("Do you provide printer repair in Tumakuru?","Yes. Safe and Secure Solutions repairs and services printers. Share your printer model so we can confirm the right approach."),
   ("Do you service TVS-e printers?","Yes, we are an authorized service center for TVS-e. See our TVS-e page for details."),
   ("Can you fix a printer that is not printing?","In many cases yes, after inspection. The cause may be the cartridge, a clogged head, drivers or a hardware fault."),
   ("Do you offer printer maintenance for offices?","Yes. Contact us with your printer models and usage so we can discuss maintenance support.")],
  related=["cartridge-refilling-tumkur","tvs-e-printer-service-center-tumkur","desktop-computer-repair-tumkur"],
  alt="Printer repair and servicing in Tumakuru"),
 dict(
  slug="cartridge-refilling-tumkur", nav="Cartridge Refilling", icon="🖋️",
  title="Cartridge Refilling in Tumkur (Tumakuru): Ink & Toner",
  meta="Ink cartridge and toner refilling in Tumakuru. Check your printer model with us on WhatsApp for compatibility. Support for homes and offices.",
  h1="Cartridge Refilling in Tumkur (Tumakuru): Ink & Toner",
  intro=[
   "Buying a new cartridge each time can be expensive, and many cartridges can be refilled. Safe and Secure Solutions offers printer cartridge refilling in Tumakuru for homes, students and offices.",
   "Not every cartridge can be refilled, so we check the cartridge and printer model first and tell you honestly whether refilling is suitable."],
  problems_h="When people come for cartridge refilling",
  problems=[
   "Ink or toner has run out and prints are fading",
   "Black or colour ink cartridge needs a refill",
   "Laser printer toner cartridge refill for an office",
   "Cartridge not recognised or printing poorly after refilling elsewhere",
   "Offices wanting regular refilling for several printers"],
  process_h="How cartridge refilling enquiries work",
  process=[
   ("Send the printer and cartridge model","Share the printer model and cartridge number by WhatsApp, or bring the empty cartridge."),
   ("Compatibility check","We confirm whether that cartridge can be refilled."),
   ("Refill and check","If suitable, the cartridge is refilled and checked."),
   ("Test the print","You can confirm print quality at collection.")],
  brands_h="Compatible cartridges and printer models",
  brands="Compatibility depends on the cartridge type and condition. We do not promise to refill every cartridge. Send your printer model and cartridge number to confirm. Business customers with multiple printers can contact us for regular support.",
  why=[
   "Honest answer on whether your cartridge can be refilled",
   "Ink and toner refilling for homes and offices",
   "Printer repair available if the problem is the printer",
   "Easy enquiry on WhatsApp with a photo of the cartridge"],
  faqs=[
   ("Where can I refill my printer cartridge in Tumkur?","Safe and Secure Solutions in Tumakuru offers ink and toner cartridge refilling. Message us the printer and cartridge model first."),
   ("Can every cartridge be refilled?","No. Some cartridges are damaged or not designed for refilling. We check and advise before refilling."),
   ("Do you refill laser printer toner?","We handle toner refilling enquiries. Share the toner cartridge number to confirm."),
   ("Can my office get regular refilling support?","Yes, business customers can contact us to discuss ongoing cartridge refilling for their printers.")],
  related=["printer-repair-tumkur","tvs-e-printer-service-center-tumkur","computer-accessories-tumkur"],
  alt="Printer ink cartridges for refilling in Tumakuru"),
 dict(
  slug="computer-accessories-tumkur", nav="Computer Accessories", icon="⌨️",
  title="Computer & Laptop Accessories in Tumkur (Tumakuru)",
  meta="Computer accessories in Tumakuru: keyboards, mice, laptop chargers, cables, adapters, plus RAM and SSD upgrade services. Ask for availability.",
  h1="Computer & Laptop Accessories in Tumkur (Tumakuru)",
  intro=[
   "Along with repairs, Safe and Secure Solutions helps customers in Tumakuru with everyday computer and laptop accessories and parts.",
   "Stock changes from time to time, so please call or WhatsApp to confirm availability. If an item is not in the shop, we can tell you whether it can be sourced."],
  problems_h="What you can ask us about",
  problems=[
   "Keyboards and mice for desktops and laptops",
   "Laptop charger replacement, matched to your laptop model",
   "Cables and adapters",
   "RAM and SSD upgrades with installation",
   "Other peripherals and replacement parts on request"],
  process_h="How to enquire",
  process=[
   ("Tell us what you need","Name the item and, for chargers or upgrades, your laptop or computer model."),
   ("We confirm availability","We tell you if it is in stock or can be sourced."),
   ("Fitting if needed","For RAM, SSD or chargers we can help with fitting and testing.")],
  brands_h="Compatibility",
  brands="For chargers, memory and storage, compatibility depends on the exact model. Send the model number, or a photo of the label on the laptop or charger.",
  why=[
   "Accessories and installation help in one place",
   "Help choosing the correct charger, RAM or SSD for your model",
   "Repair support if the problem is more than an accessory"],
  faqs=[
   ("Do you sell computer accessories in Tumkur?","Yes, we offer computer and laptop accessories. Availability varies, so please ask before visiting."),
   ("Can you replace my laptop charger?","We can help with charger replacement. Send your laptop model or a photo of the charger label."),
   ("Will you install the RAM or SSD for me?","Yes, we provide RAM and SSD upgrade services, subject to your computer's compatibility.")],
  related=["laptop-repair-tumkur","desktop-computer-repair-tumkur","cartridge-refilling-tumkur"],
  alt="Computer keyboards, mice and laptop accessories"),
]

BRANDS = [
 dict(slug="dell-service-center-tumkur", nav="Dell Service", brand="Dell", kind="laptops",
  title="Dell Laptop Service Center in Tumkur (Tumakuru)",
  meta="Dell authorized service center in Tumkur, Tumakuru. Dell laptop repair, diagnosis and support. Call or WhatsApp 97432 74005 to book.",
  h1="Dell Laptop Service Center in Tumkur (Tumakuru)",
  intro=["Safe and Secure Solutions is an authorized service center for Dell in Tumakuru (Tumkur). If your Dell laptop has a hardware or software issue, you can contact us for diagnosis and service.",
         "We are not a company-owned Dell store. We are an authorized service center operated independently, and the specific services available depend on your product and its warranty status."],
  products="Dell laptops. Contact us with your model name or service tag so we can confirm what is covered.",
  services=["Diagnosis of power, display, battery, keyboard and performance issues","Hardware repair and part replacement as applicable","Windows and driver troubleshooting","Guidance on warranty-related service for eligible products"],
  steps=["Collect your Dell service tag (usually on a sticker under the laptop) and note the problem.","Call or WhatsApp us, or visit the shop.","We inspect the laptop and explain the findings and next steps.","Warranty coverage and charges are confirmed according to the product's status before proceeding."],
  faqs=[("Do you service Dell laptops in Tumkur?","Yes, Safe and Secure Solutions is an authorized service center for Dell."),
        ("What should I bring for Dell service?","Bring the laptop, its charger and any proof of purchase you have. Note your service tag if you can."),
        ("Is my Dell laptop covered under warranty?","Coverage depends on the product and its warranty terms. We will help check when you contact us.")],
  related=["laptop-repair-tumkur","lenovo-service-center-tumkur","acer-service-center-tumkur"],
  alt="Dell laptop service in Tumakuru"),
 dict(slug="lenovo-service-center-tumkur", nav="Lenovo Service", brand="Lenovo", kind="laptops",
  title="Lenovo Authorized Service Center in Tumkur (Tumakuru)",
  meta="Lenovo authorized service center in Tumkur (Tumakuru). Lenovo laptop repair, screen, battery and keyboard service. Call 97432 74005.",
  h1="Lenovo Authorized Service Center in Tumkur (Tumakuru)",
  intro=["Safe and Secure Solutions is an authorized service center for Lenovo in Tumakuru (Tumkur). Whether your Lenovo laptop will not charge, has a damaged screen or runs slowly, we can inspect it and advise.",
         "We are an independently run authorized service center, not a Lenovo-owned store. Services depend on the product and its warranty status."],
  products="Lenovo laptops. Share your model name or serial number so we can confirm support.",
  services=["Screen, keyboard and battery issues","Charging and power faults","Overheating, slow performance and software problems","Support for warranty-eligible products according to Lenovo's terms"],
  steps=["Note your Lenovo model and serial number (on the label under the laptop).","Contact us by call or WhatsApp, or bring the laptop in.","We diagnose the issue and explain the options.","Warranty status and any chargeable work are explained before repair."],
  faqs=[("Are you a Lenovo authorized service center in Tumkur?","Yes, Safe and Secure Solutions is an authorized service center for Lenovo."),
        ("Can you replace a Lenovo laptop battery or screen?","Depending on the model and part availability, yes. We will confirm after inspection."),
        ("Do you repair out-of-warranty Lenovo laptops?","Yes, we can inspect and repair laptops that are out of warranty as well.")],
  related=["laptop-repair-tumkur","dell-service-center-tumkur","acer-service-center-tumkur"],
  alt="Lenovo laptop repair in Tumakuru"),
 dict(slug="acer-service-center-tumkur", nav="Acer Service", brand="Acer", kind="laptops",
  title="Acer Authorized Service Center in Tumkur (Tumakuru)",
  meta="Acer authorized service center in Tumkur (Tumakuru). Acer laptop repair and diagnosis. Call or WhatsApp 97432 74005 for service enquiries.",
  h1="Acer Authorized Service Center in Tumkur (Tumakuru)",
  intro=["Safe and Secure Solutions is an authorized service center for Acer in Tumakuru (Tumkur). If your Acer laptop has stopped working properly, you can bring it in for inspection.",
         "We are an independently operated authorized service center, not an Acer-owned store, and service terms depend on your product and warranty."],
  products="Acer laptops. Please share your model number and serial number.",
  services=["Fault diagnosis for power, display, keyboard and battery issues","Repair and replacement of parts as applicable","Windows reinstall and performance troubleshooting","Warranty guidance for eligible products"],
  steps=["Note your Acer model and serial number.","Call or WhatsApp us with a short description of the problem.","Bring the laptop and charger for inspection.","We explain what is needed and confirm any charges before work."],
  faqs=[("Do you service Acer laptops in Tumkur?","Yes, Safe and Secure Solutions is an authorized service center for Acer."),
        ("How do I request an Acer laptop diagnosis?","Call or WhatsApp 97432 74005, or use the repair form on our contact page."),
        ("Can you upgrade RAM or SSD in my Acer laptop?","On many models, yes. Share your model number to confirm compatibility.")],
  related=["laptop-repair-tumkur","dell-service-center-tumkur","lenovo-service-center-tumkur"],
  alt="Acer laptop service in Tumakuru"),
 dict(slug="tvs-e-printer-service-center-tumkur", nav="TVS-e Service", brand="TVS-e", kind="printers",
  title="TVS-e Printer Service Center in Tumkur (Tumakuru)",
  meta="TVS-e printer service center in Tumkur (Tumakuru). Printer repair, troubleshooting and support. Call or WhatsApp 97432 74005.",
  h1="TVS-e Printer Service Center in Tumkur (Tumakuru)",
  intro=["Safe and Secure Solutions is an authorized service center for TVS-e in Tumakuru (Tumkur). If your TVS-e printer is not printing, jamming or giving errors, contact us for service.",
         "We are an independently operated authorized service center, not a TVS-e-owned outlet. Services and warranty handling depend on the product and its terms."],
  products="TVS-e printers. Share the printer model and what the printer is doing so we can advise.",
  services=["Printer fault diagnosis and repair","Paper jam and paper feed problems","Print quality and consumable issues","Driver installation and connectivity help"],
  steps=["Note your printer model and the problem or error shown.","Call or WhatsApp us, or bring the printer to the shop.","We inspect and explain what is needed.","Warranty status and any charges are confirmed before repair."],
  faqs=[("Do you provide TVS-e printer servicing in Tumkur?","Yes, Safe and Secure Solutions is an authorized service center for TVS-e."),
        ("My TVS-e printer is not printing. Can you help?","Yes. Contact us with the model and symptoms, and we will inspect it."),
        ("Do you also refill cartridges?","We offer cartridge refilling enquiries; compatibility depends on the cartridge. See our cartridge refilling page.")],
  related=["printer-repair-tumkur","cartridge-refilling-tumkur","computer-accessories-tumkur"],
  alt="TVS-e printer service in Tumakuru"),
]
ALL = {p["slug"]: p for p in SERVICES + BRANDS}

HOME_FAQS = [
 ("Where can I repair my laptop in Tumkur?","Safe and Secure Solutions in Tumakuru repairs laptops. Call or WhatsApp 97432 74005 to describe the problem."),
 ("Do you provide desktop and computer repair services?","Yes. We troubleshoot and repair desktops and computers, including upgrades and Windows issues."),
 ("Do you provide printer repair in Tumakuru?","Yes. We repair and service printers and are an authorized service center for TVS-e."),
 ("Where can I refill my printer cartridge in Tumkur?","We offer ink and toner cartridge refilling. Send your printer and cartridge model first to confirm compatibility."),
 ("Do you service Dell, Lenovo and Acer laptops?","Yes. We are an authorized service center for Dell, Lenovo and Acer."),
 ("Do you provide TVS-e printer servicing?","Yes. We are an authorized service center for TVS-e."),
 ("Can I contact you on WhatsApp for a repair enquiry?","Yes. Message us on 97432 74005 with your device model and a short description of the problem."),
 ("How can I request a laptop or printer diagnosis?","Call, WhatsApp, use the Book a Repair form, or visit the shop. We inspect first and explain before repair."),
 ("Do you provide computer maintenance for offices?","Yes. Contact us with the number of computers and printers so we can discuss support."),
]

# --------------------------- SHARED PIECES ---------------------------
NAV = [("/", "Home"), ("/laptop-repair-tumkur.html", "Laptop"), ("/desktop-computer-repair-tumkur.html", "Desktop"),
       ("/printer-repair-tumkur.html", "Printer"), ("/cartridge-refilling-tumkur.html", "Cartridge"),
       ("/computer-accessories-tumkur.html", "Accessories"), ("/contact.html", "Contact")]

def url(path):
    return DOMAIN + ("" if path == "/" else path)

def address_text():
    if ADDRESS_STREET:
        return f"{ADDRESS_STREET}, {CITY}, {STATE}" + (f" {POSTAL_CODE}" if POSTAL_CODE else "")
    return f"{CITY} (Tumkur), {STATE}, India"

def ld_business():
    d = {"@context": "https://schema.org", "@type": "LocalBusiness", "@id": DOMAIN + "/#business",
         "name": BIZ, "url": DOMAIN + "/", "telephone": PHONE_TEL,
         "description": "Laptop, desktop, computer and printer repair, cartridge refilling and computer accessories in Tumakuru (Tumkur), Karnataka. Authorized service center for Dell, Lenovo, Acer and TVS-e.",
         "areaServed": {"@type": "City", "name": CITY},
         "address": {"@type": "PostalAddress", "addressLocality": CITY, "addressRegion": STATE, "addressCountry": "IN"}}
    if ADDRESS_STREET: d["address"]["streetAddress"] = ADDRESS_STREET
    if POSTAL_CODE: d["address"]["postalCode"] = POSTAL_CODE
    if OPENING_HOURS_SCHEMA: d["openingHours"] = OPENING_HOURS_SCHEMA
    if GBP_URL: d["hasMap"] = GBP_URL
    if SOCIAL_SAMEAS: d["sameAs"] = SOCIAL_SAMEAS
    return d

def ld_faq(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def ld_crumbs(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(crumbs)]}

def ld_service(p):
    return {"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "serviceType": p.get("nav", p["h1"]),
            "provider": {"@id": DOMAIN + "/#business"}, "areaServed": {"@type": "City", "name": CITY},
            "description": p["meta"]}

def script_ld(objs):
    return "\n".join('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>" for o in objs)

def page(path, title, meta, body, crumbs=None, ld=None, noindex=False, extra_head=""):
    canon = url(path)
    gsc = f'<meta name="google-site-verification" content="{e(GSC_VERIFICATION)}">' if GSC_VERIFICATION else ""
    ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
          f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>") if GA4_ID else ""
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    objs = [ld_business()] + (ld or [])
    if crumbs: objs.append(ld_crumbs(crumbs))
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    crumb_html = ""
    if crumbs and len(crumbs) > 1:
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>' + "".join(
            (f'<li><a href="{p_}">{e(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{e(n)}</li>')
            for i, (n, p_) in enumerate(crumbs)) + "</ol></div></nav>"
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title if len(title)+len(BIZ)+3>60 else title+" | "+BIZ)}</title>
<meta name="description" content="{e(meta)}">
{robots}
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0b2545">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(meta)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
{gsc}{extra_head}
{script_ld(objs)}
{ga}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap bar">
  <a class="brand" href="/" aria-label="{BIZ} home"><span class="logo">S&amp;S</span><span class="bn">{BIZ}<small>{CITY} (Tumkur)</small></span></a>
  <nav class="main-nav" id="nav" aria-label="Main">{nav}</nav>
  <div class="hdr-cta">
   <a class="btn btn-call" href="tel:{PHONE_TEL}">📞 <span>Call Now</span></a>
   <a class="btn btn-wa" href="{wa('Hello, I need a service enquiry.')}" rel="noopener">💬 <span>WhatsApp</span></a>
   <button class="menu" aria-label="Menu" aria-expanded="false" aria-controls="nav">☰</button>
  </div>
 </div>
</header>
{crumb_html}
<main id="main">
{body}
</main>
<footer class="site-footer">
 <div class="wrap grid4">
  <div><h3>{BIZ}</h3><p>Computer, laptop and printer repair centre in {CITY} (Tumkur), {STATE}.</p>
   <p><strong>Address:</strong> {e(address_text())}</p>
   <p><strong>Phone / WhatsApp:</strong> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
   <p><strong>Hours:</strong> {e(OPENING_HOURS_TEXT) if OPENING_HOURS_TEXT else "Call or WhatsApp to confirm"}</p></div>
  <div><h3>Services</h3><ul>{"".join(f'<li><a href="/{s["slug"]}.html">{s["nav"]}</a></li>' for s in SERVICES)}</ul></div>
  <div><h3>Authorized service</h3><ul>{"".join(f'<li><a href="/{b["slug"]}.html">{b["brand"]} service center</a></li>' for b in BRANDS)}</ul></div>
  <div><h3>Company</h3><ul><li><a href="/about.html">About us</a></li><li><a href="/faq.html">FAQ</a></li><li><a href="/contact.html">Contact &amp; book repair</a></li><li><a href="{DIRECTIONS}" rel="noopener">Get directions</a></li><li><a href="{REVIEW}" rel="noopener">Leave a Google review</a></li><li><a href="/privacy-policy.html">Privacy policy</a></li></ul></div>
 </div>
 <div class="wrap legal">© <span id="yr">2026</span> {BIZ}, {CITY}. Brand names belong to their respective owners. Authorized service status is subject to each brand's current authorization.</div>
</footer>
<div class="mbar" role="navigation" aria-label="Quick contact">
 <a href="tel:{PHONE_TEL}">📞 Call</a>
 <a href="{wa('Hello, I need a service enquiry.')}" rel="noopener">💬 WhatsApp</a>
 <a href="{DIRECTIONS}" rel="noopener">📍 Directions</a>
</div>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def cta_row(msg="Hello, I need a service enquiry."):
    return (f'<div class="cta-row"><a class="btn btn-call big" href="tel:{PHONE_TEL}">📞 Call Now: {PHONE_DISPLAY}</a>'
            f'<a class="btn btn-wa big" href="{wa(msg)}" rel="noopener">💬 WhatsApp for Service</a>'
            f'<a class="btn btn-ghost big" href="/contact.html#book">Book a Repair</a>'
            f'<a class="btn btn-ghost big" href="{DIRECTIONS}" rel="noopener">📍 Get Directions</a></div>')

def faq_block(faqs, h="Frequently asked questions"):
    return f'<section class="sec"><div class="wrap narrow"><h2>{h}</h2>' + "".join(
        f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faqs) + "</section>".replace("</section>", "</div></section>")

def contact_card():
    return f"""<aside class="card contact-card" aria-label="Contact details">
<h2>Contact {BIZ}</h2>
<p><strong>Location:</strong> {e(address_text())}</p>
<p><strong>Phone / WhatsApp:</strong> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<p><strong>Hours:</strong> {e(OPENING_HOURS_TEXT) if OPENING_HOURS_TEXT else "Please call or WhatsApp to confirm"}</p>
<p><a class="btn btn-ghost" href="{DIRECTIONS}" rel="noopener">📍 Get directions</a></p></aside>"""

def related_block(slugs):
    cards = "".join(f'<a class="card link-card" href="/{s}.html"><strong>{ALL[s]["h1"].split(" in Tumkur")[0].split(" Tumkur")[0]}</strong><span>{e(ALL[s]["meta"][:95].rsplit(" ",1)[0])}…</span></a>' for s in slugs)
    return f'<section class="sec alt"><div class="wrap"><h2>Related services</h2><div class="grid3">{cards}</div></div></section>'

# ----------------------------- PAGE BUILDERS -----------------------------
def build_service(p):
    path = f"/{p['slug']}.html"
    crumbs = [("Home", "/"), (p["nav"], path)]
    body = f"""<section class="hero small"><div class="wrap"><h1>{e(p['h1'])}</h1>
<p class="lead">{p['intro'][0]}</p>{cta_row(f"Hello, I need help with: {p['nav']}.")}</div></section>
<section class="sec"><div class="wrap two"><div>
<p>{p['intro'][1]}</p>
<h2>{p['problems_h']}</h2>{ul(p['problems'])}
<h2>{p['process_h']}</h2><ol class="steps">{''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a,b in p['process'])}</ol>
<h2>{p['brands_h']}</h2><p>{p['brands']}</p>
<h2>Why choose {BIZ}</h2>{ul(p['why'])}
<p class="note">Diagnosis, quotation and any warranty terms are explained at the time of service, as they vary by device and repair. Back up important data before submitting any device.</p>
</div>{contact_card()}</div></section>
{faq_block(p['faqs'], f"{p['nav']} FAQs")}
{related_block(p['related'])}"""
    return page(path, p["title"], p["meta"], body, crumbs, [ld_service(p), ld_faq(p["faqs"])])

def build_brand(b):
    path = f"/{b['slug']}.html"
    crumbs = [("Home", "/"), (f"{b['brand']} Service Center", path)]
    kind_page = "/laptop-repair-tumkur.html" if b["kind"] == "laptops" else "/printer-repair-tumkur.html"
    body = f"""<section class="hero small"><div class="wrap"><h1>{e(b['h1'])}</h1>
<p class="lead">{b['intro'][0]}</p>{cta_row(f"Hello, I need {b['brand']} service.")}</div></section>
<section class="sec"><div class="wrap two"><div>
<p>{b['intro'][1]}</p>
<h2>{b['brand']} products we support</h2><p>{b['products']}</p>
<h2>{b['brand']} services available in Tumakuru</h2>{ul(b['services'])}
<h2>How {b['brand']} service works at our centre</h2><ol class="steps">{''.join(f'<li><span>{s}</span></li>' for s in b['steps'])}</ol>
<p>See also our general <a href="{kind_page}">{b['kind'][:-1]} repair services in Tumkur</a>.</p>
<p class="note">{b['brand']} is a trademark of its respective owner. {BIZ} is described here as an authorized service center; it is not a company-owned store.</p>
</div>{contact_card()}</div></section>
{faq_block(b['faqs'], f"{b['brand']} service FAQs")}
{related_block(b['related'])}"""
    return page(path, b["title"], b["meta"], body, crumbs, [ld_service(dict(b, nav=b["brand"] + " service")), ld_faq(b["faqs"])])

def build_home():
    title = "Laptop, Desktop & Printer Repair in Tumakuru (Tumkur)"
    meta = "Safe and Secure Solutions: laptop, desktop and printer repair, cartridge refilling and accessories in Tumakuru. Authorized for Dell, Lenovo, Acer, TVS-e."
    svc_cards = "".join(f'<a class="card link-card" href="/{s["slug"]}.html"><span class="ico" aria-hidden="true">{s["icon"]}</span><strong>{s["nav"]}</strong><span>{e(s["meta"][:100].rsplit(" ",1)[0])}…</span></a>' for s in SERVICES)
    brand_cards = "".join(f'<a class="card link-card" href="/{b["slug"]}.html"><strong>{b["brand"]}</strong><span>Authorized service center in Tumkur</span></a>' for b in BRANDS)
    body = f"""<section class="hero"><div class="wrap">
<p class="eyebrow">{BIZ} · {CITY} (Tumkur), {STATE}</p>
<h1>Laptop, Desktop &amp; Printer Repair Services in Tumakuru</h1>
<p class="lead">Looking for a reliable laptop repair shop in Tumkur? {BIZ} provides laptop servicing, desktop troubleshooting, printer repair, cartridge refilling and IT support for homes, students, offices and businesses.</p>
{cta_row("Hello, I need a laptop/computer/printer service.")}
<ul class="chips"><li>Authorized service: Dell</li><li>Lenovo</li><li>Acer</li><li>TVS-e</li><li>Phone / WhatsApp {PHONE_DISPLAY}</li></ul>
</div></section>
<section class="sec"><div class="wrap"><h2>Our computer and printer services in Tumkur</h2><div class="grid3">{svc_cards}</div></div></section>
<section class="sec alt"><div class="wrap"><h2>Authorized laptop and printer service center in Tumkur</h2>
<p>We are an authorized service center for Dell, Lenovo, Acer and TVS-e. Choose your brand for supported products and how service works.</p><div class="grid4">{brand_cards}</div></div></section>
<section class="sec"><div class="wrap two"><div>
<h2>Why customers in Tumakuru contact us</h2>
{ul(["One place for laptop, desktop and printer problems","We diagnose first and explain the fault and cost before repair","Authorized service for Dell, Lenovo, Acer and TVS-e","Cartridge refilling and accessories along with repairs","Quick contact by call or WhatsApp"])}
<h2>Computer technician in Tumakuru for homes and offices</h2>
<p>From a student's laptop to an office with several computers and printers, we help with repairs, upgrades and regular maintenance. Tell us what you need and we will advise on the next step.</p>
</div>{contact_card()}</div></section>
<section class="sec alt"><div class="wrap narrow"><h2>Visit or contact us</h2>
<p>Find us in {CITY} (Tumkur), {STATE}. Use the buttons below for directions, calls and WhatsApp enquiries.</p>
<div class="cta-row"><a class="btn btn-ghost big" href="{DIRECTIONS}" rel="noopener">📍 Get Directions</a><a class="btn btn-ghost big" href="{REVIEW}" rel="noopener">⭐ Leave a Genuine Review</a><a class="btn btn-ghost big" href="/contact.html">Contact page</a></div></div></section>
{faq_block(HOME_FAQS)}"""
    return page("/", title, meta, body, None, [ld_faq(HOME_FAQS)])

def build_about():
    body = f"""<section class="hero small"><div class="wrap"><h1>About {BIZ}, Tumakuru</h1>
<p class="lead">A local computer, laptop and printer service centre in {CITY} (Tumkur), {STATE}.</p></div></section>
<section class="sec"><div class="wrap two"><div>
<h2>What we do</h2>
<p>{BIZ} repairs and services laptops, desktops and printers, refills printer cartridges and helps customers with computer accessories and upgrades. We serve homes, students, offices and small businesses in Tumakuru.</p>
<h2>Authorized service</h2>
<p>We are an authorized service center for Dell, Lenovo, Acer and TVS-e. See our pages for <a href="/dell-service-center-tumkur.html">Dell</a>, <a href="/lenovo-service-center-tumkur.html">Lenovo</a>, <a href="/acer-service-center-tumkur.html">Acer</a> and <a href="/tvs-e-printer-service-center-tumkur.html">TVS-e</a>.</p>
<h2>How we work</h2>
<p>We diagnose the problem first, explain what we find and discuss the repair and cost before starting. We would rather give you a straight answer, including when a repair is not worthwhile, than sell you work you do not need.</p>
<h2>Contact</h2>
<p>Call or WhatsApp <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>, or visit the <a href="/contact.html">contact page</a>.</p>
</div>{contact_card()}</div></section>"""
    return page("/about.html", f"About {BIZ} | Computer Service in Tumakuru",
                f"About {BIZ}: laptop, desktop and printer repair and authorized service for Dell, Lenovo, Acer and TVS-e in Tumakuru (Tumkur).",
                body, [("Home", "/"), ("About", "/about.html")])

def build_faq():
    items = HOME_FAQS + [
      ("Do you refill laser toner cartridges?","We handle toner refilling enquiries. Share the cartridge model on WhatsApp to confirm."),
      ("Can you upgrade my laptop with SSD or RAM?","On many laptops, yes. Share the model so we can confirm compatibility.")]
    body = f"""<section class="hero small"><div class="wrap"><h1>FAQs: Computer, Laptop &amp; Printer Service in Tumkur</h1>
<p class="lead">Answers to common questions about repairs, cartridge refilling and authorized service at {BIZ}.</p></div></section>
{faq_block(items, "Common questions")}
<section class="sec"><div class="wrap narrow"><p>Still have a question? </p>{cta_row("Hello, I have a question.")}</div></section>"""
    return page("/faq.html", "FAQ: Laptop, Printer & Computer Service in Tumkur",
                "Frequently asked questions about laptop repair, desktop repair, printer service and cartridge refilling at Safe and Secure Solutions, Tumakuru.",
                body, [("Home", "/"), ("FAQ", "/faq.html")], [ld_faq(items)])

def build_contact():
    map_html = (f'<iframe title="Map of {BIZ}, {CITY}" src="{GOOGLE_MAP_EMBED_SRC}" width="100%" height="380" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
                if GOOGLE_MAP_EMBED_SRC else
                f'<div class="mapph"><p>See our location on Google Maps.</p><a class="btn btn-call big" href="{DIRECTIONS}" rel="noopener">📍 Open in Google Maps</a></div>')
    action = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f"""<section class="hero small"><div class="wrap"><h1>Contact {BIZ}, Tumakuru: Call, WhatsApp or Book a Repair</h1>
<p class="lead">Reach us for laptop, desktop and printer repair, cartridge refilling and accessories in Tumkur.</p>{cta_row()}</div></section>
<section class="sec"><div class="wrap two"><div>
<h2>Book a repair or send an enquiry</h2>
<p>Fill in the form and it will open WhatsApp with your details ready to send. We only ask for what is needed.</p>
<form id="book" class="form"{action} data-wa="{WA_LINK}">
 <label>Your name<input name="name" required autocomplete="name"></label>
 <label>Phone number<input name="phone" type="tel" required autocomplete="tel" inputmode="tel"></label>
 <label>Service needed<select name="service" required>
  <option value="">Select</option>{''.join(f'<option>{s["nav"]}</option>' for s in SERVICES)}
  {''.join(f'<option>{b["brand"]} service</option>' for b in BRANDS)}<option>Other</option></select></label>
 <label>Device brand and model<input name="model" placeholder="e.g. Dell Inspiron 15"></label>
 <label>What is the problem?<textarea name="message" rows="4" required></textarea></label>
 <button class="btn btn-wa big" type="submit">💬 Send on WhatsApp</button>
 <p class="note">Please do not send passwords or sensitive personal data.</p>
</form></div>
{contact_card()}</div></section>
<section class="sec alt"><div class="wrap"><h2>Location and directions</h2>{map_html}
<div class="cta-row"><a class="btn btn-ghost big" href="{DIRECTIONS}" rel="noopener">📍 Get Directions</a><a class="btn btn-ghost big" href="{REVIEW}" rel="noopener">⭐ Leave a Google Review</a></div></div></section>"""
    return page("/contact.html", f"Contact {BIZ} | Computer Repair Tumkur",
                "Call, WhatsApp or book a laptop, desktop or printer repair with Safe and Secure Solutions in Tumakuru. Phone 97432 74005. Get directions.",
                body, [("Home", "/"), ("Contact", "/contact.html")])

def build_privacy():
    body = f"""<section class="hero small"><div class="wrap"><h1>Privacy Policy</h1><p class="lead">Last updated: {LASTMOD}</p></div></section>
<section class="sec"><div class="wrap narrow">
<h2>Who we are</h2><p>{BIZ}, {CITY}, {STATE}, India. Contact: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
<h2>Information we collect</h2><p>When you use our enquiry form we collect your name, phone number, service needed, device details and message. The form opens WhatsApp with this information so you can send it to us; if an email form service is enabled, it is delivered to us through that service.</p>
<h2>How we use it</h2><p>Only to respond to your enquiry and provide the service you request. We do not sell your information.</p>
<h2>Cookies and analytics</h2><p>If Google Analytics is enabled, it collects anonymous usage data such as pages viewed to help us improve the site. Embedded Google Maps may set cookies according to Google's policies.</p>
<h2>Your devices and data</h2><p>Please back up and remove sensitive data before submitting devices for repair. We recommend not sharing passwords.</p>
<h2>Your choices</h2><p>You can ask us to delete enquiry details we hold by calling or messaging us.</p>
<h2>Changes</h2><p>We may update this policy; the date above shows the latest revision.</p>
</div></section>"""
    return page("/privacy-policy.html", "Privacy Policy", f"Privacy policy of {BIZ}, Tumakuru: how we handle enquiry details, analytics and cookies.",
                body, [("Home", "/"), ("Privacy Policy", "/privacy-policy.html")])

def build_404():
    body = f"""<section class="hero small"><div class="wrap"><h1>Page not found</h1>
<p class="lead">Sorry, we could not find that page. Try one of these:</p>
<ul class="chips"><li><a href="/">Home</a></li><li><a href="/laptop-repair-tumkur.html">Laptop repair</a></li><li><a href="/printer-repair-tumkur.html">Printer repair</a></li><li><a href="/contact.html">Contact</a></li></ul>
{cta_row()}</div></section>"""
    return page("/404.html", "Page Not Found", "The page you are looking for could not be found.", body, None, None, noindex=True)

# ----------------------------- ASSETS -----------------------------
CSS = """
:root{--navy:#0b2545;--navy2:#13315c;--blue:#1d4e89;--grey:#f1f4f8;--line:#d9e0ea;--text:#1b2733;--wa:#1faa59;--call:#0b2545;--amber:#f2a900}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--text);background:#fff;padding-bottom:64px}
img,iframe{max-width:100%}a{color:var(--blue)}
.wrap{max-width:1120px;margin:0 auto;padding:0 18px}.narrow{max-width:820px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:99}
.site-header{position:sticky;top:0;z-index:50;background:var(--navy);color:#fff;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.bar{display:flex;align-items:center;gap:14px;min-height:62px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;margin-right:auto}
.logo{background:#fff;color:var(--navy);font-weight:800;border-radius:8px;padding:6px 8px;font-size:15px}
.bn{font-weight:700;line-height:1.1;font-size:15px}.bn small{display:block;font-weight:400;opacity:.8;font-size:12px}
.main-nav{display:flex;gap:4px;flex-wrap:wrap}.main-nav a{color:#dbe6f5;text-decoration:none;padding:8px 10px;border-radius:6px;font-size:14px}
.main-nav a:hover,.main-nav a:focus{background:var(--navy2);color:#fff}
.hdr-cta{display:flex;gap:8px;align-items:center}
.menu{display:none;background:none;border:1px solid #5b7aa5;color:#fff;border-radius:6px;font-size:20px;padding:4px 10px}
.btn{display:inline-flex;align-items:center;gap:6px;border-radius:8px;padding:9px 14px;font-weight:600;text-decoration:none;border:2px solid transparent;cursor:pointer;font-size:15px;line-height:1.2}
.btn-call{background:var(--amber);color:#1b1b1b}.btn-wa{background:var(--wa);color:#fff}
.btn-ghost{background:#fff;color:var(--navy);border-color:var(--navy)}
.hero .btn-ghost{border-color:#fff}.btn.big{padding:12px 18px;font-size:16px}
.btn:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #ffbf47;outline-offset:2px}
.hero{background:linear-gradient(135deg,var(--navy),var(--blue));color:#fff;padding:54px 0 46px}
.hero.small{padding:36px 0 30px}.hero h1{font-size:clamp(26px,4.4vw,42px);line-height:1.2;margin:.2em 0 .4em}
.hero .lead{font-size:18px;max-width:760px;color:#e4edf9}.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:13px;color:#ffd978;margin:0}
.cta-row{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.chips{list-style:none;display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:14px 0 0}
.chips li{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:4px 12px;font-size:14px}
.chips a{color:#fff}
.sec{padding:44px 0}.sec.alt{background:var(--grey)}
h2{color:var(--navy);font-size:clamp(21px,3vw,28px);line-height:1.25;margin:1.4em 0 .5em}.sec h2:first-child{margin-top:0}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px}
.link-card{display:flex;flex-direction:column;gap:6px;text-decoration:none;color:var(--text);transition:.15s}
.link-card:hover{border-color:var(--blue);box-shadow:0 6px 18px rgba(11,37,69,.12);transform:translateY(-2px)}
.link-card strong{color:var(--navy);font-size:17px}.link-card span{font-size:14px;color:#4a5a6c}.ico{font-size:28px}
.two{display:grid;grid-template-columns:1fr 340px;gap:32px;align-items:start}
.contact-card{position:sticky;top:84px;background:var(--grey)}.contact-card h2{font-size:20px;margin:0 0 .6em}
ul{padding-left:1.2em}li{margin:.3em 0}
.steps{list-style:none;counter-reset:s;padding:0}.steps li{counter-increment:s;display:flex;gap:12px;align-items:flex-start;background:var(--grey);border-radius:10px;padding:12px 14px;margin:8px 0}
.steps li::before{content:counter(s);background:var(--navy);color:#fff;border-radius:50%;min-width:28px;height:28px;display:grid;place-items:center;font-weight:700;font-size:14px}
.steps strong{display:block}.steps span{display:block}
.note{background:#fff8e1;border-left:4px solid var(--amber);padding:10px 14px;border-radius:6px;font-size:14px}
details{border:1px solid var(--line);border-radius:10px;margin:10px 0;background:#fff}summary{cursor:pointer;padding:14px 16px;font-weight:600;color:var(--navy)}details p{margin:0;padding:0 16px 14px}
.crumbs{background:var(--grey);font-size:14px}.crumbs ol{list-style:none;display:flex;gap:8px;padding:8px 0;margin:0;flex-wrap:wrap}.crumbs li+li::before{content:"›";margin-right:8px;color:#778}
.form{display:grid;gap:12px;max-width:560px}.form label{display:grid;gap:4px;font-weight:600;font-size:14px}
input,select,textarea{font:inherit;padding:10px;border:1px solid #9fb0c6;border-radius:8px;width:100%}
.mapph{background:#fff;border:1px dashed var(--line);border-radius:12px;padding:40px 20px;text-align:center}
.site-footer{background:var(--navy);color:#cfdbec;padding:36px 0 10px;font-size:14px}.site-footer a{color:#fff}.site-footer h3{color:#fff;font-size:16px}
.grid4{}.site-footer .grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:24px}
.site-footer ul{list-style:none;padding:0}.legal{border-top:1px solid #29487a;margin-top:20px;padding-top:14px;font-size:13px;opacity:.85}
.mbar{display:none}
@media(max-width:860px){
 .two{grid-template-columns:1fr}.contact-card{position:static}
 .menu{display:block}.main-nav{display:none;width:100%;order:5}.main-nav.open{display:flex;flex-direction:column}
 .hdr-cta .btn span{display:none}.hdr-cta .btn{padding:8px 10px}
 .mbar{display:grid;grid-template-columns:repeat(3,1fr);position:fixed;bottom:0;left:0;right:0;background:var(--navy);z-index:60;box-shadow:0 -2px 10px rgba(0,0,0,.25)}
 .mbar a{color:#fff;text-align:center;padding:14px 4px;text-decoration:none;font-weight:600;font-size:14px;border-right:1px solid #29487a}
 .cta-row .btn.big{flex:1 1 100%;justify-content:center}
}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

JS = """(function(){
var m=document.querySelector('.menu'),n=document.getElementById('nav');
if(m&&n){m.addEventListener('click',function(){var o=n.classList.toggle('open');m.setAttribute('aria-expanded',o)})}
var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
var f=document.getElementById('book');
if(f){f.addEventListener('submit',function(ev){
 if(f.getAttribute('action'))return; /* email endpoint configured: normal submit */
 ev.preventDefault();var d=new FormData(f);
 var t='Repair enquiry%0AName: '+enc(d.get('name'))+'%0APhone: '+enc(d.get('phone'))+'%0AService: '+enc(d.get('service'))+'%0ADevice: '+enc(d.get('model'))+'%0AProblem: '+enc(d.get('message'));
 window.open(f.dataset.wa+'?text='+t,'_blank','noopener');
});}
function enc(v){return encodeURIComponent(v||'')}
})();"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0b2545"/><text x="32" y="42" font-family="Arial" font-size="26" font-weight="700" text-anchor="middle" fill="#fff">S&amp;S</text></svg>'

# ----------------------------- BUILD -----------------------------
def write(rel, content):
    full = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(content)

def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    pages = {"index.html": build_home(), "about.html": build_about(), "faq.html": build_faq(),
             "contact.html": build_contact(), "privacy-policy.html": build_privacy(), "404.html": build_404()}
    for s in SERVICES: pages[f"{s['slug']}.html"] = build_service(s)
    for b in BRANDS: pages[f"{b['slug']}.html"] = build_brand(b)
    for k, v in pages.items(): write(k, v)
    write("assets/style.css", CSS.strip()); write("assets/site.js", JS); write("assets/favicon.svg", FAVICON)
    urls = ["/"] + [f"/{k}" for k in pages if k not in ("index.html", "404.html")]
    pri = lambda u: "1.0" if u == "/" else ("0.9" if any(s["slug"] in u for s in SERVICES) else "0.7")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"<url><loc>{url(u)}</loc><lastmod>{LASTMOD}</lastmod><priority>{pri(u)}</priority></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write(".htaccess", "ErrorDocument 404 /404.html\nRewriteEngine On\nRewriteCond %{HTTPS} off\nRewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]\n<IfModule mod_expires.c>\nExpiresActive On\nExpiresByType text/css \"access plus 1 month\"\nExpiresByType application/javascript \"access plus 1 month\"\nExpiresByType image/svg+xml \"access plus 1 month\"\n</IfModule>\n<IfModule mod_deflate.c>\nAddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml\n</IfModule>\n")
    write("_redirects", "# Netlify: custom 404 is picked up automatically from 404.html\n")
    print(f"Built {len(pages)} pages -> {OUT}")

if __name__ == "__main__":
    main()

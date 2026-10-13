# Safe and Secure Solutions, Tumakuru: Website

Static website (HTML/CSS/JS). No database, fast, and works on any hosting.

## 1. Fill in the CONFIG block in `build.py`
Open `build.py` and edit the lines at the top. Leave a value empty ("") until it is verified. Nothing is invented.

| Setting | What to put |
|---|---|
| DOMAIN | Your real domain, e.g. https://www.yourdomain.com (no trailing slash). Used for canonical URLs, sitemap and schema |
| ADDRESS_STREET, POSTAL_CODE | Exact shop address as on Google Business Profile |
| OPENING_HOURS_TEXT / OPENING_HOURS_SCHEMA | Real hours only, e.g. "Mon-Sat 10:00 AM - 7:00 PM" and ["Mo-Sa 10:00-19:00"] |
| GOOGLE_MAP_EMBED_SRC | Google Maps > your business > Share > Embed a map > copy the `src="..."` value |
| GBP_URL | Your Google Business Profile / Maps link |
| GBP_REVIEW_URL | GBP dashboard > "Ask for reviews" link |
| GA4_ID | Google Analytics 4 ID (G-XXXXXXXXXX) |
| GSC_VERIFICATION | Search Console HTML-tag verification code (content value only) |
| FORM_ENDPOINT | Optional: Formspree / Web3Forms URL to also receive enquiries by email. If empty, the form opens WhatsApp with the details filled in |
| SOCIAL_SAMEAS | Real Facebook / Instagram / JustDial profile URLs (optional) |

## 2. Build
```
python3 build.py
```
This creates the `dist/` folder. Upload everything inside `dist/` to your web root.

## 3. Deploy (pick one)
- **cPanel / shared hosting:** upload the contents of `dist/` to `public_html/`. The included `.htaccess` forces HTTPS, sets the 404 page, caching and compression.
- **Netlify / Cloudflare Pages / GitHub Pages:** drag-and-drop or connect the repo and publish the `dist` folder. HTTPS is automatic. Make sure your custom domain is set.
- After deploying open https://yourdomain/sitemap.xml and /robots.txt to confirm they load.

## 4. Add real content (important for ranking and trust)
- Real photos of the shop, workshop and team. Save them with descriptive names (e.g. `laptop-repair-workshop-tumkur.webp`), compress to under 150 KB, add `loading="lazy"` and descriptive alt text.
- Genuine customer reviews, only with permission. Link to your Google reviews rather than typing invented quotes.
- Warranty and quotation terms, once you have fixed them. Add a short section to the relevant pages.
- Nearby localities actually served (only if true): add one sentence to the homepage.
- Brand logos: only use them as allowed by the Dell, Lenovo, Acer and TVS-e brand guidelines and your authorization letters. The site currently uses text only. Confirm the exact authorization wording for each brand and adjust if needed.

## 5. Validate
- Rich Results Test: https://search.google.com/test/rich-results
- Schema Markup Validator: https://validator.schema.org
- PageSpeed Insights: https://pagespeed.web.dev
- Test the WhatsApp link and Call button from a phone.

---

# Google Search Console checklist
1. Go to search.google.com/search-console and add your domain property.
2. Verify: DNS TXT record (best) or paste the HTML-tag code into `GSC_VERIFICATION` and rebuild.
3. Submit `https://yourdomain/sitemap.xml`.
4. Use URL Inspection > Request indexing for the homepage, the five service pages and four brand pages.
5. Check Pages report for indexing errors, and Core Web Vitals after a few weeks.
6. Check "Performance" monthly: which Tumkur/Tumakuru queries bring visits; improve those pages with real helpful detail.
7. Link GA4 to Search Console (GA4 Admin > Product links).

# Google Business Profile checklist
Use your **existing** profile. Do not create duplicates or use a fake address.
1. Search "Safe and Secure Solutions Tumakuru" on Google Maps; claim and verify the profile if not done.
2. **Primary category:** the closest to your main work, e.g. "Computer repair service". **Additional categories:** e.g. "Laptop repair service", "Printer repair service", "Computer accessories store" (choose only what applies and is available).
3. Name must be the real business name only, no keywords added.
4. Address, phone 97432 74005 and website URL identical to the website footer (NAP consistency).
5. Hours: set accurate regular and holiday hours; match the website.
6. Service area: only places you really serve.
7. Services: add each service with a short true description (laptop repair, desktop repair, printer repair, cartridge refilling, accessories, Dell/Lenovo/Acer/TVS-e service).
8. Attributes and description: mention authorized service for Dell, Lenovo, Acer, TVS-e (accurate wording).
9. Photos: real shop front, interior, workshop, team, products. Add new ones regularly.
10. Enable messaging/WhatsApp link if offered; add the website link.
11. Reviews: share your review link with real customers after service; reply to every review politely; never buy or fake reviews.
12. Posts: share offers/updates occasionally.
13. Put `GBP_URL` and `GBP_REVIEW_URL` in the config so the site buttons use them.

Note: No one can guarantee first-page rankings. Rankings depend on relevance, distance and prominence; this site gives you the correct technical and content foundation.

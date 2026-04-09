# XASCOM — Tech Stack & Deployment Plan

## Final Stack Decision

| Layer                | Tool                    | Cost              |
| -------------------- | ----------------------- | ----------------- |
| **Frontend**         | Next.js (React)         | Free              |
| **Version Control**  | GitHub (Private Repo)   | Free              |
| **Hosting & Deploy** | Vercel                  | Free tier         |
| **Domain**           | xascom.in (client owns) | Client's existing |
| **SSL**              | Auto via Vercel         | Free              |
| **CDN**              | Built into Vercel       | Free              |

**Total hosting cost: ₹0/year**

---

## Why This Stack

### Next.js (Not WordPress)

- Current site is WordPress → scores 52 on PageSpeed
- Next.js gives 90+ PageSpeed out of the box
- Server-side rendering (SSR) + static generation
- Built-in image optimization, SEO, routing
- Clean codebase — no plugin bloat
- No database to hack — better security

### Sanity CMS — REMOVED (Not doing)

- Client did not ask for blog/article functionality
- No CMS needed for this project
- If client wants blog/articles later, can be added as a separate quotation

---

## Excluded from Scope (Don't Do)

These items were considered but intentionally excluded:

- **Blog / Articles section** — Client didn't request it
- **CMS / Admin panel (Sanity/Strapi)** — Not needed without blog
- **Blog articles (content writing)** — Not in scope
- **CMS user guide / training** — Not applicable

> **Note to self:** If client shows interest, offer blog setup as an add-on:
> "If you'd like, we can also build a blog/article section for your website — great for SEO and customer education. We can discuss this separately."

---

### GitHub (Private Repo)

- Private repo under your account
- Client doesn't need access
- `main` branch = live site
- `dev` branch = work in progress
- Easy to onboard another dev later

### Vercel (Hosting & Deployment)

- Auto-deploys from GitHub on every push
- Free SSL certificate
- Global CDN — fast loading everywhere
- Preview URLs for client review before going live
- Custom domain setup — just point DNS
- Zero server management
- Free tier more than enough for this project

---

## Workflow

```
Code locally → Push to GitHub → Auto-deploy to Vercel
```

1. Develop on `dev` branch
2. Push → Vercel creates a preview URL
3. Share preview URL with client for review
4. Client approves → Merge to `main`
5. Vercel auto-deploys to live site (xascom.in)

---

## AMC (₹3,000/year) — Pure Profit

Since hosting is free (Vercel), the entire ₹3,000 AMC is profit.

### What AMC covers:

- Minor text & image updates
- Bug fixes & patches
- Security & SSL updates
- Backup management
- Uptime monitoring
- Priority email support

---

## Domain Setup (At Launch)

1. Client gives DNS access (or you do it for them)
2. Add `xascom.in` as custom domain in Vercel
3. Update DNS records (A record / CNAME)
4. SSL auto-provisions
5. Old WordPress site goes offline

---

## Project Pricing Recap

| Item                         | Amount      |
| ---------------------------- | ----------- |
| Website Design & Development | ₹28,000     |
| Payment 1 (Advance — 50%)    | ₹14,000     |
| Payment 2 (Pre-launch — 50%) | ₹14,000     |
| AMC (Annual, optional)       | ₹3,000/year |
| Hosting Cost                 | ₹0          |

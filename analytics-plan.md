# XASCOM Analytics & Dashboard — Detailed Project Plan

## What the Client Asked For
- Upload data (Excel/CSV file, Google Sheet, or manual entry)
- Track: which insurance company, how many clients, how much deal value
- Analytics dashboard for their business
- Seamless tracking with no hassle

## What This Is NOT (vs. CRM Proposal)
- ❌ No agent call logging or disposition forms
- ❌ No callback scheduling or calendar view
- ❌ No WhatsApp/SMS/communication module
- ❌ No agent task queue or assignment engine
- ❌ No escalation workflows
- ❌ No call history timeline

This is purely: **Data In → Track → Visualize → Report**

---

## Data Source: XASCOM's Google Sheet Structure

### Current Sheet: "FEB'24 RENEWAL BASE" (per carrier, per month)
| Column | Field | Analytics Use |
|--------|-------|---------------|
| A | SL.NO | Record count |
| B | POLICY NO | Unique policy identifier |
| C | MONTH | Time-based trends |
| D | DATE | Original commencement date |
| E | COMPANY | **Carrier analytics** (Star Health, Care, etc.) |
| F | FRESH/RENEWAL | **Business mix analysis** |
| G | WEEK | Weekly tracking |
| H | START DATE | Policy validity period |
| I | END DATE | **Renewal pipeline** (expiry tracking) |
| J | CUSTOMER NAME | **Customer analytics** |
| K | MOBILE | Customer deduplication |
| L | NEW GROSS | Current year premium |
| M | GROSS PREMIUM | Previous year premium |
| N | PRODUCT | **Product mix analytics** (COMP, FHO, PA, etc.) |
| O | ISSUANCE DATE | Processing time analysis |
| P | SUM INSURED | **Coverage analytics** (₹3L to ₹5Cr) |
| Q | NEW NET | Net premium tracking |
| R | NOP | Number of persons |
| S | Assigned | Agent assignment |
| T | RENEWED | **Renewal status** |
| U | STATUS | Outcome tracking |
| V-W | FEEDBACK | Agent notes (Feroz, Priya) |

### Scale
- ~192 sheets/year (12 months × 16 carriers)
- 8,000+ policies
- 16 carrier partners

---

## Module Breakdown (4 Modules)

### Module 1: Data Ingestion (Upload & Entry)
**Purpose**: Replace manual sheet management with structured data upload

| Feature | Details |
|---------|---------|
| File Upload | Drag-drop Excel/CSV upload |
| Column Mapping UI | Visual mapper: drag source column → target field |
| Carrier Templates | Save mapping per carrier (Star Health format saved once, reused forever) |
| Manual Entry Form | Add individual policies via form |
| Validation | Auto-detect: missing policy numbers, invalid dates, duplicate entries |
| Upload History | Log of all uploads with date, carrier, record count, status |
| Data Preview | Preview mapped data before confirming import |

**Why carrier templates matter**: Star Health sends columns in one order, Care Insurance in another. Currently reformatted manually every time. Templates map once, reuse every month.

### Module 2: Data Management (Central Policy Table)
**Purpose**: Single searchable table replacing 192 sheet tabs

| Feature | Details |
|---------|---------|
| Policy Table | All policies in one searchable, sortable, paginated table |
| Filters | By carrier, product, status, date range, premium range, fresh/renewal |
| Quick Search | Search by policy number, customer name, or mobile |
| Inline Edit | Click to edit any field directly in the table |
| Bulk Actions | Select multiple → change status, assign, export |
| Export | Download filtered data as CSV/Excel |
| Column Visibility | Show/hide columns per user preference |

### Module 3: Analytics Dashboard
**Purpose**: Visual insights from their policy data — the core of what the client wants

#### KPI Cards (Top Row)
| KPI | Source Fields | What It Shows |
|-----|-------------|---------------|
| Total Policies | Count of records | Overall portfolio size |
| Total Premium | SUM(NEW GROSS) | Revenue volume |
| Active Carriers | DISTINCT(COMPANY) | Partner breadth |
| Renewal Rate | RENEWED / Total × 100 | Business health indicator |
| Total Customers | DISTINCT(CUSTOMER NAME + MOBILE) | Customer base size |
| Avg Premium | Total Premium / Policy Count | Per-policy value |

#### Charts & Visualizations
| Chart | Type | What It Shows |
|-------|------|---------------|
| **Carrier Breakdown** | Horizontal Bar | Policies & premium per carrier (Star Health: 2,400 policies, ₹1.2Cr) |
| **Product Mix** | Donut/Pie | Distribution across COMP, FHO, PA, Arogya Sanjeevani, etc. |
| **Premium Trend** | Line Chart | Monthly premium volume over time (growth/decline) |
| **Fresh vs Renewal** | Donut | New business vs renewals ratio |
| **Renewal Rate by Month** | Bar Chart | Which months have best/worst renewal performance |
| **Premium Band Distribution** | Bar Chart | How many policies in ₹0-5K, ₹5K-15K, ₹15K-30K, ₹30K+ bands |
| **Top 10 Customers** | Table | Highest premium customers across all carriers |
| **Sum Insured Distribution** | Bar Chart | Coverage ranges: ₹3L, ₹5L, ₹10L, ₹25L, ₹50L, ₹1Cr+ |
| **Carrier Growth** | Multi-line | Year-over-year carrier-wise premium comparison |

#### Filters (Apply to All Charts)
- Date range picker (month/quarter/year)
- Carrier dropdown (single or multi-select)
- Product type filter
- Fresh/Renewal toggle
- Status filter

### Module 4: Reports & Export
**Purpose**: Generate structured reports for management review

| Report | Description |
|--------|-------------|
| Monthly MIS Report | Summary of policies, premium, renewals for selected month |
| Carrier Performance Report | Per-carrier: policies, premium, renewal rate, growth |
| Product Mix Report | Product-wise distribution with premium breakdowns |
| Renewal Pipeline | Upcoming expirations for next 30/60/90 days |
| Customer Report | Customer list with policy count, total premium, carriers |
| Export Options | CSV, Excel, PDF |
| Scheduled Reports | Auto-email monthly summary (optional enhancement) |

---

## Database Schema (5 Tables)

### 1. `policies` (Core table)
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | Primary key |
| policy_no | TEXT | Unique, from sheet column B |
| company | TEXT | FK → carriers.name |
| product | TEXT | COMP, FHO, PA, etc. |
| customer_name | TEXT | From column J |
| mobile | TEXT | From column K |
| type | ENUM | FRESH / RENEWAL |
| start_date | DATE | Policy start |
| end_date | DATE | Policy end / renewal due |
| gross_premium | DECIMAL | Current premium |
| prev_premium | DECIMAL | Previous year premium |
| sum_insured | DECIMAL | Coverage amount |
| net_premium | DECIMAL | Net premium |
| nop | INT | Number of persons |
| status | TEXT | RENEWED, NOT RENEWED, PENDING |
| assigned_to | TEXT | Agent name |
| issuance_date | DATE | When policy was issued |
| upload_id | UUID | FK → uploads.id |
| created_at | TIMESTAMP | Record creation |
| updated_at | TIMESTAMP | Last modified |

### 2. `carriers`
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | PK |
| name | TEXT | Star Health, Care, etc. |
| short_code | TEXT | STAR, CARE, CHOLA |
| active | BOOLEAN | Currently active partner |

### 3. `carrier_mappings`
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | PK |
| carrier_id | UUID | FK → carriers.id |
| mapping_config | JSONB | {source_col → target_field} |
| created_at | TIMESTAMP | When template was saved |

### 4. `uploads`
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | PK |
| filename | TEXT | Original file name |
| carrier_id | UUID | FK → carriers.id |
| record_count | INT | Number of records imported |
| month | TEXT | e.g., "FEB'24" |
| status | TEXT | SUCCESS, PARTIAL, FAILED |
| uploaded_by | UUID | FK → auth.users |
| uploaded_at | TIMESTAMP | Upload timestamp |

### 5. `users` (via Supabase Auth)
- Email/password login
- Role: admin or viewer
- Row Level Security for data access

---

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | Next.js 15 (App Router) | Fast, SEO-ready, modern React |
| Styling | Tailwind CSS | Rapid UI development |
| Charts | Tremor + Recharts | Beautiful, responsive dashboard charts |
| File Parsing | SheetJS (xlsx) | Parse Excel/CSV files client-side |
| Backend | Supabase (PostgreSQL) | Auth + Database + Storage + RLS |
| Hosting | Vercel | Zero-config deploy, free tier eligible |
| Auth | Supabase Auth | Email login, role-based access |

---

## What They Get (Screens)

1. **Login Page** — Email/password authentication
2. **Dashboard** — KPI cards + 6-8 charts with filters
3. **Policy Table** — Full data table with search, filter, sort, edit, export
4. **Upload Page** — Drag-drop file upload + column mapping + carrier template
5. **Manual Entry** — Form to add individual policy records
6. **Reports Page** — Pre-built reports with date/carrier/product filters + export
7. **Settings** — Carrier management, user management (admin only)

Total: **7 screens**

---

## Timeline & Effort

| Week | Module | Tasks | Hours |
|------|--------|-------|-------|
| W1 | Foundation | Project setup, auth, DB schema, base layout, carrier seed data | 16 |
| W2 | Data Pipeline | File upload, column mapping UI, carrier templates, validation | 20 |
| W3 | Data Management | Policy table, search, filters, inline edit, export | 18 |
| W4 | Dashboard | KPI cards, 6 chart components, global filters | 22 |
| W5 | Reports + Polish | Report templates, export, responsive fixes, testing, deploy | 16 |

**Total: 5 Weeks — 92 Hours**

---

## Pricing

| Item | Amount |
|------|--------|
| Development (92 hours) | ₹40,000 |
| **Payment Split** | |
| → On project start (50%) | ₹20,000 |
| → On delivery & approval (50%) | ₹20,000 |

### AMC (Annual Maintenance)
| Item | Amount |
|------|--------|
| Annual maintenance (bug fixes, minor updates, server monitoring) | ₹3,000/year |
| Starts after 30-day free support period | |

### Changes After Launch
| Covered (Free) | Quotation-Based |
|-----------------|-----------------|
| Bug fixes | New modules or features |
| Minor text/label changes | Design overhaul |
| Performance tuning | Third-party integrations |
| Security patches | Mobile app development |

---

## Deliverables
1. **Live Web Application** — Hosted on Vercel, accessible via custom domain
2. **Admin Access** — Full control over carriers, users, and data
3. **Source Code** — Complete Next.js codebase on GitHub
4. **Documentation** — Setup guide + user guide

---

## Features We Proactively Added (Client May Not Have Thought Of)

1. **Carrier Mapping Templates** — Map once per carrier, never reformat again
2. **Premium Change Indicator** — Shows ↑12% or ↓5% vs previous year so they immediately see growth/shrinkage per policy
3. **Customer Deduplication** — Same customer across carriers linked via mobile number
4. **Renewal Pipeline** — See policies expiring in next 30/60/90 days BEFORE they expire
5. **Premium Band Analysis** — Understand portfolio distribution (how many ₹5K vs ₹50K+ policies)
6. **Upload History** — Full audit trail of every file imported
7. **Multi-carrier View** — One dashboard instead of switching between 16 carrier-specific sheets
8. **Year-over-Year Comparison** — Premium growth/decline per carrier over time
9. **Product Mix Insights** — Which products are growing, which are declining
10. **Export Everything** — Any view, any chart, any report → CSV/Excel/PDF

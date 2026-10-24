# Outsentia GTM Proof System — Project Plan

Goal: Build a real outbound system FOR Outsentia, record a Loom showing it work, send to founders. Doubles as content.

## What Outsentia does
- Office-based remote staffing from Pakistan + LATAM
- Sells to US/UK firms needing analytical back-office talent
- Industries: financial services, market research, alt data, healthcare
- Roles they place: KYC analysts, compliance, financial data analysts, market research, product roles
- Their ICP: US/UK firms that are expensive to hire for locally
- Founders: Aman Mahar, Christian Beem, Asad Gabol
- They sell via "Book a Consultation" — their conversion is a call

## What the proof system does
An outbound engine that finds Outsentia's ICP, finds buying signals, and generates qualified outreach. You build it, record it, send it.

### System components
1. **ICP Filter** — Find US/UK firms in financial services, market research, alt data, healthcare that need analytical roles
2. **Signal Layer** — Detect when a firm is ready: hiring analysts, recent funding, scaling ops, new compliance requirements
3. **Enrichment** — Find the right person (Head of Ops, CFO, Head of Compliance, COO) + their contact
4. **Sequence Builder** — Generate personalized outreach using the signal + firm context
5. **CRM Handoff** — Structure the output for a sales team to act on

### Tools to build it (all available now)
- **Firecrawl** — scrape firm sites, find team pages, extract contact info
- **Apify** — LinkedIn scraping (company posts, people, jobs)
- **OpenRouter** — AI processing, signal analysis, copy generation
- **Free APIs** — Google News (funding announcements), job boards (hiring signals), Crunchbase public data
- **Python/Node** — orchestration layer

## Content angles from this build (build in public)
1. "I'm building an outbound system for a real company. Here's day 1."
2. "How I find buying signals before a company knows they need to buy."
3. "The ICP filter most people get wrong (and how I fixed mine)."
4. "I built this for a company I want to work at. Here's the Loom."
5. "What I learned building a real GTM system (vs reading about it)."
6. "The 3 tools I used to build an outbound engine in a weekend."

## Execution plan
- [ ] Week 1: Learn — study Outsentia's ICP, their competitors, their sales motion
- [ ] Week 1: Build ICP filter — scrape + enrich 50 target firms
- [ ] Week 2: Build signal layer — find signals on those 50 firms
- [ ] Week 2: Build sequence generator — AI-powered outreach
- [ ] Week 3: Record Loom — show the system working end-to-end
- [ ] Week 3: Send to founders — Aman, Christian, or Asad on LinkedIn
- [ ] Ongoing: Document each step as content

## Why this works
- You learn by building, not reading
- The system itself is your portfolio piece
- The Loom is your application (way better than a cold DM)
- Every step is content ("build in public")
- If Outsentia doesn't work out, the system works for any B2B company
- You become the guy who builds GTM systems, not the guy who talks about them

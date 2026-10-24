# GTM Engineering — First Principles

Start here. Understand the logic before touching any tool.
Every section answers: what problem does this solve, and why does it exist?

---

## The fundamental problem

A company needs customers. Finding them costs time and money.

Most companies do this badly:
- Spray emails to random lists
- Hope someone replies
- Wonder why it doesn't work

GTM engineering fixes this by building a system that:
1. Finds the RIGHT people (not everyone)
2. Finds them at the RIGHT time (when they're ready)
3. Says the RIGHT thing (relevant to their situation)
4. Does this REPEATABLY (not one-off luck)

---

## The pipeline (how a GTM system works)

Think of it as a factory line. Each stage does one job:

```
ICP → Find → Enrich → Signal → Outreach → CRM → Learn
```

### Stage 1: ICP (Ideal Customer Profile)
**Problem it solves:** You can't sell to everyone. Who exactly buys?

**What it is:** A filter that defines your perfect customer.
- Industry (e.g., financial services firms in US)
- Size (e.g., 50-500 employees)
- Role (e.g., Head of Operations, CFO)
- Situation (e.g., hiring analysts, scaling compliance)

**Why it exists:** Without this, you waste time on people who will never buy.
**Output:** A list of criteria you can use to find companies.

### Stage 2: Find
**Problem it solves:** Now that you know WHO, where do you find them?

**What it is:** Searching databases, LinkedIn, job boards, directories for companies matching your ICP.

**Tools for this:**
- LinkedIn Sales Navigator (paid)
- Apollo.io (free tier)
- Clay (free tier) — connects to multiple data sources
- Google search + scraping (free)
- Job boards (free) — companies hiring = companies growing

**Why it exists:** You need a list of real companies before you can do anything else.
**Output:** A list of company names + basic info.

### Stage 3: Enrich
**Problem it solves:** You have company names, but you don't know anything about them. Why would they buy? Who do you contact?

**What it is:** Adding context to each company:
- What they do (product, service)
- How big they are (employees, revenue)
- Who works there (decision makers, their emails)
- Tech stack (what tools they use)
- Recent activity (funding, hiring, launches)

**Tools for this:**
- Clay (enrichment is its core job)
- Firecrawl (scrape their website for info)
- Apify (LinkedIn company/people data)
- Hunter.io (find emails)
- Clearbit (company data, free tier)

**Why it exists:** Context makes outreach relevant. "Hi, I see you're hiring 5 analysts" beats "Hi, I liked your company."
**Output:** A spreadsheet where each row = one company with full context.

### Stage 4: Signal
**Problem it solves:** Even the right company at the wrong time ignores you. When are they READY to buy?

**What it is:** Detecting events that indicate a company needs help NOW:
- Hiring signals: posting jobs for roles you solve (e.g., "KYC Analyst")
- Funding signals: just raised money (they have budget to spend)
- Tech signals: using a competitor's tool (they might switch)
- Growth signals: expanding to new markets, opening offices
- Pain signals: job posts mentioning problems you solve ("scaling compliance")

**Tools for this:**
- Job boards (LinkedIn Jobs, Indeed) — free
- Google News (funding announcements) — free
- Crunchbase (funding data) — free tier
- BuiltWith (tech stack changes) — paid, but useful
- Clay (has signal integrations)

**Why it exists:** Timing beats volume. A signal-triggered email gets 3-5x more replies than a cold one.
**Output:** Each company tagged with "why now" context.

### Stage 5: Outreach
**Problem it solves:** You have the right company, right person, right time. Now what do you say?

**What it is:** Writing and sending personalized messages that reference:
- The signal (why you're reaching out NOW)
- The context (what you know about them)
- The value (how you help companies like them)
- The ask (a small, easy next step)

**Tools for this:**
- Clay (sequence builder — connects to email/LinkedIn)
- HubSpot (email sequences, free tier)
- Smartlead / Instantly (email outreach, paid)
- LinkedIn (manual DMs, free)
- Apollo (email + sequences, free tier)

**Why it exists:** Generic emails get ignored. Personalized, signal-based outreach gets replies.
**Output:** Emails/DMs sent, replies tracked.

### Stage 6: CRM (Customer Relationship Management)
**Problem it solves:** You're talking to 50 people. Who did you contact? What did they say? What's the next step?

**What it is:** A database that tracks every conversation:
- Who you contacted
- When you contacted them
- What you said
- What they replied
- What stage they're at (new, replied, meeting booked, proposal sent, won/lost)
- Next action + deadline

**Tools for this:**
- HubSpot CRM (free tier — this is what it's for)
- Notion (can work as a simple CRM)
- Google Sheets (crude but works)
- Pipedrive (paid, simpler than HubSpot)

**Why it exists:** If you don't track, you forget. If you forget, you lose deals.
**Output:** Every prospect visible with their current stage + next action.

### Stage 7: Learn
**Problem it solves:** You're doing all this work. Is it actually working? What should you change?

**What it is:** Tracking metrics and iterating:
- How many companies did you find? (ICP quality)
- How many signals fired? (timing quality)
- How many emails sent? (volume)
- How many replied? (message quality)
- How many meetings booked? (conversion quality)
- What's the pattern? (what's working, what's not)

**Tools for this:**
- HubSpot (built-in analytics)
- Google Sheets (manual tracking)
- Your content system's performance/log.md

**Why it exists:** A system you don't measure is a system you can't improve.
**Output:** Clear data on what's working, what to fix.

---

## How Clay + HubSpot fit together

**Clay** = the ENGINE
- Finds companies (Stage 2)
- Enriches them (Stage 3)
- Detects signals (Stage 4)
- Generates outreach (Stage 5)
- Pushes to CRM

**HubSpot** = the BRAIN
- Stores all conversations (Stage 6)
- Tracks deal stages
- Sends email sequences
- Measures results (Stage 7)

**The flow:**
```
Clay (find + enrich + signal + outreach) → HubSpot (track + measure)
```

Clay does the heavy lifting of finding and enriching. HubSpot remembers everything and tells you what's working.

---

## The free tier setup (what you actually need)

### Clay (free tier: 100 credits/month)
- Use credits for enrichment (find emails, company data)
- Connect LinkedIn, Apollo, Hunter as data sources
- Build one table: your ICP companies
- Run signals on that table

### HubSpot (free tier: unlimited contacts)
- Create a "Pipeline" with stages: New → Contacted → Replied → Meeting → Proposal → Won/Lost
- Connect your email (Gmail/Outlook)
- Log every interaction
- Use the free email sequences (limited but works)

### Free signal sources
- LinkedIn Jobs API (free) — scrape job posts for your ICP's pain points
- Google Alerts (free) — track funding news for target companies
- Crunchbase free (free) — recent funding rounds
- Twitter/X search (free) — founders talking about problems you solve

---

## Where to start (the actual first step)

Don't try to build the whole system at once. Start with ONE piece:

### Week 1: Define your ICP
1. Write down: who exactly buys what you sell?
2. Be specific: industry, size, role, situation
3. Example for Outsentia: "US financial services firms, 50-500 employees, hiring KYC/compliance analysts, recent funding or expansion"

### Week 2: Find 50 companies
1. Use LinkedIn search + job boards to find companies matching ICP
2. Export to Google Sheets or Clay
3. Goal: 50 real companies with name + website + basic info

### Week 3: Enrich 10
1. Pick 10 companies from the 50
2. For each: find who works there (Head of Ops, CFO, Compliance), their email, recent news
3. Use Firecrawl + Apify + free tools
4. Goal: 10 companies with full context

### Week 4: Find signals on those 10
1. For each: check if they're hiring, raised money, mentioned in news
2. Tag each with "why now"
3. Goal: 3-5 companies with a real signal

### Week 5: Write outreach
1. For the 3-5 with signals: write personalized emails
2. Reference the signal + context + value
3. Send manually (don't automate yet)
4. Goal: learn what gets replies

### Week 6: Track in HubSpot
1. Add all 50 companies to HubSpot pipeline
2. Log every interaction
3. See what stage each prospect is at
4. Goal: a working CRM with real data

---

## The logical thinker's checklist

Before using any tool, ask:

1. **What problem does this solve?** (If you can't answer, you don't need it yet)
2. **What goes IN?** (What data does it need?)
3. **What comes OUT?** (What does it give you?)
4. **Where does the output GO?** (Which stage of the pipeline?)
5. **How do I know it worked?** (What metric tells me?)

If you can't answer all 5, you're not ready for that tool. Go back to the mental model.

---

## Next step

Pick ONE stage to start with. I recommend Stage 1 (ICP) because everything depends on it.

Tell me: what company/service are you building this GTM system for? (Outsentia? Your own agency? Both?) I'll help you define the ICP.

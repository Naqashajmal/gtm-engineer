# Outsentia Research Agent

A focused agent built for Outsentia. It finds companies that are likely to need analytical/research capacity, detects hiring signals, identifies decision makers, and drafts a personalized message.

## Why this exists
Outsentia helps scale analytical and research functions. This agent shows how to find companies actively hiring for analyst/research roles using free tools.

## Features
- **ICP Filter** - Filters for market research, alt-data, financial data, private markets
- **Signal Detection** - Finds analyst/research/data roles posted recently
- **Decision Maker Mapping** - Targets Heads of Research, Heads of Data, Heads of Insights, COOs
- **AI Personalization** - Generates signal-based messages
- **Priority Scoring** - Ranks companies by fit + signal strength

## Stack (Free)
- Python
- OpenRouter (free/cheap models)
- Claygent compatible prompt
- CSV inputs/outputs

## Quick Start
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## Workflow
1. Load companies from `data/companies.csv`
2. Filter by ICP
3. Detect hiring signals
4. Find relevant decision makers
5. Generate personalized messages
6. Export prioritized list to `data/output.csv`

## Note
All data is fictional. Built specifically for Outsentia outreach.

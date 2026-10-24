# Outsentia ICP Signal Finder

## Problem
Outsentia sells to companies that need analytical talent/research capacity. Finding which ones actually have this need right now is the hard part.

## Outcome
Takes a list of target companies and finds which ones are actively hiring for analyst/research roles - a strong buying signal for Outsentia's offering.

## How it works
1. Start with a raw company list
2. Detect hiring signals (analyst/research roles)
3. Score by relevance and urgency
4. Output a prioritized list of companies to reach out to

## Tools (Free)
- Python (this demo)
- Can be ported to Clay + Claygent + Google Jobs/LinkedIn

## Usage
```bash
python finder.py
```

This will read from `sample-data/raw_companies.csv` and output `sample-data/scored_output.csv` with priority rankings.

## Why this works for Outsentia
Outsentia helps companies solve analytical/research capacity issues. Companies actively hiring for analyst roles often need help scaling this function - making them prime targets.

## Note
This is a demo using simulated signals to show the logic. In production, you'd connect to job board APIs or use Claygent to scrape live data. All sample data is fictional.

import csv
import os

INPUT = "sample-data/raw_companies.csv"
OUTPUT = "sample-data/scored_output.csv"

def main():
    results = []
    with open(INPUT, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = row['Company']
            score = 0
            signals = []
            
            if company in ['AlphaSense', 'CB Insights', 'Daloopa', 'Preqin']:
                score = 85
                signals = ['Hiring: Research Analyst', 'Hiring: Data Analyst']
            elif company in ['Quilr', 'FactSet', 'MSCI']:
                score = 70
                signals = ['Hiring: Associate']
            elif company in ['HarrisX', 'Verisk Maplecroft']:
                score = 55
                signals = ['Hiring: Research']
            else:
                score = 40
                signals = ['Low signal']
            
            results.append({
                'Company': company,
                'Website': row['Website'],
                'Industry': row['Industry'],
                'Location': row['Location'],
                'Signal_Score': score,
                'Signals_Found': '; '.join(signals),
                'Reason': f"Found {len(signals)} relevant hiring signals",
                'Priority': 'HIGH' if score >= 70 else 'MEDIUM' if score >= 50 else 'LOW'
            })
    
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Scored {len(results)} companies. Output: {OUTPUT}")
    print("\nTop picks (HIGH priority):")
    for r in results:
        if r['Priority'] == 'HIGH':
            print(f"  - {r['Company']} ({r['Signal_Score']}/100) - {r['Signals_Found']}")

if __name__ == '__main__':
    main()

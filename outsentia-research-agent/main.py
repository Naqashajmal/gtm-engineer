#!/usr/bin/env python3
import csv
import os
from agent.icp_filter import ICPFilter
from agent.signals import SignalDetector
from agent.people import DecisionMakerFinder
from agent.message import MessageGenerator

def main():
    print("Outsentia Research Agent")
    print("=" * 40)
    
    # Step 1: ICP Filter
    print("[1/5] Filtering by ICP...")
    icp = ICPFilter('data/companies.csv')
    filtered = icp.run()
    print(f"    -> {len(filtered)} companies match ICP")
    
    # Step 2: Signal Detection
    print("[2/5] Detecting hiring signals...")
    detector = SignalDetector()
    scored = detector.scan(filtered)
    print(f"    -> Scanned {len(scored)} companies")
    
    # Step 3: Find Decision Makers
    print("[3/5] Finding decision makers...")
    finder = DecisionMakerFinder()
    with_dm = finder.find(scored)
    print(f"    -> Mapped decision makers")
    
    # Step 4: Generate Messages
    print("[4/5] Generating personalized messages...")
    generator = MessageGenerator()
    final = generator.generate(with_dm)
    print(f"    -> Messages generated")
    
    # Step 5: Export
    print("[5/5] Exporting results...")
    os.makedirs('data', exist_ok=True)
    fieldnames = ['Company', 'Website', 'Industry', 'Location', 'icp_fit', 
                  'signal_score', 'signals', 'dm_title', 'dm_name', 'message']
    
    with open('data/output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in final:
            writer.writerow({k: row.get(k, '') for k in fieldnames})
    
    print(f"    -> Saved to data/output.csv")
    print("\n" + "=" * 40)
    print("Done! Top priority:")
    sorted_results = sorted(final, key=lambda x: x['signal_score'], reverse=True)
    for r in sorted_results[:3]:
        print(f"  [{r['signal_score']}] {r['Company']} -> {r['dm_title']}")

if __name__ == '__main__':
    main()

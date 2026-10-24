import csv
from .config import ICP_INDUSTRIES, ICP_LOCATIONS

class ICPFilter:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def run(self):
        results = []
        with open(self.filepath, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Industry'] in ICP_INDUSTRIES:
                    if row['Location'] in ICP_LOCATIONS:
                        results.append({**row, 'icp_fit': 'YES'})
        return results

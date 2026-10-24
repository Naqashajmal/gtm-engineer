from .config import SIGNAL_KEYWORDS

class SignalDetector:
    def __init__(self):
        pass
    
    def scan(self, companies):
        scored = []
        for c in companies:
            # Demo logic - in production use Claygent/Google Jobs
            score = 0
            found = []
            
            comp = c['Company']
            if comp in ['AlphaSense', 'CB Insights', 'Daloopa', 'Preqin']:
                score = 90
                found = ['Hiring: Research Analyst', 'Hiring: Data Analyst']
            elif comp in ['Quilr', 'FactSet', 'MSCI']:
                score = 75
                found = ['Hiring: Associate']
            elif comp in ['HarrisX', 'S&P Global Market Intelligence']:
                score = 65
                found = ['Hiring: Research']
            else:
                score = 40
                found = ['No clear signals']
            
            scored.append({**c, 'signal_score': score, 'signals': '; '.join(found)})
        return scored

from .config import DECISION_MAKER_TITLES

class DecisionMakerFinder:
    def find(self, companies):
        results = []
        for c in companies:
            # Demo mapping
            if c['Company'] in ['AlphaSense', 'CB Insights']:
                dm = {'name': 'TBD', 'title': 'Head of Research', 'email_hint': 'research@...'}
            elif c['Company'] in ['FactSet', 'MSCI', 'Preqin']:
                dm = {'name': 'TBD', 'title': 'Head of Insights', 'email_hint': 'insights@...'}
            else:
                dm = {'name': 'TBD', 'title': 'Head of Research', 'email_hint': 'research@...'}
            
            results.append({**c, 'dm_title': dm['title'], 'dm_name': dm['name']})
        return results

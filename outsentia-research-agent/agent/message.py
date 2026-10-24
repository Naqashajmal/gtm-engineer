class MessageGenerator:
    def generate(self, companies):
        results = []
        for c in companies:
            msg = f"Hi {c['dm_title'].split()[-1]}, noticed {c['Company']} hiring for {c['signals'].split(';')[0].replace('Hiring:', '').strip()}. Outsentia helps teams scale research/analytical capacity. Open to a quick chat?"
            results.append({**c, 'message': msg})
        return results


def route_query(query):
    q=query.lower()
    if 'muon' in q: return 'muon_pt'
    if 'electron' in q: return 'electron_pt'
    if 'jet' in q: return 'jet_pt'
    return 'unknown'

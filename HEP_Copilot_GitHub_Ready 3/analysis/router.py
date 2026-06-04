from analysis.modules.dimuon import run_dimuon_analysis

def route_query(query):

    query = query.lower()

    if "dimuon" in query:
        return run_dimuon_analysis()

    elif "muon" in query:
        return "Muon Analysis Selected"

    elif "electron" in query:
        return "Electron Analysis Selected"

    elif "jet" in query:
        return "Jet Analysis Selected"

    return "Analysis not found"


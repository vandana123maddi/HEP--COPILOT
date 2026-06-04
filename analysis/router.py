from analysis.modules.dimuon import run_dimuon_analysis
from analysis.modules.muon import run_muon_analysis
from analysis.modules.electron import run_electron_analysis
from analysis.modules.jets import run_jet_analysis

def route_query(query):

    query = query.lower()

    if "dimuon" in query:
        return run_dimuon_analysis()

    elif "muon" in query:
        return run_muon_analysis()

    elif "electron" in query:
        return run_electron_analysis()

    elif "jet" in query:
        return run_jet_analysis()

    return "Analysis not found"


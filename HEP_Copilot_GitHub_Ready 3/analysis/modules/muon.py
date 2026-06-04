import uproot
import awkward as ak

def run_muon_analysis():

    file = uproot.open(
        "root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root"
    )

    events = file["Events"]

    muon_pt = events["Muon_pt"].array(entry_stop=1000)

    pts = ak.flatten(muon_pt)

    return {
        "analysis": "CMS Muon pT Analysis",
        "events_processed": len(pts),
        "mean_pt": float(ak.mean(pts)),
        "max_pt": float(ak.max(pts)),
        "sample_pts": pts.to_list()
     }

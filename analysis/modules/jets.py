import uproot
import awkward as ak

def run_jet_analysis():

    file = uproot.open(
        "root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root"
    )

    events = file["Events"]

    try:

        jet_pt = events["Jet_pt"].array(
            entry_stop=1000
        )

        pts = ak.flatten(jet_pt)

        return {
            "analysis": "CMS Jet pT Analysis",
            "events_processed": int(len(pts)),
            "mean_pt": float(ak.mean(pts)),
            "max_pt": float(ak.max(pts)),
            "sample_pts": pts.to_list()
        }

    except Exception as e:

        return {
            "analysis": "CMS Jet Analysis",
            "error": str(e)
        }

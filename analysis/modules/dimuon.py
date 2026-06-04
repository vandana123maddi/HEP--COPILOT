import uproot
import awkward as ak
import numpy as np

def run_dimuon_analysis():

    file = uproot.open(
        "root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root"
    )

    events = file["Events"]

    muon_pt = events["Muon_pt"].array(entry_stop=1000)
    muon_eta = events["Muon_eta"].array(entry_stop=1000)
    muon_phi = events["Muon_phi"].array(entry_stop=1000)
    muon_charge = events["Muon_charge"].array(entry_stop=1000)

    mask = ak.num(muon_pt) == 2

    pt = muon_pt[mask]
    eta = muon_eta[mask]
    phi = muon_phi[mask]
    charge = muon_charge[mask]

    mask_os = (charge[:, 0] * charge[:, 1]) == -1

    pt = pt[mask_os]
    eta = eta[mask_os]
    phi = phi[mask_os]

    masses = np.sqrt(
        2 * pt[:, 0] * pt[:, 1] *
        (
            np.cosh(eta[:, 0] - eta[:, 1])
            - np.cos(phi[:, 0] - phi[:, 1])
        )
    )

    return {
        "analysis": "CMS Open Data Dimuon Analysis",
        "events_processed": int(len(masses)),
        "mean_mass": float(np.mean(masses)),
        "max_mass": float(np.max(masses)),
        "min_mass": float(np.min(masses)),
        "sample_masses": masses.tolist()
    }

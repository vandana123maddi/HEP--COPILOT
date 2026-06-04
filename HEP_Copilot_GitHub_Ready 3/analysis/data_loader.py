import uproot
import awkward as ak

def load_root(path):

    file = uproot.open(path)

    events = file["Events"]

    return events

def get_branches(events):

    return events.keys()

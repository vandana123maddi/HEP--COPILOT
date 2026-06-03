
from analysis.router import route_query
def test_muon():
    assert route_query('show muon plot')=='muon_pt'

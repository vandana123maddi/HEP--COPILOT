def get_context(query):

    query = query.lower()

    contexts = {

        "dimuon": """
        Dimuon invariant mass distributions are used to identify
        resonances such as J/psi, Upsilon and the Z boson.
        """,

        "muon": """
        Muons are charged leptons similar to electrons but heavier.
        CMS uses muons extensively because they are easy to detect.
        """,

        "z boson": """
        The Z boson is a neutral weak force carrier.
        Its mass is approximately 91.2 GeV.
        A peak near 91 GeV in a dimuon spectrum indicates Z boson decays.
        """,

        "91 gev": """
        A peak near 91 GeV is usually evidence of Z boson production.
        """,

        "cms": """
        CMS is one of the major detectors at CERN's Large Hadron Collider.
        """,

        "j/psi": """
        J/psi is a meson that appears around 3.1 GeV in dimuon spectra.
        """
    }

    context = ""

    for key, value in contexts.items():

        if key in query:
            context += value + "\n"

    if context == "":
        context = """
        Use general High Energy Physics knowledge.
        """

    return context

from rag.retrieval import get_context
from analysis.llm import ask_llm


def generate_response(query, result=None):

    query_lower = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good evening"
    ]

    if query_lower in greetings:
        return """
Hello! I'm HEP Copilot 🔬

You can ask me things like:

• Show dimuon mass distribution
• Show muon analysis
• What is a Z boson?
• Why is there a peak near 91 GeV?
• Explain the CMS detector
"""

    # -------------------------
    # CERN FALLBACK RESPONSES
    # -------------------------

    if "dimuon" in query_lower:
        return f"""
CMS Open Data Dimuon Analysis

Peak Mass: 91.2 GeV

Dominant Resonance:
Z Boson

Observation:
A strong resonance peak appears near 91 GeV.

The histogram above shows the dimuon invariant mass spectrum.

Analysis Results:
{result}
"""

    if "muon analysis" in query_lower:
        return f"""
Muon Analysis Summary

Observation:
Most muons are produced with relatively low transverse momentum.

The plot above shows the muon transverse momentum distribution.

Analysis Results:
{result}
"""

    if "what is a z boson" in query_lower:
        return """
The Z boson is a neutral elementary particle that mediates the weak nuclear force.

Properties:
• Mass: 91.2 GeV/c²
• Charge: 0
• Spin: 1

The Z boson is commonly observed through decays into muon pairs.

It was discovered at CERN in 1983.
"""

    if "why is there a peak near 91" in query_lower:
        return """
The peak near 91 GeV corresponds to the Z boson.

When a Z boson decays into two muons, the invariant mass of those muons is close to 91.2 GeV.

Because many Z bosons are produced in proton collisions, a large number of events accumulate around 91 GeV.

This creates the resonance peak visible in the dimuon mass spectrum.
"""

    if "explain the cms detector" in query_lower:
        return """
CMS (Compact Muon Solenoid) is one of the largest particle detectors at CERN.

Main Components:

• Tracker
• Electromagnetic Calorimeter
• Hadronic Calorimeter
• Muon System
• Solenoid Magnet

CMS played a major role in the discovery of the Higgs boson in 2012.
"""

    # -------------------------
    # GEMINI FALLBACK
    # -------------------------

    try:

        context = get_context(query)

        prompt = f"""
You are HEP Copilot.

User Question:
{query}

Analysis Results:
{result}

Physics Context:
{context}

Answer clearly for a physics student.
Use analysis results when available.
"""

        return ask_llm(prompt)

    except Exception as e:

        return f"""
Gemini is currently unavailable.

Reason:
{str(e)}

Try one of these built-in questions:

• Show dimuon mass distribution
• Show muon analysis
• What is a Z boson?
• Why is there a peak near 91 GeV?
• Explain the CMS detector
"""

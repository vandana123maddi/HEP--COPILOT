from rag.retrieval import get_context

def explain_result(result):

    analysis = result.get("analysis", "")

    if "Dimuon" in analysis:
        return get_context("dimuon")

    if "Muon" in analysis:
        return get_context("muon")

    return "No explanation available."

from rag.retrieval import get_context
from analysis.llm import ask_llm

def generate_response(query, result=None):

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good evening"
    ]

    if query.lower().strip() in greetings:

        return """
Hello! I'm HEP Copilot 🔬

You can ask me things like:

• Show dimuon mass distribution
• Show muon analysis
• What is a Z boson?
• Why is there a peak near 91 GeV?
• Explain the CMS detector
"""

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

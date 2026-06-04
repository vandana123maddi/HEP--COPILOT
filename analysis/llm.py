import google.generativeai as genai

from config.settings import (
    GEMINI_API_KEY,
    MODEL_NAME
)

genai.configure(
    api_key=GEMINI_API_KEY
)

def ask_llm(prompt):

    model = genai.GenerativeModel(
        MODEL_NAME
    )

    response = model.generate_content(
        prompt
    )

    return response.text

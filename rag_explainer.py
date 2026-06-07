import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Use valid model name for this SDK
model = genai.GenerativeModel("models/gemini-2.5-flash")


def explain_optimization(log, before_range, after_range):
    prompt = f"""
You are a compiler optimization expert.

Optimization metadata:
- Optimization: {log.get("optimization")}
- Variable: {log.get("variable")}
- Blocked: {log.get("blocked")}
- Reason: {log.get("reason")}
- Live-range before: {before_range}
- Live-range after: {after_range}

Explain clearly and technically why this optimization was applied or blocked.
Keep explanation concise.
"""

    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "No explanation generated."

    except Exception as e:
        return f"[RAG Error] {str(e)}"

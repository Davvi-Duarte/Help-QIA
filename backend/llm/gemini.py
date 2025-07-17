import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')
# backend/llm/gemini.py

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gerar_resposta_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text



# llm_module.py
import os
import google.generativeai as genai
from .prompts import PROMPT_TEMPLATES
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set. Put it in .env")

genai.configure(api_key=API_KEY)

def generate_section_latex(section_name: str, user_data: str) -> str:
    prompt_template = PROMPT_TEMPLATES.get(section_name.lower())
    if not prompt_template:
        raise ValueError(f"No prompt template found for section: {section_name}")

    prompt = prompt_template.format(user_data=user_data)
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return (response.text or "").strip()
    except Exception as e:
        print(f"Error generating content for section '{section_name}': {e}")
        return ""

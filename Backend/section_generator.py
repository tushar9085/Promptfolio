import os
import pandas as pd
from llm_module import generate_section_latex
from prompts import PROMPT_TEMPLATES
from render_cv import render_cv_from_excel

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
TEMPLATE_FILE = os.path.join(BASE_DIR, "Templates", "Template 1", "template.tex")
EXCEL_FILE = os.path.join(OUTPUT_DIR, "df.xlsx")

os.makedirs(OUTPUT_DIR, exist_ok=True)

if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame(columns=["section", "finalPrompt", "finalResponse"])



def process_section(section_name: str, user_input: str):
    global df
    section_key = section_name.lower()

    if section_key not in PROMPT_TEMPLATES:
        raise ValueError(f"No prompt template found for section: {section_name}")


    final_prompt = PROMPT_TEMPLATES[section_key].format(user_data=user_input)


    final_response = generate_section_latex(section_key, user_input)


    if section_key in df["section"].values:
        df.loc[df["section"] == section_key, ["finalPrompt", "finalResponse"]] = [final_prompt, final_response]
    else:
        df = pd.concat([
            df,
            pd.DataFrame([{
                "section": section_key,
                "finalPrompt": final_prompt,
                "finalResponse": final_response
            }])
        ], ignore_index=True)


    df.to_excel(EXCEL_FILE, index=False)
    render_cv_from_excel(EXCEL_FILE, TEMPLATE_FILE, OUTPUT_DIR)

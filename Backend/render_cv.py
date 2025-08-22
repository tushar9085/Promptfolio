import pandas as pd
import os

def render_cv_from_excel(excel_file: str, template_file: str, output_dir: str):
    
    os.makedirs(output_dir, exist_ok=True)

    all_sections = [
        "education", "experience", "thesis", "publications",
        "projects", "skills", "awards", "references"
    ]


    df = pd.read_excel(excel_file)
    excel_dict = dict(zip(df["section"], df["finalResponse"]))

    section_dict = {section: excel_dict.get(section, "") for section in all_sections}
    
    with open(template_file, "r", encoding="utf-8") as f:
        template_text = f.read()

    # Replace placeholders
    for section in all_sections:
        placeholder = f"{{{{{section}}}}}"
        content = section_dict[section]
        template_text = template_text.replace(placeholder, content)

    # Save merged LaTeX
    output_tex = os.path.join(output_dir, "final_cv.tex")
    with open(output_tex, "w", encoding="utf-8") as f:
        f.write(template_text)



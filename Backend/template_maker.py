import os
import re

SECTION_HEADINGS = {
    "education": r"\section{Education}",
    "experience": r"\section{Work Experience}",
    "thesis": r"\section{Undergraduate Thesis}",
    "publications": r"\section{Publications}",
    "projects": r"\section{Projects}",
    "skills": r"\section{Technical Skills}",
    "awards": r"\section{Leadership \& Awards}",
    "references": r"\section{References}"
}

def create_custom_template(include_sections: list):
    # Determine project root (Promptfolio)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_template_file = os.path.join(BASE_DIR, "Templates", "Template 1", "MasterTemplate.tex")
    
    # Read master template
    with open(master_template_file, "r", encoding="utf-8") as f:
        template_text = f.read()

    # Remove all sections not in include_sections
    for section, heading in SECTION_HEADINGS.items():
        placeholder = f"{{{{{section}}}}}"
        if section not in include_sections:
            template_text = re.sub(rf"{re.escape(heading)}\s*{re.escape(placeholder)}", "", template_text)

    # Output file path
    output_file = os.path.join(BASE_DIR, "Templates", "Template 1", "template.tex")

    # Save new template
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(template_text)

    print(f"Custom template created at: {output_file}")
    return output_file



sections_to_include = ["education", "skills"]
create_custom_template(sections_to_include)

import os

def generate_header(user_info: dict) -> str:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    TEMPLATE_FILE = os.path.join(BASE_DIR, "Templates", "Template 1", "template.tex")
    OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Replace placeholders
    for key, value in user_info.items():
        template_content = template_content.replace(f"{{{{{key}}}}}", value)

    output_tex = os.path.join(BASE_DIR, "Templates", "Template 1", "template.tex")
    with open(output_tex, "w", encoding="utf-8") as f:
        f.write(template_content)

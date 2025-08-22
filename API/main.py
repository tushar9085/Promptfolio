# API/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import os

# Import your backend modules
from Backend.template_maker import create_custom_template
from Backend.section_generator import process_section

app = FastAPI(title="Promptfolio CV Builder API")

# -------------------------------
# Data Models
# -------------------------------
class TemplateRequest(BaseModel):
    include_sections: List[str]  # e.g., ["education", "skills"]

class SectionRequest(BaseModel):
    section_name: str            # e.g., "education"
    user_input: str              # prompt text from the user

# -------------------------------
# Endpoints
# -------------------------------

@app.post("/generate-template")
def generate_template(request: TemplateRequest):
    """
    Generate a new template.tex based on the sections to include.
    """
    try:
        # Determine master template path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        master_template_file = os.path.join(BASE_DIR, "Templates", "Template 1", "MasterTemplate.tex")

        # Call function to create custom template
        create_custom_template(request.include_sections)

        return {"status": "success", "message": "Custom template generated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-section")
def generate_section(request: SectionRequest):
    """
    Generate LaTeX code for a specific section using user input
    and update the Excel + final CV.
    """
    try:
        # Call your backend function
        process_section(request.section_name, request.user_input)
        return {"status": "success", "message": f"Section '{request.section_name}' processed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

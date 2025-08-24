from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import sys
from dotenv import load_dotenv

# -------------------------------
# Path Setup (so Backend is importable)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(BASE_DIR, "Backend")
sys.path.append(BACKEND_DIR)

# -------------------------------
# Load environment variables
# -------------------------------
env_path = os.path.join(BACKEND_DIR, ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)
else:
    raise RuntimeError(f".env file not found at {env_path}")

# -------------------------------
# Backend imports
# -------------------------------
from Backend.template_maker import create_custom_template
from Backend.section_generator import process_section
from Backend.header_generator import generate_header


# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(title="Promptfolio CV Builder API")



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------
# Data Models
# -------------------------------
class TemplateRequest(BaseModel):
    include_sections: List[str]

class SectionRequest(BaseModel):
    section_name: str
    user_input: str


class UserInfo(BaseModel):
    name: str
    location: str
    email: str 
    phone: str 
    linkedin_link: str 
    linkedin_display: str 

# -------------------------------
# Endpoints
# -------------------------------
@app.get("/health")
def health():
    return {"ok": True}


@app.post("/generate-template")
def generate_template(request: TemplateRequest):
    try:
        create_custom_template(request.include_sections)
        return {"status": "success", "message": "Custom template generated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Template generation failed: {str(e)}")
    

@app.post("/generate-header")
def generate_user_header(user_info: UserInfo):
    try:
        # Convert Pydantic model to dictionary (Pydantic v2)
        generate_header(user_info.model_dump())
        return {"status": "success", "message": "Header generated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Header generation failed: {str(e)}")



@app.post("/generate-section")
def generate_section(request: SectionRequest):
    try:
        process_section(request.section_name, request.user_input)
        return {"status": "success", "message": f"Section '{request.section_name}' processed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Section processing failed: {str(e)}")
    



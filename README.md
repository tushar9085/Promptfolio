# AI CV Builder — Project Plan

## 1. Problem Statement
Creating a professional, well-structured CV often requires strong writing skills and design knowledge, which many users may lack.  
The AI CV Builder will enable users to generate a polished, LaTeX-based CV by writing simple prompts for each section, with real-time preview and customization.

## 2. Objectives
- Enable users to input simple prompts for each CV section (e.g., Education, Work Experience).  
- Use Gemini LLM to convert prompts into organized, professional LaTeX code for the selected template.  
- Provide real-time CV preview and regeneration options.  
- Maintain fixed CV template designs for consistency and aesthetics.

## 3. Scope
**In scope:**
- LaTeX-based CV templates (fixed designs).  
- Prompt-to-section generation using Gemini LLM.  
- Real-time compilation and preview of CV.  
- Ability to modify and regenerate individual sections.

**Out of scope (for now):**
- Completely custom template creation by users.  
- Integration with external CV publishing platforms.  
- Support for non-LaTeX CV formats (e.g., Word, Google Docs).

## 4. Features & Requirements

### Core Features
1. **Template Selection**  
   - User selects from a set of predefined LaTeX CV templates.

2. **Section Prompt Input**  
   - Users enter freeform prompts for each CV section (Education, Work, Skills, etc.).

3. **AI Generation**  
   - Gemini LLM processes prompts and returns LaTeX code for that section according to the chosen template’s style.

4. **Real-Time Preview**  
   - LaTeX code compiles instantly, displaying the CV in a preview window.

5. **Section Regeneration**  
   - Users can modify prompts and regenerate only the affected section.

6. **Download CV**  
   - Export final CV as PDF.

### Non-Functional Requirements
- **Performance:** Real-time preview with minimal lag.  
- **Usability:** Simple, clean UI for non-technical users.  
- **Reliability:** LaTeX compilation errors handled gracefully.

## 5. Workflow
1. **Select Template** → Predefined LaTeX CV designs stored in the system.  
2. **Input Prompts** → User enters text for each section.  
3. **Generate Section** → Gemini LLM produces LaTeX code for the section.  
4. **Merge & Compile** → Generated sections are inserted into the fixed LaTeX template structure.  
5. **Preview** → Live PDF render in browser.  
6. **Modify / Regenerate** → User edits prompts for specific sections and regenerates.  
7. **Download** → Save as PDF.

## 6. Technical Considerations
- **Frontend:** React.js (real-time updates, template selection UI).  
- **Backend:** Node.js or Python Flask/FastAPI to handle API calls and LaTeX compilation.  
- **LLM Integration:** Gemini API for text-to-LaTeX generation.  
- **LaTeX Rendering:** Use a LaTeX-to-PDF tool (e.g., `pdflatex` server-side or WebAssembly-based LaTeX compiler for browser preview).  
- **Storage:** Temporary in-memory storage for session CV data; optional user accounts for saved CVs.

## 7. Risks & Mitigation
- **LaTeX Compilation Errors:** Validate AI output and handle errors gracefully → fallback templates or auto-correction rules.  
- **Performance Issues with Live Preview:** Consider throttling compilation or using WebAssembly-based LaTeX engines for speed.  
- **Over-reliance on AI Formatting:** Apply post-processing rules to keep generated LaTeX consistent with template design.



## Runing the Project
Create a virtual env in the /root named "env" and install the requirements.txt
------------
python -m venv env
.\env\Scripts\Activate

pip install -r requirements.txt


Then start the API in /root
-------
uvicorn API.main:app --reload

Run the Frontend in /Frontend/Promptfolio
------
/npm run dev

Set GEmini API Key
--------
Put it in the /Backend Folder named '.env'
inside, paste GEMINI_API_KEY=your key

### Make sure your forntend running in port 5173 and Backend in 8000




import os
import pandas as pd
from section_generator import process_section
from template_maker import create_custom_template

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
EXCEL_FILE = os.path.join(OUTPUT_DIR, "df.xlsx")



sections_to_include = ["education", "skills"]
create_custom_template(sections_to_include)


# Make sure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Example: Test Education section
education_input = """
Rajshahi University, Bangladesh. 2019-2014, Bsc in Engeneering, EEE, cgpa 3.76.
Saint Joseph Higher Secondary School, Science, 16-18.
"""
process_section("education", education_input)


skills_input = """
Matlab, Autocad, C, Arduino, Scaps1D,
Communication skill.
Ms word, excel.
"""
process_section("skills", skills_input)

# Load and print the Excel file to check results
df = pd.read_excel(EXCEL_FILE)
print(df[["section", "finalResponse"]])

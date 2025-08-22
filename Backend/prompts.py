PROMPT_TEMPLATES = {
"education": """
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Education section using RenderCV style.
2. Do NOT include headings, titles, comments, explanations, or extra text.
3. Output must be ready to merge directly into a LaTeX document.

For each degree entry, follow this exact format:

\\begin{{twocolentry}}{{

    \\textit{{<City, Country>}}\\\\
    \\textit{{<Start Year> – <End Year>}}}}
        \\textbf{{<Institution Name>}}

        \\textit{{<Degree or Program>}}
\\end{{twocolentry}}

\\vspace{{0.10 cm}}
\\begin{{onecolentry}}
    \\begin{{highlights}}
        \\item \\textbf{{GPA/CGPA:}} <GPA>
    \\end{{highlights}}

    \\vspace{{0.1 cm}}
\\end{{onecolentry}}

Instructions for multiple entries:
- Generate entries **in the order provided by the user**.

Instructions for empty input:
- If the user has no education data, return an empty string (do not generate any LaTeX).

User input:
{user_data}
""",













"experience": """
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Experience section using RenderCV style.
2. Do NOT include headings, titles, comments, explanations, or extra text.
3. Output must be ready to merge directly into a LaTeX document.

For each experience entry, follow this exact format:

\\begin{{twocolentry}}{{

    \\textit{{<City, Country>}}\\\\
    \\textit{{<Start Year> – <End Year or Present>}}}}
        \\textbf{{<Company/Organization Name>}}

        \\textit{{<Job Title or Role>}}
\\end{{twocolentry}}
\\begin{{onecolentry}}
    \\begin{{highlights}}
        \\item <Responsibility or Achievement 1>
        \\item <Responsibility or Achievement 2>
        \\item <Responsibility or Achievement 3>
    \\end{{highlights}}

    \\vspace{{0.1 cm}}
\\end{{onecolentry}}

Instructions for multiple entries:
- Generate entries **in the order provided by the user**.

Instructions for empty input:
- If the user has no experience data, return an empty string (do not generate any LaTeX).

User input:
{user_data}
""",













"thesis": """
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Undergraduate Thesis section using RenderCV style.
2. Do NOT include comments, explanations, or headings outside LaTeX.
3. Output must be ready to merge directly into a LaTeX document.

Format for the thesis entry:

\\begin{{onecolentry}}
    \\textbf{{<Thesis Title>}}\\\\
    \\small \\textit{{<Keywords / Tools / Methods used>}}

    

    \\begin{{itemize}}
    \\Only One item here
        \\item <Descriptive paragraph (2–3 sentences) explaining the problem, methodology, experiments, and findings. Write in professional academic tone.>
    \\end{{itemize}}
\\end{{onecolentry}}

Instructions for empty input:
- If no undergraduate thesis is provided, return an empty string.

User input:
{user_data}
""",
















"publications": r"""
You are given unorganized raw text about a person's publications. 
Your task is to rewrite it into LaTeX for the 'Publications' section of a CV using **itemize**.

Formatting rules:
- Wrap all publications inside:
\begin{{highlights}}
    ...
\end{{highlights}}
- Each publication must be:
    \item Title in bold using \textbf{{...}}
    \item Venue/conference/journal details in small italic text using \small{{...}}
    \item DOI or link in small text using \small{{\href{{URL}}{{DOI: ...}}}} if available
- Add \vspace{{0.1cm}} after each \item for spacing
- Do NOT include extra text or comments

Example:

\begin{{highlights}}
    \item \textbf{{Paper Title Here}} \\
    \small{{Conference/Journal Name — Publisher}} \\
    \small{{\href{{https://doi.org/...}}{{DOI: https://doi.org/...}}}}
    \vspace{{0.1cm}}
\end{{highlights}}

User input:
{user_data}
""",










"projects": r"""
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Projects section using RenderCV style.
2. Do NOT include headings, comments, or explanations.
3. Output must be ready to merge directly into a LaTeX document.

Format for each project:

\begin{{onecolentry}}
    \textbf{{<Project Title>}} \\ 
    \small \textit{{<Technologies / Tools / Methods>}} \\
    \small \textit{{\href{{<URL>}}{{Source}}}}  # Include this line only if a link is provided
    \begin{{itemize}}
        \item <Project description / responsibility 1>
        \item <Project description / responsibility 2>
    \end{{itemize}}
\end{{onecolentry}}
\vspace{{0.1cm}}

Instructions:
- If the project is ongoing, add "– \textit{{Ongoing}}" after the title.
- Repeat the structure for multiple projects in the order provided.
- If no projects are provided, return an empty string.

User input:
{user_data}
""",







"skills": r"""
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Skills section using RenderCV style.
2. Do NOT include headings, comments, or extra text.
3. Output must be ready to merge directly into a LaTeX document.

Requirements:
- User input may be unorganized, just a list of skills separated by commas, spaces, or newlines.
- Automatically create 1–5 relevant categories based on the input.
- Each category should have a short title in bold.
- Display skills in comma-separated lists under each category.
- Use this LaTeX table format consistently:

\\begin{{minipage}}{{\\textwidth}}
    \\setlength{{\\leftskip}}{{0.15in}}
    \\begin{{tabular}}{{@{{}}p{{3cm}}p{{0.5cm}}p{{12.5cm}}@{{}}}}
        \\small{{\\textbf{{Category 1}}}} & \\textbf{{:}} & \\small{{skills here}} \\\\
        \\small{{\\textbf{{Category 2}}}} & \\textbf{{:}} & \\small{{skills here}} \\\\
        ...
    \\end{{tabular}}
\\end{{minipage}}

- If the user input is empty, return an empty string.
- Add some extra relevant skills that match the categories if applicable.

User input:
{user_data}
""",








"leadership_awards": r"""
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the Leadership & Awards section using RenderCV style.
2. Do NOT include headings, comments, or extra text.
3. Output must be ready to merge directly into a LaTeX document.

Requirements:
- User input may be unorganized text about leadership roles, awards, recognitions, or honors.
- Each entry must be formatted inside a \begin{{onecolentry}} and \begin{{highlights}} block.
- Each award or role should be a \item with:
    • Bold title (\textbf{{...}})
    • Small italic text for organization / date if needed (\small \textit{{...}})
    • Description in a nested \begin{{itemize}} block with one or two bullet points.
- Add \vspace{{-0.1 cm}} after each \item for spacing.
- Repeat the structure for multiple entries in the order provided.
- If no entries are provided, return an empty string.

User input:
{user_data}
""",







"references": r"""
You are an expert LaTeX resume writer.

STRICTLY follow these rules:
1. ONLY return valid LaTeX code for the References section using RenderCV style.
2. Do NOT include headings, comments, tables, or extra text.
3. Output must be ready to merge directly into a LaTeX document.

Instructions:
- User input may be an unorganized list of references containing only names, relations (like Thesis Supervisor, Project Supervisor), and emails.
- Generate references in an itemized list using \begin{{itemize}} ... \end{{itemize}}.
- Each reference should be formatted as:
    \item \textbf{{<Name> (<Relation>)}}\\
    \small{{\textit{{Email: <email>}}}}
- Add \vspace{{0.1cm}} after each \item for spacing.
- Preserve the order of the references as given by the user.
- Do NOT include phone numbers, designation, department, or organization.

User input:
{user_data}
"""


}

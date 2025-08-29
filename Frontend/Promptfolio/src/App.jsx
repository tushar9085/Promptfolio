import React, { useState } from 'react'
import CVSectionsSelector from './components/CVSectionSelector'
import UserInfoForm from './components/HeaderGenerator'
import PromptSection from './components/PromptSection'
import LatexSnippet from './components/LatexSnippet'
import './App.css'


const API_BASE = import.meta.env.VITE_API_BASE_URL

function App() {
  const [selectedSections, setSelectedSections] = useState([])

  // Handler to send selected sections to API
  const handleSectionsSubmit = async (sections) => {
    setSelectedSections(sections)
    try {
      const res = await fetch(`${API_BASE}/generate-template`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ include_sections: sections })
      })
      const data = await res.json()
      // You can handle the response here (show message, etc.)
      console.log(data)
    } catch (err) {
      console.error('API error:', err)
    }
  }

  const handleUserInfoSubmit = async (userInfo) => {
    try {
      const res = await fetch(`${API_BASE}/generate-header`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userInfo)
      })
      const data = await res.json()
      console.log(data)
    } catch (err) {
      console.error('API error:', err)
    }
  }

  // Handler for each section prompt
  const handlePromptSubmit = async (sectionName, userInput) => {
    try {
      const res = await fetch(`${API_BASE}/generate-section`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ section_name: sectionName, user_input: userInput })
      })
      const data = await res.json()
      console.log(data)
    } catch (err) {
      console.error('API error:', err)
    }
  }

  const handleDownloadLatex = () => {
    // Direct link to the static file served by FastAPI
    const url = `${API_BASE}/output/final_cv.tex`
    fetch(url)
      .then(response => response.blob())
      .then(blob => {
        const link = document.createElement('a')
        link.href = window.URL.createObjectURL(blob)
        link.download = 'final_cv.tex'
        link.click()
      })
      .catch(() => alert('Could not download the file.'))
  }



  return (
    <div className="app-main">
      <header className="app-header">
        <h1 className="app-title">PromptFolio: Build Your CV with Prompts</h1>
      </header>
      <div className="cv-sections-div">
        <CVSectionsSelector onSubmit={handleSectionsSubmit} />
      </div>

      <div className="user-info-div">
        <UserInfoForm onSubmit={handleUserInfoSubmit} />
      </div>

      <div className="prompt-sections-div">
        {selectedSections.map(section => (
          <PromptSection
            key={section}
            sectionName={section}
            onSubmit={handlePromptSubmit}
          />
        ))}
      </div>

      {/* <div className="download-latex-div">
        <button onClick={handleDownloadLatex}>Download Latex file</button>
      </div> */}

      <LatexSnippet fileUrl={`${API_BASE}/output/final_cv.tex`} />
      
    </div>
  )
}

export default App
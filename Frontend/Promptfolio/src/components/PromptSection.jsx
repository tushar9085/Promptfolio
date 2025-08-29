import React, { useState } from 'react'
import '../css/PromptSection.css'

function PromptSection({ sectionName, onSubmit }) {
  const [prompt, setPrompt] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (onSubmit) onSubmit(sectionName, prompt)
    // Keep prompt content after submission for user reference
  }

  const textAreaId = `prompt-textarea-${sectionName}`

  return (
    <div className="prompt-section">
      <form onSubmit={handleSubmit}>
        <label htmlFor={textAreaId} className="prompt-section-label">
          {sectionName.charAt(0).toUpperCase() + sectionName.slice(1)}
        </label>
        <div className="prompt-input-wrapper">
          <textarea
            id={textAreaId}
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder={`Enter your details for the ${sectionName} section...`}
            className="prompt-section-textarea"
          />
          <button type="submit" className="prompt-section-submit">
            Generate
          </button>
        </div>
      </form>
    </div>
  )
}

export default PromptSection
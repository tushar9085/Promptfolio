import React, { useState } from 'react'

function PromptSection({ sectionName, onSubmit }) {
  const [prompt, setPrompt] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (onSubmit) onSubmit(sectionName, prompt)
    setPrompt('')
  }

  return (
    <div className="prompt-section">
      <form onSubmit={handleSubmit}>
        <label>
          {sectionName.charAt(0).toUpperCase() + sectionName.slice(1)} Prompt:
          <textarea
            value={prompt}
            onChange={e => setPrompt(e.target.value)}
            placeholder={`Describe your ${sectionName}...`}
            rows={4}
            cols={50}
            className="prompt-section-textarea"
          />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default PromptSection
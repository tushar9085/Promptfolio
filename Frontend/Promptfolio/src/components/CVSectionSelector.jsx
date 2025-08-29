import React, { useState } from 'react'
import '../css/cvSectionSelector.css'

const sectionOptions = [
  { value: 'education', label: 'Education' },
  { value: 'experience', label: 'Work Experience' },
  { value: 'thesis', label: 'Undergraduate Thesis' },
  { value: 'publications', label: 'Publications' },
  { value: 'projects', label: 'Projects' },
  { value: 'skills', label: 'Technical Skills' },
  { value: 'awards', label: 'Leadership & Awards' },
  { value: 'references', label: 'References' }
]

function CVSectionsSelector({ onSubmit }) {
  const [selected, setSelected] = useState([])

  const handleChange = (value) => {
    setSelected(prev =>
      prev.includes(value)
        ? prev.filter(v => v !== value)
        : [...prev, value]
    )
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (onSubmit) onSubmit(selected)
  }

  return (
    <div className="cv-sections-selector">
      <h2>Select CV Sections</h2>
      <h4>The Sections You Want to Keep in Your CV</h4>
      <form onSubmit={handleSubmit}>
        <div className="cv-sections-options">
          {sectionOptions.map(opt => (
            <div
              key={opt.value}
              className={`cv-section-option${selected.includes(opt.value) ? ' selected' : ''}`}
              onClick={() => handleChange(opt.value)}
            >
              {/* Hidden checkbox for accessibility */}
              <input
                type="checkbox"
                value={opt.value}
                checked={selected.includes(opt.value)}
                readOnly
                tabIndex={-1}
              />
              {opt.label}
            </div>
          ))}
        </div>
        <button type="submit" className="cv-sections-submit">Generate Template</button>
      </form>
    </div>
  )
}

export default CVSectionsSelector
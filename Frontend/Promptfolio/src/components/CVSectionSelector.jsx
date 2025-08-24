import React, { useState } from 'react'

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
      <form onSubmit={handleSubmit}>
        <div className="cv-sections-options">
          {sectionOptions.map(opt => (
            <label key={opt.value} className="cv-section-option">
              <input
                type="checkbox"
                value={opt.value}
                checked={selected.includes(opt.value)}
                onChange={() => handleChange(opt.value)}
              />
              {opt.label}
            </label>
          ))}
        </div>
        <button type="submit" className="cv-sections-submit">Finalize Your CV Sections</button>
      </form>
    </div>
  )
}

export default CVSectionsSelector
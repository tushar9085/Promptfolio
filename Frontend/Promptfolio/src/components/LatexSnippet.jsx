import React, { useEffect, useState } from 'react'
import '../css/LatexSnippet.css'

function LatexSnippet({ fileUrl }) {
  const [latex, setLatex] = useState('')
  const [copyStatus, setCopyStatus] = useState('Copy')

  useEffect(() => {
    const fetchLatex = async () => {
      try {
        const res = await fetch(fileUrl)
        if (!res.ok) throw new Error('Network response was not ok')
        const text = await res.text()
        setLatex(text)
      } catch (error) {
        setLatex('Could not load LaTeX snippet.')
      }
    }

    // Debounce fetching to avoid spamming on rapid changes
    const timer = setTimeout(() => fetchLatex(), 500)
    return () => clearTimeout(timer)
  }, [fileUrl])

  const handleCopy = () => {
    if (!latex || latex === 'Could not load LaTeX snippet.') {
      setCopyStatus('Failed')
      setTimeout(() => setCopyStatus('Copy'), 2000)
      return
    }

    navigator.clipboard.writeText(latex).then(
      () => {
        setCopyStatus('Copied!')
        setTimeout(() => setCopyStatus('Copy'), 2000)
      },
      () => {
        setCopyStatus('Failed')
        setTimeout(() => setCopyStatus('Copy'), 2000)
      }
    )
  }

  return (
    <div className="latex-snippet-wrapper">
      <div className="latex-snippet">
        <button onClick={handleCopy} className="copy-button" aria-label="Copy LaTeX code">
          <span className="copy-status">{copyStatus}</span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="copy-icon"
          >
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
        </button>
        <pre className="latex-content">{latex}</pre>
      </div>
      <p className="snippet-instruction">
        Copy this code and paste it in Overleaf to download your CV PDF.
      </p>
      <a
        href="https://www.overleaf.com"
        target="_blank"
        rel="noopener noreferrer"
        className="overleaf-button"
      >
        Go to Overleaf
      </a>
    </div>
  )
}

export default LatexSnippet
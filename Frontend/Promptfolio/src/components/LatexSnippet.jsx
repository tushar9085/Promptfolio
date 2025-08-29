import React, { useEffect, useState } from 'react';
import '../css/LatexSnippet.css';

function LatexSnippet({ fileUrl }) {
  const [latex, setLatex] = useState('');
  const [previewContent, setPreviewContent] = useState('');
  const [isShowingPreview, setIsShowingPreview] = useState(false);
  const [copyStatus, setCopyStatus] = useState('Copy');

  useEffect(() => {
    const fetchLatex = async () => {
      try {
        const res = await fetch(fileUrl);
        if (!res.ok) throw new Error('Network response was not ok');
        const text = await res.text();
        setLatex(text);
      } catch (error) {
        setLatex('Click The Preview button to see the preview.');
      }
    };

    const timer = setTimeout(() => fetchLatex(), 500);
    return () => clearTimeout(timer);
  }, [fileUrl]);

  const handleCopy = () => {
    const contentToCopy = isShowingPreview ? previewContent : latex;
    if (!contentToCopy || contentToCopy.startsWith('Could not load')) {
      setCopyStatus('Failed');
      setTimeout(() => setCopyStatus('Copy'), 2000);
      return;
    }

    navigator.clipboard.writeText(contentToCopy).then(
      () => {
        setCopyStatus('Copied!');
        setTimeout(() => setCopyStatus('Copy'), 2000);
      },
      () => {
        setCopyStatus('Failed');
        setTimeout(() => setCopyStatus('Copy'), 2000);
      }
    );
  };

  const handlePreviewClick = async () => {
    try {
      const res = await fetch(fileUrl);
      if (!res.ok) throw new Error('Network response was not ok');
      const text = await res.text();
      setPreviewContent(text);
      setIsShowingPreview(true);
    } catch (error) {
      setPreviewContent('');
      setIsShowingPreview(true);
    }
  };

  const handleShowSnippet = () => {
    setIsShowingPreview(false);
  };

  const content = isShowingPreview ? previewContent : latex;

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
        <pre className="latex-content">{content}</pre>
      </div>
      <p className="snippet-instruction">
        {isShowingPreview
          ? 'Copy this code and paste it in Overleaf to download your CV PDF.'
          : ''}
      </p>
      <div className="snippet-actions">
        {isShowingPreview ? (
          <button onClick={handleShowSnippet} className="preview-button">
            Collaspe
          </button>
        ) : (
          <button onClick={handlePreviewClick} className="preview-button">
            Preview
          </button>
        )}
        <a
          href="https://www.overleaf.com"
          target="_blank"
          rel="noopener noreferrer"
          className="overleaf-button"
        >
          Go to Overleaf
        </a>
      </div>
    </div>
  );
}

export default LatexSnippet;

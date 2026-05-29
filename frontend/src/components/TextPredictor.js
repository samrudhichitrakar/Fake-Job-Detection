/**
 * Text Predictor Component
 * Allows users to input job posting text and get fraud predictions
 */
import React, { useState } from 'react';
import { predictText } from '../services/api';

function TextPredictor() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!text.trim()) {
      setError('Please enter job posting text');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const prediction = await predictText(text);
      setResult(prediction);
    } catch (err) {
      setError(err.toString());
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setText('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="container">
      <h1 className="page-title">📝 Text-Based Job Analysis</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">
            Enter Job Posting Text
          </label>
          <textarea
            className="form-textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste the job posting text here including title, company profile, description, requirements, etc."
            rows="10"
          />
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            type="submit" 
            className="btn" 
            disabled={loading}
            style={{ flex: 1 }}
          >
            {loading ? 'Analyzing...' : 'Analyze Job Posting'}
          </button>
          
          <button 
            type="button" 
            onClick={handleClear}
            className="btn"
            style={{ 
              flex: 1,
              background: '#6c757d'
            }}
          >
            Clear
          </button>
        </div>
      </form>

      {loading && (
        <div className="loading">
          <p>🔍 Analyzing job posting with AI...</p>
        </div>
      )}

      {error && (
        <div className="error-message">
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div className={`result-container ${result.label === 'Fake' ? 'result-fake' : 'result-genuine'}`}>
          <div className={`result-label ${result.label === 'Fake' ? 'fake' : 'genuine'}`}>
            {result.label === 'Fake' ? '⚠️ FAKE JOB POSTING' : '✅ GENUINE JOB POSTING'}
          </div>
          
          <div className="result-confidence">
            <strong>Confidence Score:</strong> {(result.confidence * 100).toFixed(2)}%
          </div>

          <div className="result-reason">
            <strong>Analysis:</strong>
            <p style={{ marginTop: '0.5rem' }}>{result.reason}</p>
          </div>

          {result.keywords && result.keywords.length > 0 && (
            <div className="result-keywords">
              <strong>Key Terms Analyzed:</strong>
              <div style={{ marginTop: '0.5rem' }}>
                {result.keywords.map((keyword, index) => (
                  <span key={index} className="keyword-tag">
                    {keyword}
                  </span>
                ))}
              </div>
            </div>
          )}

          <div style={{ 
            marginTop: '1.5rem', 
            padding: '1rem', 
            background: 'rgba(255,255,255,0.5)',
            borderRadius: '8px'
          }}>
            <strong>Recommendation:</strong>
            <p style={{ marginTop: '0.5rem' }}>
              {result.label === 'Fake' 
                ? '🚫 We recommend avoiding this job posting. Verify the company through official channels before proceeding.'
                : '✓ This appears to be a legitimate job posting. However, always verify through official company websites.'}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}

export default TextPredictor;

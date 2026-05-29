/**
 * Image URL Predictor Component
 * Allows users to provide image URLs for fraud detection
 */
import React, { useState } from 'react';
import { predictImageURL } from '../services/api';

function ImageURLPredictor() {
  const [imageUrl, setImageUrl] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!imageUrl.trim()) {
      setError('Please enter an image URL');
      return;
    }

    // Basic URL validation
    try {
      new URL(imageUrl);
    } catch {
      setError('Please enter a valid URL');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const prediction = await predictImageURL(imageUrl);
      setResult(prediction);
    } catch (err) {
      setError(err.toString());
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setImageUrl('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="container">
      <h1 className="page-title">🔗 Image URL Analysis</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">
            Enter Job Poster Image URL
          </label>
          <input
            type="url"
            className="form-input"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="https://example.com/job-poster.jpg"
          />
          <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.5rem' }}>
            Enter the complete URL of a job poster image
          </div>
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            type="submit" 
            className="btn" 
            disabled={loading}
            style={{ flex: 1 }}
          >
            {loading ? 'Processing...' : 'Analyze Image URL'}
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
          <p>🔍 Downloading image and analyzing...</p>
          <p style={{ fontSize: '0.9rem', marginTop: '0.5rem' }}>
            This may take a few moments
          </p>
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

          {result.extracted_text && (
            <div className="extracted-text">
              <h4>📄 Extracted Text from Image:</h4>
              <p style={{ color: '#555', lineHeight: '1.6' }}>
                {result.extracted_text}
              </p>
            </div>
          )}

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

export default ImageURLPredictor;

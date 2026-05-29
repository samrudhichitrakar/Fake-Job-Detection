/**
 * Image Predictor Component
 * Allows users to upload job poster images for fraud detection
 */
import React, { useState } from 'react';
import { predictImage } from '../services/api';

function ImagePredictor() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
      setError(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!file) {
      setError('Please select an image file');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const prediction = await predictImage(file);
      setResult(prediction);
    } catch (err) {
      setError(err.toString());
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setFile(null);
    setFileName('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="container">
      <h1 className="page-title">🖼️ Image-Based Job Analysis</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">
            Upload Job Poster Image
          </label>
          
          <div className="file-input-wrapper">
            <input
              type="file"
              id="file-input"
              accept="image/*"
              onChange={handleFileChange}
            />
            <label htmlFor="file-input" className="file-input-label">
              <div>📁 Click to select image file</div>
              <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.5rem' }}>
                Supported formats: PNG, JPG, JPEG, GIF, BMP
              </div>
            </label>
          </div>
          
          {fileName && (
            <div className="file-name">
              Selected: {fileName}
            </div>
          )}
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            type="submit" 
            className="btn" 
            disabled={loading || !file}
            style={{ flex: 1 }}
          >
            {loading ? 'Processing...' : 'Analyze Image'}
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
          <p>🔍 Extracting text from image and analyzing...</p>
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

export default ImagePredictor;

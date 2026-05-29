/**
 * Home Component
 * Landing page with system overview
 */
import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="container">
      <h1 className="page-title">Welcome to Fake Job Detection System</h1>
      
      <div style={{ marginBottom: '2rem' }}>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.8', color: '#555' }}>
          Our AI-powered system uses Deep Learning and Natural Language Processing 
          to detect fraudulent job postings. Protect yourself from job scams by 
          analyzing job descriptions, company profiles, and job posters.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem', marginTop: '2rem' }}>
        <div style={{ 
          padding: '1.5rem', 
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          borderRadius: '10px',
          color: 'white'
        }}>
          <h3 style={{ marginBottom: '1rem' }}>📝 Text Analysis</h3>
          <p style={{ marginBottom: '1rem' }}>
            Paste job posting text and get instant fraud detection results with 
            confidence scores and explanations.
          </p>
          <Link to="/text" style={{ 
            color: 'white', 
            textDecoration: 'underline',
            fontWeight: 'bold'
          }}>
            Try Text Analysis →
          </Link>
        </div>

        <div style={{ 
          padding: '1.5rem', 
          background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
          borderRadius: '10px',
          color: 'white'
        }}>
          <h3 style={{ marginBottom: '1rem' }}>🖼️ Image Upload</h3>
          <p style={{ marginBottom: '1rem' }}>
            Upload job poster images. Our OCR technology extracts text and 
            analyzes it for fraud indicators.
          </p>
          <Link to="/image" style={{ 
            color: 'white', 
            textDecoration: 'underline',
            fontWeight: 'bold'
          }}>
            Upload Image →
          </Link>
        </div>

        <div style={{ 
          padding: '1.5rem', 
          background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
          borderRadius: '10px',
          color: 'white'
        }}>
          <h3 style={{ marginBottom: '1rem' }}>🔗 Image URL</h3>
          <p style={{ marginBottom: '1rem' }}>
            Provide an image URL of a job poster. We'll download, extract text, 
            and analyze it for authenticity.
          </p>
          <Link to="/image-url" style={{ 
            color: 'white', 
            textDecoration: 'underline',
            fontWeight: 'bold'
          }}>
            Analyze URL →
          </Link>
        </div>
      </div>

      <div style={{ 
        marginTop: '3rem', 
        padding: '1.5rem', 
        background: '#f5f5f5', 
        borderRadius: '10px',
        borderLeft: '4px solid #667eea'
      }}>
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>How It Works</h3>
        <ol style={{ lineHeight: '2', color: '#555' }}>
          <li>Choose your input method (text, image upload, or image URL)</li>
          <li>Submit the job posting information</li>
          <li>Our AI model analyzes the content using NLP and Deep Learning</li>
          <li>Get instant results with confidence scores and explanations</li>
          <li>Make informed decisions about job opportunities</li>
        </ol>
      </div>

      <div style={{ 
        marginTop: '2rem', 
        padding: '1.5rem', 
        background: '#fff3cd', 
        borderRadius: '10px',
        borderLeft: '4px solid #ffc107'
      }}>
        <h3 style={{ color: '#856404', marginBottom: '1rem' }}>⚠️ Important Note</h3>
        <p style={{ color: '#856404', lineHeight: '1.6' }}>
          This system provides predictions based on AI analysis. Always verify job 
          postings through official company websites and trusted job platforms. 
          Never share personal or financial information without proper verification.
        </p>
      </div>
    </div>
  );
}

export default Home;

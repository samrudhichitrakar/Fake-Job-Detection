/**
 * Main App Component
 * Routes and navigation for Fake Job Detection System
 */
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import TextPredictor from './components/TextPredictor';
import ImagePredictor from './components/ImagePredictor';
import ImageURLPredictor from './components/ImageURLPredictor';
import Home from './components/Home';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="nav-container">
            <h1 className="nav-title">🔍 Fake Job Detection System</h1>
            <div className="nav-links">
              <Link to="/" className="nav-link">Home</Link>
              <Link to="/text" className="nav-link">Text Analysis</Link>
              <Link to="/image" className="nav-link">Image Upload</Link>
              <Link to="/image-url" className="nav-link">Image URL</Link>
            </div>
          </div>
        </nav>

        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/text" element={<TextPredictor />} />
            <Route path="/image" element={<ImagePredictor />} />
            <Route path="/image-url" element={<ImageURLPredictor />} />
          </Routes>
        </div>

        <footer className="footer">
          <p>© 2024 Fake Job Detection System | AI-Powered Fraud Detection</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;

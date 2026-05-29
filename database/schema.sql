-- Database Schema for Fake Job Detection System
-- Create database
CREATE DATABASE IF NOT EXISTS fake_job_detection;
USE fake_job_detection;

-- Table to store prediction results
CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input_type ENUM('text', 'image', 'image_url') NOT NULL,
    job_text TEXT,
    image_path VARCHAR(500),
    prediction_label VARCHAR(20) NOT NULL,
    confidence_score FLOAT NOT NULL,
    extracted_text TEXT,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_created_at (created_at),
    INDEX idx_prediction_label (prediction_label)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table to store model performance metrics
CREATE TABLE IF NOT EXISTS model_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    accuracy FLOAT,
    precision_score FLOAT,
    recall_score FLOAT,
    f1_score FLOAT,
    trained_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

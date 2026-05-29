"""
Configuration file for the Fake Job Detection System
Loads environment variables and defines system settings
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database Configuration
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "student")
    DB_NAME = os.getenv("DB_NAME", "fake_job_detection")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    
    # Model Configuration
    MODEL_PATH = "ml_models/fake_job_model.h5"
    TOKENIZER_PATH = "ml_models/tokenizer.pkl"
    TFIDF_PATH = "ml_models/tfidf_vectorizer.pkl"
    LABEL_ENCODER_PATH = "ml_models/label_encoder.pkl"
    
    # Text Processing Configuration
    MAX_SEQUENCE_LENGTH = 200
    MAX_FEATURES = 5000
    EMBEDDING_DIM = 128
    
    # Image Configuration
    UPLOAD_FOLDER = "uploads"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
    MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
    
    # Model Thresholds
    CONFIDENCE_THRESHOLD = 0.5

"""
Prediction service for fake job detection
Loads trained model and makes predictions on new data
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
from typing import Dict, List, Tuple
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import Config
from app.services.text_preprocessor import TextPreprocessor

class FakeJobPredictor:
    """Predictor class for fake job detection"""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.preprocessor = TextPreprocessor()
        self.load_models()
    
    def load_models(self):
        """Load trained model and tokenizer"""
        try:
            if os.path.exists(Config.MODEL_PATH):
                self.model = load_model(Config.MODEL_PATH)
                print("Model loaded successfully")
            else:
                print(f"Model not found at {Config.MODEL_PATH}")
            
            if os.path.exists(Config.TOKENIZER_PATH):
                self.tokenizer = joblib.load(Config.TOKENIZER_PATH)
                print("Tokenizer loaded successfully")
            else:
                print(f"Tokenizer not found at {Config.TOKENIZER_PATH}")
        except Exception as e:
            print(f"Error loading models: {e}")
    
    def predict_text(self, text: str) -> Dict:
        """
        Predict if job posting text is fake or genuine
        Returns: dict with label, confidence, and explanation
        """
        if not self.model or not self.tokenizer:
            return {
                'error': 'Model not loaded. Please train the model first.',
                'label': 'Unknown',
                'confidence': 0.0
            }
        
        # Preprocess text
        processed_text = self.preprocessor.preprocess(text)
        
        if not processed_text:
            return {
                'error': 'Empty text after preprocessing',
                'label': 'Unknown',
                'confidence': 0.0
            }
        
        # Tokenize and pad
        sequence = self.tokenizer.texts_to_sequences([processed_text])
        padded = pad_sequences(sequence, maxlen=Config.MAX_SEQUENCE_LENGTH, padding='post')
        
        # Predict
        prediction_prob = self.model.predict(padded, verbose=0)[0][0]
        
        # Determine label
        is_fake = prediction_prob > Config.CONFIDENCE_THRESHOLD
        label = "Fake" if is_fake else "Genuine"
        confidence = float(prediction_prob if is_fake else 1 - prediction_prob)
        
        # Extract keywords for explanation
        keywords = self.preprocessor.extract_keywords(text, top_n=5)
        
        # Generate reason
        reason = self._generate_reason(is_fake, confidence, keywords)
        
        return {
            'label': label,
            'confidence': round(confidence, 4),
            'confidence_score': round(float(prediction_prob), 4),
            'keywords': keywords,
            'reason': reason
        }
    
    def _generate_reason(self, is_fake: bool, confidence: float, keywords: List[str]) -> str:
        """Generate explanation for the prediction"""
        if is_fake:
            if confidence > 0.8:
                reason = f"High probability of fraud detected. "
            elif confidence > 0.6:
                reason = f"Moderate fraud indicators found. "
            else:
                reason = f"Some suspicious patterns detected. "
            
            reason += f"Key terms analyzed: {', '.join(keywords[:3])}. "
            reason += "Common fraud indicators include unrealistic salary promises, vague job descriptions, "
            reason += "lack of company information, or requests for personal/financial information upfront."
        else:
            if confidence > 0.8:
                reason = f"Strong indicators of legitimate job posting. "
            elif confidence > 0.6:
                reason = f"Appears to be a genuine job posting. "
            else:
                reason = f"Likely a legitimate posting. "
            
            reason += f"Key terms: {', '.join(keywords[:3])}. "
            reason += "Genuine postings typically have clear job descriptions, realistic requirements, "
            reason += "and verifiable company information."
        
        return reason
    
    def batch_predict(self, texts: List[str]) -> List[Dict]:
        """Predict multiple job postings at once"""
        return [self.predict_text(text) for text in texts]
    
    def get_model_info(self) -> Dict:
        """Get information about loaded model"""
        if not self.model:
            return {'status': 'Model not loaded'}
        
        return {
            'status': 'Model loaded',
            'model_path': Config.MODEL_PATH,
            'max_sequence_length': Config.MAX_SEQUENCE_LENGTH,
            'max_features': Config.MAX_FEATURES,
            'confidence_threshold': Config.CONFIDENCE_THRESHOLD
        }

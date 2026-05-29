"""
FastAPI Main Application
REST API endpoints for Fake Job Detection System
"""
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import Optional
import os
import uuid
from datetime import datetime
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config import Config
from app.services.predictor import FakeJobPredictor
from app.services.image_processor import ImageProcessor
from app.database.connection import Database

# Initialize FastAPI app
app = FastAPI(
    title="Fake Job Detection API",
    description="AI-powered system to detect fraudulent job postings",
    version="1.0.0"
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
predictor = FakeJobPredictor()
image_processor = ImageProcessor()
db = Database()

# Create upload directory
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Pydantic models for request/response
class TextPredictionRequest(BaseModel):
    text: str

class TextPredictionResponse(BaseModel):
    label: str
    confidence: float
    confidence_score: float
    keywords: list
    reason: str
    prediction_id: Optional[int] = None

class ImageURLRequest(BaseModel):
    image_url: HttpUrl

class ImagePredictionResponse(BaseModel):
    label: str
    confidence: float
    confidence_score: float
    extracted_text: str
    keywords: list
    reason: str
    prediction_id: Optional[int] = None

@app.on_event("startup")
async def startup_event():
    """Initialize database connection on startup"""
    try:
        db.connect()
        print("API Server started successfully")
    except Exception as e:
        print(f"Warning: Database connection failed: {e}")
        print("API will work without database storage")

@app.on_event("shutdown")
async def shutdown_event():
    """Close database connection on shutdown"""
    try:
        db.disconnect()
        print("API Server shutdown")
    except:
        pass

@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Fake Job Detection API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "predict_text": "/predict-text",
            "predict_image": "/predict-image",
            "predict_image_url": "/predict-image-url",
            "model_info": "/model-info"
        }
    }

@app.post("/predict-text", response_model=TextPredictionResponse)
async def predict_text(request: TextPredictionRequest):
    """
    Predict if job posting text is fake or genuine
    
    Args:
        request: TextPredictionRequest with job posting text
    
    Returns:
        Prediction result with label, confidence, and explanation
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        # Make prediction
        result = predictor.predict_text(request.text)
        
        if 'error' in result:
            raise HTTPException(status_code=500, detail=result['error'])
        
        # Save to database (optional)
        try:
            prediction_id = db.save_prediction(
                input_type='text',
                job_text=request.text,
                image_path=None,
                prediction_label=result['label'],
                confidence_score=result['confidence'],
                extracted_text=None,
                reason=result['reason']
            )
            result['prediction_id'] = prediction_id
        except Exception as e:
            print(f"Warning: Could not save to database: {e}")
            result['prediction_id'] = None
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-image", response_model=ImagePredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    """
    Predict if job poster image contains fake job posting
    Extracts text using OCR and analyzes it
    
    Args:
        file: Uploaded image file
    
    Returns:
        Prediction result with extracted text and analysis
    """
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        file_ext = file.filename.split('.')[-1].lower()
        if file_ext not in Config.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file type. Allowed: {Config.ALLOWED_EXTENSIONS}"
            )
        
        # Save uploaded file
        file_id = str(uuid.uuid4())
        file_path = os.path.join(Config.UPLOAD_FOLDER, f"{file_id}.{file_ext}")
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Extract text from image
        extracted_text, _ = image_processor.process_image_file(file_path)
        
        if not extracted_text or len(extracted_text.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the image"
            )
        
        # Make prediction on extracted text
        result = predictor.predict_text(extracted_text)
        
        if 'error' in result:
            raise HTTPException(status_code=500, detail=result['error'])
        
        # Save to database (optional)
        try:
            prediction_id = db.save_prediction(
                input_type='image',
                job_text=None,
                image_path=file_path,
                prediction_label=result['label'],
                confidence_score=result['confidence'],
                extracted_text=extracted_text,
                reason=result['reason']
            )
            result['extracted_text'] = extracted_text
            result['prediction_id'] = prediction_id
        except Exception as e:
            print(f"Warning: Could not save to database: {e}")
            result['extracted_text'] = extracted_text
            result['prediction_id'] = None
        
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-image-url", response_model=ImagePredictionResponse)
async def predict_image_url(request: ImageURLRequest):
    """
    Predict if job poster from URL contains fake job posting
    Downloads image, extracts text using OCR, and analyzes it
    
    Args:
        request: ImageURLRequest with image URL
    
    Returns:
        Prediction result with extracted text and analysis
    """
    try:
        # Extract text from image URL
        extracted_text, image = image_processor.process_image_url(str(request.image_url))
        
        if not extracted_text or len(extracted_text.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the image URL"
            )
        
        # Make prediction on extracted text
        result = predictor.predict_text(extracted_text)
        
        if 'error' in result:
            raise HTTPException(status_code=500, detail=result['error'])
        
        # Save to database (optional)
        try:
            prediction_id = db.save_prediction(
                input_type='image_url',
                job_text=None,
                image_path=str(request.image_url),
                prediction_label=result['label'],
                confidence_score=result['confidence'],
                extracted_text=extracted_text,
                reason=result['reason']
            )
            result['extracted_text'] = extracted_text
            result['prediction_id'] = prediction_id
        except Exception as e:
            print(f"Warning: Could not save to database: {e}")
            result['extracted_text'] = extracted_text
            result['prediction_id'] = None
        
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model-info")
async def get_model_info():
    """Get information about the loaded model"""
    return predictor.get_model_info()

@app.get("/predictions")
async def get_predictions(limit: int = 50):
    """Get recent predictions from database"""
    try:
        predictions = db.get_predictions(limit)
        return {
            "count": len(predictions),
            "predictions": predictions
        }
    except Exception as e:
        return {
            "count": 0,
            "predictions": [],
            "message": "Database not configured or unavailable"
        }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "model_loaded": predictor.model is not None
    }

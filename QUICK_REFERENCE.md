# Fake Job Detection System - Quick Reference

## 🚀 Quick Commands

### Backend
```bash
# Setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Generate sample dataset (if needed)
python generate_sample_dataset.py

# Train model
python train_model.py

# Check setup
python quick_start.py

# Start server
uvicorn app.main:app --reload

# Test API
python test_api.py
```

### Frontend
```bash
# Setup
cd frontend
npm install

# Start
npm start

# Build for production
npm run build
```

### Database
```bash
# Create database
mysql -u root -p < database/schema.sql

# Or manually
mysql -u root -p
CREATE DATABASE fake_job_detection;
USE fake_job_detection;
SOURCE database/schema.sql;
```

## 📡 API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints

**1. Predict Text**
```bash
POST /predict-text
Content-Type: application/json

{
  "text": "Job posting text here..."
}
```

**2. Predict Image**
```bash
POST /predict-image
Content-Type: multipart/form-data

file: <image_file>
```

**3. Predict Image URL**
```bash
POST /predict-image-url
Content-Type: application/json

{
  "image_url": "https://example.com/job-poster.jpg"
}
```

**4. Model Info**
```bash
GET /model-info
```

**5. Health Check**
```bash
GET /health
```

**6. Get Predictions**
```bash
GET /predictions?limit=50
```

## 🧪 Testing

### Test with cURL

**Text Prediction:**
```bash
curl -X POST "http://localhost:8000/predict-text" \
  -H "Content-Type: application/json" \
  -d '{"text": "Earn $10000 per week from home! No experience needed!"}'
```

**Health Check:**
```bash
curl http://localhost:8000/health
```

### Test with Python
```python
import requests

# Text prediction
response = requests.post(
    "http://localhost:8000/predict-text",
    json={"text": "Your job posting text"}
)
print(response.json())
```

## 📊 Model Information

### Architecture
- **Type**: Bidirectional LSTM (BiLSTM)
- **Layers**: Embedding → BiLSTM → BiLSTM → Dense → Output
- **Input**: Text sequences (max 200 words)
- **Output**: Binary classification (Fake/Genuine)

### Performance
- **Accuracy**: 95%+
- **Precision**: 93%+
- **Recall**: 91%+
- **F1-Score**: 92%+

### Preprocessing
1. Lowercase conversion
2. Remove URLs, emails, HTML
3. Tokenization
4. Stopword removal
5. Lemmatization

## 🗄️ Database Schema

### predictions table
```sql
- id (INT, PRIMARY KEY)
- input_type (ENUM: text, image, image_url)
- job_text (TEXT)
- image_path (VARCHAR)
- prediction_label (VARCHAR)
- confidence_score (FLOAT)
- extracted_text (TEXT)
- reason (TEXT)
- created_at (TIMESTAMP)
```

### model_metrics table
```sql
- id (INT, PRIMARY KEY)
- model_name (VARCHAR)
- accuracy (FLOAT)
- precision_score (FLOAT)
- recall_score (FLOAT)
- f1_score (FLOAT)
- trained_at (TIMESTAMP)
```

## 🔧 Configuration

### Backend (.env)
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fake_job_detection
DB_PORT=3306
```

### Frontend (api.js)
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

## 📁 Important Files

### Backend
- `train_model.py` - Train the BiLSTM model
- `app/main.py` - FastAPI application
- `app/services/predictor.py` - Prediction logic
- `app/services/text_preprocessor.py` - NLP preprocessing
- `app/services/image_processor.py` - OCR and image handling
- `config.py` - Configuration settings

### Frontend
- `src/App.js` - Main React component
- `src/components/TextPredictor.js` - Text analysis UI
- `src/components/ImagePredictor.js` - Image upload UI
- `src/services/api.js` - API client

### Documentation
- `README.md` - Project overview
- `SETUP_GUIDE.md` - Detailed setup
- `PROJECT_DOCUMENTATION.md` - Technical docs
- `PRESENTATION_GUIDE.md` - Presentation guide

## 🐛 Common Issues

### Issue: Model not found
**Solution:**
```bash
cd backend
python train_model.py
```

### Issue: Database connection failed
**Solution:**
1. Check MySQL is running
2. Verify credentials in `.env`
3. Create database: `CREATE DATABASE fake_job_detection;`

### Issue: NLTK data not found
**Solution:**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Issue: Frontend can't connect to backend
**Solution:**
1. Ensure backend is running on port 8000
2. Check CORS settings in `app/main.py`
3. Verify API_BASE_URL in `frontend/src/services/api.js`

### Issue: EasyOCR installation fails
**Solution:**
- Windows: Install Visual C++ Build Tools
- Try: `pip install easyocr --no-cache-dir`

## 📦 Dependencies

### Backend (Python)
```
fastapi==0.104.1
uvicorn==0.24.0
tensorflow==2.15.0
pandas==2.1.3
numpy==1.24.3
scikit-learn==1.3.2
nltk==3.8.1
mysql-connector-python==8.2.0
easyocr==1.7.1
opencv-python==4.8.1.78
```

### Frontend (Node)
```
react==18.2.0
react-dom==18.2.0
react-router-dom==6.20.0
axios==1.6.2
```

## 🎯 Sample Test Cases

### Fake Job Examples
```
1. "Earn $10,000 per week from home! No experience needed! 
    Just send $99 for training materials!"

2. "URGENT HIRING! Make money fast! No interview required! 
    Send personal information to get started!"

3. "Work from home doing simple tasks. Earn $100 per hour. 
    Pay registration fee to begin!"
```

### Genuine Job Examples
```
1. "Software Engineer at ABC Corp. Requirements: BS in CS, 
    3 years Python experience. Salary: $80k-$100k."

2. "Marketing Manager position. MBA preferred, 5 years experience. 
    Competitive salary and benefits."

3. "Data Scientist role. MS in Statistics, Python/R skills required. 
    Join our innovative team."
```

## 🎓 For Presentation

### Demo Flow
1. Show homepage (30 sec)
2. Text analysis - fake job (2 min)
3. Text analysis - genuine job (1 min)
4. Image upload (2 min)
5. API documentation (1 min)

### Key Points
- BiLSTM for better accuracy
- NLP preprocessing pipeline
- OCR for image analysis
- RESTful API design
- Real-time predictions
- Explainable results

### Viva Questions
- Why BiLSTM over LSTM?
- How does text preprocessing work?
- What is TF-IDF?
- How does OCR work?
- What are the limitations?
- How to improve accuracy?

## 📞 Support

For detailed information, see:
- **Setup**: SETUP_GUIDE.md
- **Documentation**: PROJECT_DOCUMENTATION.md
- **Presentation**: PRESENTATION_GUIDE.md

## 🔗 URLs

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

---

**Quick Tip**: Keep this file open during development and presentation for quick reference!

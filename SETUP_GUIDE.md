# Fake Job Detection System - Setup Guide

## Complete Installation and Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- npm (Node package manager)

---

## Step 1: Database Setup

### Install MySQL
Download and install MySQL from: https://dev.mysql.com/downloads/

### Create Database
```bash
# Login to MySQL
mysql -u root -p

# Run the schema file
source database/schema.sql

# Or manually create:
CREATE DATABASE fake_job_detection;
USE fake_job_detection;
```

### Configure Database Connection
```bash
cd backend
cp .env.example .env

# Edit .env file with your MySQL credentials:
# DB_HOST=localhost
# DB_USER=root
# DB_PASSWORD=your_password
# DB_NAME=fake_job_detection
# DB_PORT=3306
```

---

## Step 2: Backend Setup

### Install Python Dependencies
```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Download NLTK Data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Download Dataset (Optional)
Download the Kaggle Fake Job Postings dataset:
https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

Place `fake_jobs.csv` in the `backend/` directory.

Note: If you don't have the dataset, the training script will create a small sample dataset for demonstration.

### Train the Model
```bash
python train_model.py
```

This will:
- Load and preprocess the dataset
- Train a BiLSTM model
- Save the model to `ml_models/fake_job_model.h5`
- Save the tokenizer to `ml_models/tokenizer.pkl`
- Display accuracy, precision, recall, and F1-score

Expected output:
```
Model Performance:
Accuracy: 0.95+
Precision: 0.93+
Recall: 0.91+
F1-Score: 0.92+
```

### Start Backend Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000

API Documentation: http://localhost:8000/docs

---

## Step 3: Frontend Setup

### Install Node Dependencies
```bash
cd frontend
npm install
```

### Start Frontend Development Server
```bash
npm start
```

Frontend will be available at: http://localhost:3000

---

## Step 4: Testing the System

### Test Backend API
Visit: http://localhost:8000/docs

Try the endpoints:
1. `/predict-text` - Test with sample job text
2. `/predict-image` - Upload a job poster image
3. `/predict-image-url` - Provide an image URL

### Test Frontend
1. Open http://localhost:3000
2. Navigate to "Text Analysis"
3. Paste a job posting
4. Click "Analyze Job Posting"
5. View results with confidence score

---

## Project Structure

```
fake-job-detection/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   │   └── connection.py
│   │   ├── services/
│   │   │   ├── text_preprocessor.py
│   │   │   ├── image_processor.py
│   │   │   └── predictor.py
│   │   └── main.py
│   ├── ml_models/
│   │   ├── fake_job_model.h5
│   │   └── tokenizer.pkl
│   ├── uploads/
│   ├── config.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Home.js
│   │   │   ├── TextPredictor.js
│   │   │   ├── ImagePredictor.js
│   │   │   └── ImageURLPredictor.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
├── database/
│   └── schema.sql
└── README.md
```

---

## API Endpoints

### POST /predict-text
Analyze job posting text
```json
{
  "text": "Job posting text here..."
}
```

### POST /predict-image
Upload job poster image (multipart/form-data)

### POST /predict-image-url
Analyze image from URL
```json
{
  "image_url": "https://example.com/job-poster.jpg"
}
```

### GET /model-info
Get model information

### GET /health
Health check endpoint

---

## Troubleshooting

### Backend Issues

**Error: Model not found**
- Run `python train_model.py` to train the model

**Error: Database connection failed**
- Check MySQL is running
- Verify credentials in `.env` file
- Ensure database exists

**Error: NLTK data not found**
- Run: `python -c "import nltk; nltk.download('all')"`

**Error: EasyOCR installation failed**
- Install Visual C++ Build Tools (Windows)
- Try: `pip install easyocr --no-cache-dir`

### Frontend Issues

**Error: Cannot connect to backend**
- Ensure backend is running on port 8000
- Check CORS settings in `backend/app/main.py`

**Error: npm install fails**
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again

---

## For Final Year Project Presentation

### Key Points to Highlight:
1. **AI/ML Techniques**: BiLSTM, NLP, TF-IDF, OCR
2. **Tech Stack**: Python, FastAPI, React, MySQL
3. **Features**: Text analysis, image OCR, confidence scores
4. **Real-world Application**: Protecting job seekers from fraud
5. **Scalability**: RESTful API, modular architecture

### Demo Flow:
1. Show homepage and explain features
2. Demonstrate text analysis with sample fake job
3. Upload job poster image and show OCR extraction
4. Explain confidence scores and reasoning
5. Show database storing predictions
6. Display model performance metrics

### Viva Questions Preparation:
- Why BiLSTM over simple LSTM?
- How does text preprocessing improve accuracy?
- What is TF-IDF and why use it?
- How does OCR work in the system?
- What are the limitations of the model?
- How can the system be improved?

---

## Future Enhancements
- Add CNN for visual forgery detection
- Implement user authentication
- Add reporting and analytics dashboard
- Deploy to cloud (AWS/Azure/GCP)
- Mobile app development
- Multi-language support
- Real-time job posting monitoring

---

## License
This project is for educational purposes (Final Year Engineering Project).

## Contact
For issues or questions, please refer to the project documentation.

# Installation Troubleshooting Guide

## TensorFlow Installation Issues

### Issue: "Could not find a version that satisfies the requirement tensorflow==2.15.0"

This happens when your Python version is not compatible with the specified TensorFlow version.

### Solution 1: Use Updated Requirements (Recommended)
The requirements.txt has been updated to use the latest TensorFlow version:

```bash
cd backend
pip install -r requirements.txt
```

### Solution 2: Install TensorFlow Separately
```bash
# Install the latest TensorFlow
pip install tensorflow

# Then install other requirements
pip install fastapi uvicorn pandas numpy scikit-learn nltk mysql-connector-python python-multipart Pillow opencv-python easyocr requests pydantic python-dotenv joblib
```

### Solution 3: Use Minimal Requirements
```bash
cd backend
pip install -r requirements-minimal.txt
```

### Solution 4: Check Python Version
TensorFlow 2.20+ requires Python 3.9-3.12

```bash
python --version
```

If your Python version is too old or too new:
- Install Python 3.10 or 3.11 (recommended)
- Create a new virtual environment with the correct version

---

## Common Installation Issues

### Issue: EasyOCR Installation Fails

**Windows:**
```bash
# Install Visual C++ Build Tools first
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Then install EasyOCR
pip install easyocr --no-cache-dir
```

**Alternative:**
```bash
# Skip EasyOCR for now, install later
pip install fastapi uvicorn tensorflow pandas numpy scikit-learn nltk mysql-connector-python python-multipart Pillow opencv-python requests pydantic python-dotenv joblib

# Try EasyOCR separately
pip install easyocr
```

### Issue: OpenCV Installation Fails

```bash
# Try headless version
pip install opencv-python-headless
```

### Issue: MySQL Connector Fails

```bash
# Try alternative
pip install pymysql
```

Then update `backend/app/database/connection.py`:
```python
import pymysql as mysql.connector
```

### Issue: NumPy Version Conflict

```bash
# Install compatible NumPy version
pip install "numpy>=1.24.0,<2.0.0"
```

---

## Step-by-Step Installation (If Main Method Fails)

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### 2. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Upgrade pip
```bash
python -m pip install --upgrade pip
```

### 4. Install Core Dependencies First
```bash
pip install fastapi uvicorn pydantic python-dotenv python-multipart
```

### 5. Install TensorFlow
```bash
pip install tensorflow
```

### 6. Install Data Science Libraries
```bash
pip install pandas numpy scikit-learn joblib
```

### 7. Install NLP Libraries
```bash
pip install nltk
```

### 8. Install Database Connector
```bash
pip install mysql-connector-python
```

### 9. Install Image Processing (Optional - can skip for text-only testing)
```bash
pip install Pillow opencv-python
pip install easyocr  # This might take time
```

### 10. Install Remaining Dependencies
```bash
pip install requests
```

---

## Verify Installation

Run the quick start script:
```bash
python quick_start.py
```

This will check:
- Python version
- All dependencies
- NLTK data
- Model files

---

## Alternative: Use Docker (Advanced)

If you continue to have issues, you can use Docker:

### Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and Run
```bash
docker build -t fake-job-detection .
docker run -p 8000:8000 fake-job-detection
```

---

## Minimal Setup (Text Analysis Only)

If you want to test the system without image processing:

### Install Minimal Dependencies
```bash
pip install fastapi uvicorn tensorflow pandas numpy scikit-learn nltk mysql-connector-python pydantic python-dotenv joblib requests
```

### Skip Image Features
Comment out image-related imports in `backend/app/main.py`:
```python
# from app.services.image_processor import ImageProcessor
# image_processor = ImageProcessor()
```

Comment out image endpoints:
```python
# @app.post("/predict-image")
# @app.post("/predict-image-url")
```

---

## Platform-Specific Issues

### Windows

**Issue: Microsoft Visual C++ 14.0 required**
- Download and install: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Select "Desktop development with C++"

**Issue: Long path names**
```bash
# Enable long paths in Windows
# Run as Administrator in PowerShell:
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

### Linux

**Issue: Missing system libraries**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-pip libmysqlclient-dev

# For OpenCV
sudo apt-get install libgl1-mesa-glx libglib2.0-0
```

### Mac

**Issue: Architecture mismatch (M1/M2)**
```bash
# Use conda for better compatibility
conda create -n fakejob python=3.10
conda activate fakejob
conda install tensorflow
pip install -r requirements.txt
```

---

## Testing Without Full Installation

### Test Backend Without ML Model

Create a simple test endpoint in `backend/app/main.py`:

```python
@app.post("/test")
async def test_endpoint():
    return {"status": "Backend is working!"}
```

Start server:
```bash
uvicorn app.main:app --reload
```

Test:
```bash
curl http://localhost:8000/test
```

---

## Getting Help

### Check Versions
```bash
python --version
pip --version
pip list
```

### Check Python Path
```bash
python -c "import sys; print(sys.executable)"
```

### Check Installed Packages
```bash
pip list | grep tensorflow
pip list | grep fastapi
```

### Clear Cache and Reinstall
```bash
pip cache purge
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

---

## Quick Fix Commands

### Complete Reinstall
```bash
# Remove virtual environment
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# Create fresh environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Upgrade pip
python -m pip install --upgrade pip

# Install with no cache
pip install --no-cache-dir -r requirements.txt
```

### Install Without Version Constraints
```bash
pip install fastapi uvicorn tensorflow pandas numpy scikit-learn nltk mysql-connector-python python-multipart Pillow opencv-python easyocr requests pydantic python-dotenv joblib
```

---

## Still Having Issues?

### Option 1: Use Google Colab
Upload the training script to Google Colab and train the model there, then download the model files.

### Option 2: Use Pre-trained Model
If someone provides a pre-trained model, just place it in `backend/ml_models/` and skip training.

### Option 3: Simplify the Project
Focus on the text analysis part first, add image processing later.

---

## Contact & Support

If you continue to face issues:
1. Check the error message carefully
2. Search for the specific error online
3. Check TensorFlow compatibility: https://www.tensorflow.org/install
4. Check Python version compatibility
5. Try the minimal installation approach

---

**Remember**: The most common issue is Python version incompatibility. Make sure you're using Python 3.9-3.12 for best results.

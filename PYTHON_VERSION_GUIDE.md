# Python Version Compatibility Guide

## Current Issue

You are using **Python 3.13.5**, which is too new for TensorFlow.

**TensorFlow 2.20** supports: Python 3.9, 3.10, 3.11, and 3.12
**Your Python**: 3.13.5 ❌

## Solutions

### Solution 1: Install Python 3.11 or 3.12 (Recommended)

#### Download Python 3.11 or 3.12
- Visit: https://www.python.org/downloads/
- Download Python 3.11.x or 3.12.x (latest stable)
- Install it (you can have multiple Python versions)

#### Create Virtual Environment with Specific Python Version
```bash
# Find Python 3.11 or 3.12 installation
# Usually in: C:\Users\YourName\AppData\Local\Programs\Python\Python311
# or: C:\Python311

# Create venv with specific Python version
C:\Python311\python.exe -m venv venv

# Or if you have py launcher
py -3.11 -m venv venv

# Activate
venv\Scripts\activate

# Verify version
python --version  # Should show 3.11.x or 3.12.x

# Install requirements
pip install -r requirements.txt
```

### Solution 2: Use Conda (Easier)

```bash
# Install Miniconda or Anaconda
# Download from: https://docs.conda.io/en/latest/miniconda.html

# Create environment with Python 3.11
conda create -n fakejob python=3.11

# Activate
conda activate fakejob

# Navigate to backend
cd backend

# Install requirements
pip install -r requirements.txt
```

### Solution 3: Wait for TensorFlow Update

TensorFlow will eventually support Python 3.13, but it may take months.

### Solution 4: Use TensorFlow Nightly (Not Recommended for Production)

```bash
pip install tf-nightly
```

This might have Python 3.13 support but is unstable.

---

## Recommended Approach

### Step 1: Install Python 3.11

1. Go to https://www.python.org/downloads/
2. Download Python 3.11.x (latest 3.11 version)
3. During installation:
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install for all users" (optional)
4. Complete installation

### Step 2: Verify Installation

```bash
# Check if Python 3.11 is installed
py -3.11 --version

# Or check all Python versions
py --list
```

### Step 3: Create Project Environment

```bash
# Navigate to backend folder
cd "D:\MINI Project 2.0\Job Detection\backend"

# Remove old venv if exists
rmdir /s venv

# Create new venv with Python 3.11
py -3.11 -m venv venv

# Activate
venv\Scripts\activate

# Verify Python version
python --version  # Should show 3.11.x

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

---

## Quick Check Commands

### Check All Python Versions on Your System
```bash
py --list
```

### Check Current Python Version
```bash
python --version
```

### Check Where Python is Installed
```bash
where python
```

### Check pip Version
```bash
pip --version
```

---

## Alternative: Use Google Colab for Training

If you don't want to install a different Python version:

1. **Train model in Google Colab** (free, has TensorFlow pre-installed)
2. **Download trained model files**
3. **Use them in your project**

### Google Colab Steps:

1. Go to https://colab.research.google.com/
2. Create new notebook
3. Upload your `train_model.py` and related files
4. Run training in Colab
5. Download `fake_job_model.h5` and `tokenizer.pkl`
6. Place them in `backend/ml_models/`
7. Your API will work without training locally

---

## Compatibility Matrix

| Python Version | TensorFlow 2.20 | Recommended |
|----------------|-----------------|-------------|
| 3.8 | ❌ | No (too old) |
| 3.9 | ✅ | Yes |
| 3.10 | ✅ | Yes |
| 3.11 | ✅ | **Best** |
| 3.12 | ✅ | Yes |
| 3.13 | ❌ | No (too new) |

---

## What to Do Right Now

### Option A: Install Python 3.11 (Best for long-term)
1. Download Python 3.11 from python.org
2. Install it
3. Create new venv with Python 3.11
4. Install requirements

### Option B: Use Conda (Easiest)
1. Install Miniconda
2. Create environment with Python 3.11
3. Install requirements

### Option C: Train in Colab (Quickest)
1. Use Google Colab to train model
2. Download model files
3. Skip training locally

---

## After Installing Correct Python Version

```bash
# Verify version
python --version  # Should be 3.9-3.12

# Install requirements
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Generate sample dataset
python generate_sample_dataset.py

# Train model
python train_model.py

# Start server
uvicorn app.main:app --reload
```

---

## Need Help?

See **INSTALLATION_TROUBLESHOOTING.md** for more detailed troubleshooting steps.

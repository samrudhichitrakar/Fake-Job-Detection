# How to Run the Fake Job Detection System

## 🚀 Quick Start Guide

### Prerequisites Check
Before starting, make sure you have:
- ✅ Python 3.9, 3.10, 3.11, or 3.12 (NOT 3.13!)
- ✅ Node.js 16 or higher
- ✅ MySQL 8.0 or higher

---

## 📋 Step-by-Step Instructions

### STEP 1: Fix Python Version Issue (IMPORTANT!)

**Check your Python version:**
```bash
python --version
```

**If you see Python 3.13.x, you need to install Python 3.11 or 3.12:**

1. Download Python 3.11 from: https://www.python.org/downloads/
2. Install it (check "Add Python to PATH")
3. Verify installation:
```bash
py -3.11 --version
```

---

### STEP 2: Setup Database

**Option A: Using MySQL Command Line**
```bash
# Open MySQL command line
mysql -u root -p

# Enter your password, then run:
CREATE DATABASE fake_job_detection;
USE fake_job_detection;
SOURCE D:/MINI Project 2.0/Job Detection/database/schema.sql;
exit;
```

**Option B: Using MySQL Workbench**
1. Open MySQL Workbench
2. Connect to your server
3. Click "File" → "Run SQL Script"
4. Select `database/schema.sql`
5. Execute

---

### STEP 3: Setup Backend

**Open Command Prompt or PowerShell in the backend folder:**

```bash
# Navigate to backend folder
cd "D:\MINI Project 2.0\Job Detection\backend"

# Create virtual environment with Python 3.11
py -3.11 -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your prompt now

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies (this will take 5-10 minutes)
pip install -r requirements.txt

# If above fails, try:
pip install --no-cache-dir -r requirements.txt
```

**Configure Database Connection:**
```bash
# Copy the example env file
copy .env.example .env

# Edit .env file with Notepad
notepad .env
```

**In the .env file, set your MySQL credentials:**
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=fake_job_detection
DB_PORT=3306
```

**Download NLTK Data:**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

**Generate Sample Dataset:**
```bash
python generate_sample_dataset.py
```

**Train the Model (takes 5-10 minutes):**
```bash
python train_model.py
```

You should see output like:
```
Loading dataset...
Training samples: 160, Test samples: 40
Creating model...
Training model...
Epoch 1/10
...
Model Performance:
Accuracy: 0.95+
```

---

### STEP 4: Setup Frontend

**Open a NEW Command Prompt/PowerShell window:**

```bash
# Navigate to frontend folder
cd "D:\MINI Project 2.0\Job Detection\frontend"

# Install dependencies (takes 2-3 minutes)
npm install

# If you get errors, try:
npm install --legacy-peer-deps
```

---

### STEP 5: Run the Project

**You need TWO terminal windows open:**

**Terminal 1 - Backend:**
```bash
cd "D:\MINI Project 2.0\Job Detection\backend"
venv\Scripts\activate
uvicorn app.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Terminal 2 - Frontend:**
```bash
cd "D:\MINI Project 2.0\Job Detection\frontend"
npm start
```

Browser will automatically open to http://localhost:3000

---

## 🎉 Access the Application

Once both servers are running:

- **Frontend (User Interface)**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## 🧪 Test the System

### Test 1: Text Analysis
1. Go to http://localhost:3000
2. Click "Text Analysis"
3. Paste this fake job:
```
URGENT HIRING! Work from home and earn $10,000 per week!
No experience needed! Just send $99 for training materials!
Contact us now! Limited slots available!
```
4. Click "Analyze Job Posting"
5. You should see: **FAKE JOB POSTING** with high confidence

### Test 2: Genuine Job
Paste this:
```
Software Engineer at ABC Technology Inc.

Requirements:
- Bachelor's degree in Computer Science
- 3+ years of Python experience
- Strong knowledge of Django and Flask
- Experience with RESTful APIs

Salary: $80,000 - $100,000 per year
Benefits: Health insurance, 401(k), Paid time off

Apply: careers@abctech.com
```
You should see: **GENUINE JOB POSTING**

---

## 🛑 How to Stop the Servers

**To stop the servers:**
- Press `Ctrl + C` in each terminal window
- Or close the terminal windows

---

## 🔄 How to Run Again Later

**Every time you want to run the project:**

**Terminal 1 (Backend):**
```bash
cd "D:\MINI Project 2.0\Job Detection\backend"
venv\Scripts\activate
uvicorn app.main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd "D:\MINI Project 2.0\Job Detection\frontend"
npm start
```

---

## 🚨 Common Issues & Solutions

### Issue 1: "Python 3.13 not compatible"
**Solution:** Install Python 3.11 or 3.12
- See **PYTHON_VERSION_GUIDE.md** for detailed steps

### Issue 2: "Module not found" errors
**Solution:** Make sure virtual environment is activated
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 3: "Database connection failed"
**Solution:** 
1. Make sure MySQL is running
2. Check credentials in `backend/.env`
3. Verify database exists:
```bash
mysql -u root -p
SHOW DATABASES;
```

### Issue 4: "Model not found"
**Solution:** Train the model
```bash
cd backend
venv\Scripts\activate
python train_model.py
```

### Issue 5: "Port 8000 already in use"
**Solution:** Kill the process or use different port
```bash
# Use different port
uvicorn app.main:app --reload --port 8001
```

### Issue 6: Frontend won't start
**Solution:** 
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

### Issue 7: "Cannot find module 'react'"
**Solution:**
```bash
cd frontend
npm install react react-dom react-router-dom axios
npm start
```

---

## 📱 Using the Application

### Home Page
- Overview of the system
- Links to different analysis methods

### Text Analysis
1. Paste job posting text
2. Click "Analyze Job Posting"
3. View results with confidence score

### Image Upload
1. Click "Choose File"
2. Select a job poster image
3. Click "Analyze Image"
4. System extracts text using OCR
5. View results

### Image URL
1. Paste image URL
2. Click "Analyze Image URL"
3. View results

---

## 🎯 Quick Commands Reference

### Backend Commands
```bash
# Activate environment
cd backend
venv\Scripts\activate

# Start server
uvicorn app.main:app --reload

# Train model
python train_model.py

# Test API
python test_api.py

# Check setup
python quick_start.py
```

### Frontend Commands
```bash
# Install dependencies
cd frontend
npm install

# Start development server
npm start

# Build for production
npm run build
```

### Database Commands
```bash
# Connect to MySQL
mysql -u root -p

# Show databases
SHOW DATABASES;

# Use database
USE fake_job_detection;

# Show tables
SHOW TABLES;

# View predictions
SELECT * FROM predictions LIMIT 10;
```

---

## 📊 Verify Everything is Working

### Check Backend
Open: http://localhost:8000/health

Should show:
```json
{
  "status": "healthy",
  "timestamp": "2024-...",
  "model_loaded": true
}
```

### Check Frontend
Open: http://localhost:3000

Should show the homepage with navigation

### Check Database
```bash
mysql -u root -p
USE fake_job_detection;
SELECT COUNT(*) FROM predictions;
```

---

## 🎓 For Demonstration

### Demo Preparation
1. Start both servers
2. Open http://localhost:3000
3. Have sample texts ready
4. Test all three input methods
5. Show API documentation at http://localhost:8000/docs

### Demo Flow (5 minutes)
1. **Homepage** (30 sec) - Explain features
2. **Text Analysis** (2 min) - Show fake and genuine examples
3. **Image Upload** (1.5 min) - Upload job poster
4. **API Docs** (1 min) - Show backend endpoints

---

## 💡 Pro Tips

1. **Keep terminals open** - Don't close them while using the app
2. **Check logs** - Terminal shows useful error messages
3. **Use API docs** - http://localhost:8000/docs for testing
4. **Save test cases** - Keep sample job postings for quick testing
5. **Monitor database** - Check predictions table to see stored results

---

## 📞 Need More Help?

- **Installation Issues**: See **INSTALLATION_TROUBLESHOOTING.md**
- **Python Version**: See **PYTHON_VERSION_GUIDE.md**
- **Detailed Setup**: See **SETUP_GUIDE.md**
- **Quick Reference**: See **QUICK_REFERENCE.md**

---

## ✅ Success Checklist

Before considering setup complete:
- [ ] Python 3.11 or 3.12 installed
- [ ] MySQL database created
- [ ] Backend dependencies installed
- [ ] Model trained successfully
- [ ] Frontend dependencies installed
- [ ] Backend server running (port 8000)
- [ ] Frontend server running (port 3000)
- [ ] Can access http://localhost:3000
- [ ] Text analysis works
- [ ] Results display correctly

---

**You're all set! The system is now ready to use.** 🎉

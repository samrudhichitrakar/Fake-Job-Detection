@echo off
echo ============================================================
echo    FAKE JOB DETECTION SYSTEM - FIRST TIME SETUP
echo ============================================================
echo.
echo This script will set up the entire project.
echo Make sure you have installed:
echo   - Python 3.8+
echo   - Node.js 16+
echo   - MySQL 8.0+
echo.
pause

echo.
echo ============================================================
echo STEP 1: Setting up Backend
echo ============================================================
echo.

cd backend

echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Failed to create virtual environment!
    pause
    exit
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies!
    pause
    exit
)

echo.
echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

echo.
echo Generating sample dataset...
python generate_sample_dataset.py

echo.
echo Training model (this may take 5-10 minutes)...
python train_model.py
if errorlevel 1 (
    echo Model training failed!
    pause
    exit
)

echo.
echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Please edit backend\.env with your MySQL credentials!
)

cd ..

echo.
echo ============================================================
echo STEP 2: Setting up Frontend
echo ============================================================
echo.

cd frontend

echo Installing Node dependencies...
call npm install
if errorlevel 1 (
    echo Failed to install Node dependencies!
    pause
    exit
)

cd ..

echo.
echo ============================================================
echo STEP 3: Database Setup
echo ============================================================
echo.
echo Please run the following command in MySQL:
echo   mysql -u root -p ^< database\schema.sql
echo.
echo Or manually:
echo   1. Open MySQL command line
echo   2. CREATE DATABASE fake_job_detection;
echo   3. USE fake_job_detection;
echo   4. SOURCE database/schema.sql;
echo.
pause

echo.
echo ============================================================
echo    SETUP COMPLETE!
echo ============================================================
echo.
echo Next steps:
echo   1. Configure database in backend\.env
echo   2. Run START_PROJECT.bat to start servers
echo   3. Open http://localhost:3000 in browser
echo.
echo For detailed instructions, see SETUP_GUIDE.md
echo.
pause

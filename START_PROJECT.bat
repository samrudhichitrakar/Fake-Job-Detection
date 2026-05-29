@echo off
echo ============================================================
echo    FAKE JOB DETECTION SYSTEM - STARTUP SCRIPT
echo ============================================================
echo.

echo Checking if backend is set up...
if not exist "backend\venv" (
    echo Backend virtual environment not found!
    echo Please run setup first:
    echo   cd backend
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo   python train_model.py
    pause
    exit
)

if not exist "backend\ml_models\fake_job_model.h5" (
    echo Model not found!
    echo Please train the model first:
    echo   cd backend
    echo   python train_model.py
    pause
    exit
)

echo Checking if frontend is set up...
if not exist "frontend\node_modules" (
    echo Frontend dependencies not found!
    echo Please run setup first:
    echo   cd frontend
    echo   npm install
    pause
    exit
)

echo.
echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:app --reload"

timeout /t 3 /nobreak > nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo ============================================================
echo    SERVERS STARTING...
echo ============================================================
echo.
echo Backend will be available at: http://localhost:8000
echo Frontend will be available at: http://localhost:3000
echo API Documentation: http://localhost:8000/docs
echo.
echo Press any key to stop all servers...
pause > nul

echo.
echo Stopping servers...
taskkill /FI "WindowTitle eq Backend Server*" /T /F > nul 2>&1
taskkill /FI "WindowTitle eq Frontend Server*" /T /F > nul 2>&1

echo.
echo Servers stopped.
echo.
pause

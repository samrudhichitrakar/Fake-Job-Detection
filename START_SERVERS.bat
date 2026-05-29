@echo off
echo ============================================================
echo    STARTING FAKE JOB DETECTION SYSTEM
echo ============================================================
echo.

echo Starting Backend Server...
start "Backend - Port 8000" cmd /k "cd /d "%~dp0backend" && venv\Scripts\activate && uvicorn app.main:app --reload"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo Starting Frontend Server...
start "Frontend - Port 3000" cmd /k "cd /d "%~dp0frontend" && npm start"

echo.
echo ============================================================
echo    SERVERS ARE STARTING...
echo ============================================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Two new windows will open:
echo   1. Backend Server (black window)
echo   2. Frontend Server (will open browser)
echo.
echo Keep both windows open while using the application.
echo Close this window when done.
echo.
pause

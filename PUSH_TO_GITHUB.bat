@echo off
echo ============================================================
echo    PUSH PROJECT TO GITHUB
echo ============================================================
echo.

echo Step 1: Checking Git status...
git status
echo.

echo Step 2: Adding all files...
git add .
echo.

echo Step 3: Committing changes...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" (
    git commit -m "Update: Fake Job Detection System"
) else (
    git commit -m "%commit_msg%"
)
echo.

echo Step 4: Checking remote repository...
git remote -v
echo.

echo If you see a remote URL above, skip to Step 6.
echo If not, you need to add your GitHub repository URL.
echo.

set /p add_remote="Do you need to add remote repository? (y/n): "
if /i "%add_remote%"=="y" (
    set /p repo_url="Enter your GitHub repository URL: "
    git remote add origin !repo_url!
    echo Remote added successfully!
)
echo.

echo Step 5: Ensuring branch is named 'main'...
git branch -M main
echo.

echo Step 6: Pushing to GitHub...
git push -u origin main
echo.

echo ============================================================
echo    DONE!
echo ============================================================
echo.
echo Your project has been pushed to GitHub!
echo.
echo Next steps:
echo   1. Go to your GitHub repository
echo   2. Verify all files are there
echo   3. Check README.md displays correctly
echo.
pause

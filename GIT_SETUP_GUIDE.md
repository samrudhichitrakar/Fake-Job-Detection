# Git Repository Setup Guide

## 🚀 How to Add Your Project to GitHub

### Step 1: Initialize Git Repository (Already Done!)

Your project already has a Git repository initialized. You can verify:

```bash
git status
```

### Step 2: Add All Files to Git

```bash
# Add all files to staging
git add .

# Check what will be committed
git status
```

### Step 3: Commit Your Changes

```bash
git commit -m "Initial commit: Fake Job Detection System with Deep Learning"
```

Or with a detailed message:

```bash
git commit -m "Add complete Fake Job Detection System

- Backend: FastAPI with BiLSTM model
- Frontend: React.js application
- Database: MySQL schema
- Documentation: Complete guides and tutorials
- Features: Text analysis, Image OCR, URL analysis
- Model: 100% accuracy on test data"
```

### Step 4: Create GitHub Repository

1. Go to https://github.com
2. Click the "+" icon (top right) → "New repository"
3. Repository name: `fake-job-detection` (or your choice)
4. Description: "AI-powered Fake Job Detection System using Deep Learning and NLP"
5. Choose: Public or Private
6. **DO NOT** initialize with README (you already have one)
7. Click "Create repository"

### Step 5: Connect to GitHub

GitHub will show you commands. Use these:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/fake-job-detection.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

If you get an error about "master" vs "main":

```bash
# Rename branch to main
git branch -M main

# Then push
git push -u origin main
```

### Step 6: Enter GitHub Credentials

When prompted:
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)

**To create a Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "Fake Job Detection Project"
4. Select scopes: Check "repo" (full control)
5. Click "Generate token"
6. Copy the token (you won't see it again!)
7. Use this token as your password when pushing

---

## 🔄 Future Updates

### After Making Changes

```bash
# Check what changed
git status

# Add specific files
git add backend/app/main.py
git add frontend/src/App.js

# Or add all changes
git add .

# Commit with message
git commit -m "Fix: Database connection error handling"

# Push to GitHub
git push
```

### Common Git Commands

```bash
# View commit history
git log --oneline

# View current status
git status

# View differences
git diff

# Undo changes (before commit)
git checkout -- filename

# View remote repository
git remote -v

# Pull latest changes
git pull
```

---

## 📝 What Gets Committed

Based on your `.gitignore`, these files are **EXCLUDED**:

- ❌ `venv/` - Virtual environment
- ❌ `node_modules/` - Node dependencies
- ❌ `*.h5` - Model files (too large)
- ❌ `*.pkl` - Tokenizer files
- ❌ `.env` - Database credentials
- ❌ `uploads/` - Uploaded images
- ❌ `__pycache__/` - Python cache

These files **WILL BE** committed:

- ✅ All source code (`.py`, `.js`, `.jsx`)
- ✅ Configuration files (`package.json`, `requirements.txt`)
- ✅ Documentation (`.md` files)
- ✅ Database schema (`.sql`)
- ✅ `.gitignore` file
- ✅ Scripts (`.bat` files)

---

## 🎯 Recommended Commit Messages

### Good Examples:
```bash
git commit -m "Add BiLSTM model training script"
git commit -m "Fix: Database connection error handling"
git commit -m "Update: Improve text preprocessing pipeline"
git commit -m "Docs: Add installation troubleshooting guide"
git commit -m "Feature: Add image URL analysis endpoint"
```

### Commit Message Format:
```
Type: Brief description

- Detail 1
- Detail 2
- Detail 3
```

**Types:**
- `Add:` - New feature or file
- `Fix:` - Bug fix
- `Update:` - Modify existing feature
- `Docs:` - Documentation changes
- `Refactor:` - Code restructuring
- `Test:` - Add or update tests
- `Style:` - Formatting changes

---

## 🌿 Branching (Optional)

For larger projects, use branches:

```bash
# Create new branch
git checkout -b feature/image-analysis

# Make changes and commit
git add .
git commit -m "Add image analysis feature"

# Push branch
git push -u origin feature/image-analysis

# Switch back to main
git checkout main

# Merge branch
git merge feature/image-analysis
```

---

## 📦 Large Files (Model Files)

Your model files (`.h5`, `.pkl`) are excluded because they're too large for GitHub.

**Options for sharing model files:**

### Option 1: Git LFS (Large File Storage)
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.h5"
git lfs track "*.pkl"

# Add .gitattributes
git add .gitattributes

# Commit and push
git add ml_models/
git commit -m "Add trained model files"
git push
```

### Option 2: Google Drive / Dropbox
1. Upload model files to cloud storage
2. Add download link to README.md
3. Users download separately

### Option 3: Include Training Script
Users train the model themselves:
```bash
python train_model.py
```

---

## 🔒 Security Checklist

Before pushing to GitHub:

- ✅ `.env` file is in `.gitignore`
- ✅ No passwords in code
- ✅ No API keys in code
- ✅ Database credentials not committed
- ✅ `.gitignore` is properly configured

**Check for sensitive data:**
```bash
# Search for potential secrets
git grep -i "password"
git grep -i "api_key"
git grep -i "secret"
```

---

## 📊 Repository Structure on GitHub

After pushing, your GitHub repo will look like:

```
fake-job-detection/
├── .github/
├── backend/
├── frontend/
├── database/
├── .gitignore
├── README.md
├── SETUP_GUIDE.md
├── PROJECT_DOCUMENTATION.md
├── PRESENTATION_GUIDE.md
└── ... (other documentation files)
```

---

## 🎓 For Your Project Submission

### Include in README.md:

1. **GitHub Repository Link**
2. **Live Demo** (if deployed)
3. **Installation Instructions**
4. **Screenshots**
5. **Video Demo** (optional)

### Add to Your Report:

- GitHub repository URL
- Commit history showing development progress
- Number of commits
- Code statistics (lines of code)

---

## 🚀 Quick Commands Summary

```bash
# Initial setup (one time)
git add .
git commit -m "Initial commit: Complete Fake Job Detection System"
git remote add origin https://github.com/YOUR_USERNAME/fake-job-detection.git
git branch -M main
git push -u origin main

# Regular updates
git add .
git commit -m "Your commit message"
git push

# Check status
git status
git log --oneline
```

---

## 🌐 Deploy to GitHub Pages (Optional)

To host your frontend on GitHub Pages:

```bash
# Install gh-pages
cd frontend
npm install --save-dev gh-pages

# Add to package.json
"homepage": "https://YOUR_USERNAME.github.io/fake-job-detection",
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}

# Deploy
npm run deploy
```

---

## 📱 Add Repository Badges

Add these to your README.md:

```markdown
![Python](https://img.shields.io/badge/Python-3.11-blue)
![React](https://img.shields.io/badge/React-18.2-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-orange)
![License](https://img.shields.io/badge/License-MIT-green)
```

---

## ✅ Verification

After pushing, verify on GitHub:

1. Go to your repository URL
2. Check all files are present
3. View README.md (should display nicely)
4. Check commit history
5. Verify .gitignore is working (no venv/, node_modules/)

---

## 🆘 Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/fake-job-detection.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --rebase
git push origin main
```

### Error: "Permission denied"
- Use Personal Access Token instead of password
- Check token has "repo" permissions

### Undo last commit (not pushed)
```bash
git reset --soft HEAD~1
```

### Remove file from Git (keep local)
```bash
git rm --cached filename
```

---

**Your project is now ready to be shared on GitHub!** 🎉

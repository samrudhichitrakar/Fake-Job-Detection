"""
Quick Start Script
Checks dependencies and guides through setup
"""
import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is 3.8+"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"✗ Python 3.8+ required, found {version.major}.{version.minor}")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    required = [
        'fastapi', 'uvicorn', 'tensorflow', 'pandas', 
        'numpy', 'sklearn', 'nltk', 'mysql.connector'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} not found")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_mysql():
    """Check if MySQL is accessible"""
    print("\nChecking MySQL connection...")
    try:
        import mysql.connector
        # Try to connect (will fail if MySQL not running, but that's ok)
        print("✓ MySQL connector installed")
        return True
    except ImportError:
        print("✗ MySQL connector not installed")
        return False

def check_model_files():
    """Check if model files exist"""
    print("\nChecking model files...")
    model_path = "ml_models/fake_job_model.h5"
    tokenizer_path = "ml_models/tokenizer.pkl"
    
    model_exists = os.path.exists(model_path)
    tokenizer_exists = os.path.exists(tokenizer_path)
    
    if model_exists:
        print(f"✓ Model found at {model_path}")
    else:
        print(f"✗ Model not found at {model_path}")
    
    if tokenizer_exists:
        print(f"✓ Tokenizer found at {tokenizer_path}")
    else:
        print(f"✗ Tokenizer not found at {tokenizer_path}")
    
    return model_exists and tokenizer_exists

def download_nltk_data():
    """Download required NLTK data"""
    print("\nDownloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        print("✓ NLTK data downloaded")
        return True
    except Exception as e:
        print(f"✗ Error downloading NLTK data: {e}")
        return False

def main():
    """Main setup check"""
    print("=" * 60)
    print("FAKE JOB DETECTION SYSTEM - QUICK START")
    print("=" * 60)
    
    all_good = True
    
    # Check Python version
    if not check_python_version():
        all_good = False
    
    # Check dependencies
    deps_ok, missing = check_dependencies()
    if not deps_ok:
        all_good = False
        print("\nTo install missing dependencies:")
        print("  pip install -r requirements.txt")
    
    # Check MySQL
    if not check_mysql():
        all_good = False
    
    # Download NLTK data
    download_nltk_data()
    
    # Check model files
    if not check_model_files():
        print("\nModel files not found. To train the model:")
        print("  python train_model.py")
        all_good = False
    
    print("\n" + "=" * 60)
    if all_good:
        print("✓ ALL CHECKS PASSED!")
        print("\nYou can now start the server:")
        print("  uvicorn app.main:app --reload")
    else:
        print("✗ SOME CHECKS FAILED")
        print("\nPlease fix the issues above and try again.")
        print("See SETUP_GUIDE.md for detailed instructions.")
    print("=" * 60)

if __name__ == "__main__":
    main()

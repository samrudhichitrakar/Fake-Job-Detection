"""
Download all required NLTK data
Run this before training the model
"""
import nltk

print("Downloading NLTK data...")
print("This may take a few minutes...")

# Download all required packages
packages = [
    'punkt',
    'punkt_tab',
    'stopwords',
    'wordnet',
    'omw-1.4',
    'averaged_perceptron_tagger'
]

for package in packages:
    print(f"\nDownloading {package}...")
    try:
        nltk.download(package)
        print(f"✓ {package} downloaded successfully")
    except Exception as e:
        print(f"✗ Error downloading {package}: {e}")

print("\n" + "="*60)
print("NLTK data download complete!")
print("="*60)
print("\nYou can now run: python train_model.py")

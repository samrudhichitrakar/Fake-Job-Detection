"""
Image processing module for job poster analysis
Handles image preprocessing and OCR text extraction
"""
import cv2
import numpy as np
from PIL import Image
import easyocr
import requests
from io import BytesIO
from typing import Optional, Tuple
import os

class ImageProcessor:
    """Image processing and OCR for job posters"""
    
    def __init__(self):
        # Initialize EasyOCR reader (English language)
        self.reader = easyocr.Reader(['en'], gpu=False)
    
    def load_image_from_path(self, image_path: str) -> Optional[np.ndarray]:
        """Load image from file path"""
        try:
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to load image from {image_path}")
                return None
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
    
    def load_image_from_url(self, url: str) -> Optional[np.ndarray]:
        """Load image from URL"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            image = Image.open(BytesIO(response.content))
            image = np.array(image)
            
            # Convert RGB to BGR for OpenCV
            if len(image.shape) == 3 and image.shape[2] == 3:
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            return image
        except Exception as e:
            print(f"Error loading image from URL: {e}")
            return None
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocess image for better OCR results
        Steps: grayscale, denoising, thresholding
        """
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        
        # Apply denoising
        denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
        
        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(
            denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        
        return thresh
    
    def extract_text(self, image: np.ndarray) -> str:
        """
        Extract text from image using EasyOCR
        Returns concatenated text from all detected regions
        """
        try:
            # Preprocess image
            processed = self.preprocess_image(image)
            
            # Perform OCR
            results = self.reader.readtext(processed)
            
            # Extract and concatenate text
            extracted_text = ' '.join([result[1] for result in results])
            
            return extracted_text.strip()
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""
    
    def process_image_file(self, image_path: str) -> Tuple[Optional[str], Optional[np.ndarray]]:
        """
        Process image file and extract text
        Returns: (extracted_text, image_array)
        """
        image = self.load_image_from_path(image_path)
        if image is None:
            return None, None
        
        text = self.extract_text(image)
        return text, image
    
    def process_image_url(self, url: str) -> Tuple[Optional[str], Optional[np.ndarray]]:
        """
        Process image from URL and extract text
        Returns: (extracted_text, image_array)
        """
        image = self.load_image_from_url(url)
        if image is None:
            return None, None
        
        text = self.extract_text(image)
        return text, image
    
    def save_image(self, image: np.ndarray, save_path: str) -> bool:
        """Save processed image to disk"""
        try:
            cv2.imwrite(save_path, image)
            return True
        except Exception as e:
            print(f"Error saving image: {e}")
            return False

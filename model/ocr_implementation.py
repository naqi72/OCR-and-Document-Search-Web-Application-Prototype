import easyocr
import pytesseract
from PIL import Image

# Initialize EasyOCR for Hindi and English
reader = easyocr.Reader(['hi', 'en'], gpu=False)

# Function to perform OCR using Tesseract
def ocr_tesseract(image):
    return pytesseract.image_to_string(image)

# Function to perform OCR using EasyOCR
def ocr_easyocr(image_path):
    result = reader.readtext(image_path, detail=0)
    return ' '.join(result)

# Hybrid OCR Function based on user selection
def perform_ocr(image_path, ocr_model='easyocr'):
    image = Image.open(image_path)
    
    if ocr_model == 'tesseract':
        return ocr_tesseract(image)  # English (Tesseract)
    else:
        return ocr_easyocr(image_path)  # Multilingual (EasyOCR)


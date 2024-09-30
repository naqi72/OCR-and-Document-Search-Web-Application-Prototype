import easyocr
import pytesseract
from PIL import Image

# Initialize EasyOCR for Hindi and English
reader = easyocr.Reader(['hi', 'en'], gpu=False)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

# Function to perform OCR using Tesseract
def ocr_tesseract(image):
    return pytesseract.image_to_string(image)

# Function to perform OCR using EasyOCR
def ocr_easyocr(image):
    result = reader.readtext(image, detail=0)  # Pass the image directly
    return ' '.join(result)

# Hybrid OCR Function based on user selection
def perform_ocr(image_path, ocr_model='easyocr'):
    image = Image.open(image_path)
    
    if ocr_model == 'tesseract':
        return ocr_tesseract(image)  # Use the image directly
    else:
        return ocr_easyocr(image)  # Use the image directly

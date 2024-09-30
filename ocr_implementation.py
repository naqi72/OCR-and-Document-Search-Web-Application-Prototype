import easyocr
from PIL import Image

# Initialize EasyOCR for Hindi and English
reader = easyocr.Reader(['hi', 'en'], gpu=False)

# Function to perform OCR using EasyOCR
def perform_ocr(image_path):
    image = Image.open(image_path)
    result = reader.readtext(image, detail=0)  # detail=0 returns just the text
    return ' '.join(result)  # Join all the text into a single string

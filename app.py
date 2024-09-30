import streamlit as st
import easyocr
import numpy as np
from PIL import Image
from transformers import pipeline

# Initialize the EasyOCR Reader to support Hindi and English text recognition
reader = easyocr.Reader(['hi', 'en'])

# Initialize the Huggingface Transformers pipeline for Question Answering (QA)
# Explicitly using PyTorch as the backend framework
qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', framework='pt')

# Function to perform OCR (Optical Character Recognition) on the uploaded image
def ocr_image(uploaded_image):
    """
    Extracts text from the uploaded image using EasyOCR.
    
    Parameters:
    uploaded_image (UploadedImage): The image file uploaded by the user.

    Returns:
    str: Extracted text from the image as a single string.
    """
    # Convert the image into a NumPy array for processing
    image = Image.open(uploaded_image)
    image_np = np.array(image)

    # Use EasyOCR to extract text from the image
    result = reader.readtext(image_np, detail=0, paragraph=True)

    # Join the list of extracted text elements into a single string
    return " ".join(result)

# Function to search for a keyword in the extracted text using a Question-Answering (QA) pipeline
def search_keywords(extracted_text, keyword):
    """
    Uses a pre-trained QA model to find the keyword's location in the extracted text.
    
    Parameters:
    extracted_text (str): The text extracted from the image.
    keyword (str): The keyword to search for within the text.

    Returns:
    str: The result from the QA model, which answers where the keyword is mentioned.
    """
    # Use the Huggingface QA pipeline to search for the keyword in the text
    search_result = qa_pipeline({
        'context': extracted_text,
        'question': f"Where is {keyword} mentioned in the text?"
    })

    # Return the answer provided by the QA model
    return search_result['answer']

# Streamlit Web Application UI
st.title("OCR & Keyword Search Application using NLP")
st.write("""
    This application allows you to upload an image containing Hindi and/or English text.
    It will extract the text using OCR and perform a keyword search using a Question-Answering model.
""")

# File uploader widget to upload an image (supports JPEG and PNG formats)
uploaded_image = st.file_uploader("Upload an image (JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Display the uploaded image
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR to extract text from the image
    st.write("Extracting text from the image...")
    extracted_text = ocr_image(uploaded_image)

    # Display the extracted text
    st.write("### Extracted Text")
    st.write(extracted_text)

    # Input box for the user to enter a keyword for searching in the extracted text
    st.write("### Keyword Search in Extracted Text")
    keyword = st.text_input("Enter a keyword to search:")

    if keyword:
        # Perform keyword search using the QA model
        search_result = search_keywords(extracted_text, keyword)
        st.write(f"Search Result: {search_result}")

# Add footer or copyright information
st.write("© 2024 Developed by Syed Naqi Abbas")

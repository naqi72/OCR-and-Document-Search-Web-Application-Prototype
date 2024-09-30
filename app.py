import streamlit as st
from PIL import Image

# Import OCR functions
from ocr_implementation import perform_ocr

# Title of the web app
st.title("OCR and Document Search Application")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Model selection for OCR
ocr_model_choice = st.selectbox("Select OCR Model", ["easyocr", "tesseract"])

if uploaded_image:
    # Step 2: Perform OCR on the image
    image = Image.open(uploaded_image)
    extracted_text = perform_ocr(uploaded_image, ocr_model=ocr_model_choice)
    
    # Step 3: Display extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Step 4: Search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text")

    if search_keyword:
        # Perform search
        search_results = [line for line in extracted_text.splitlines() if search_keyword in line]
        
        # Display search results
        st.subheader("Search Results")
        if search_results:
            for result in search_results:
                st.write(result)
        else:
            st.write("No matches found.")

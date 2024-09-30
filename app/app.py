import streamlit as st
from PIL import Image

# Import OCR functions
from model/ocr_implementation import ocr_image, extract_text_as_json

# Title of the web app
st.title("OCR and Document Search Application")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Step 2: Perform OCR on the image
    image = Image.open(uploaded_image)
    extracted_text = ocr_image(uploaded_image)
    
    # Step 3: Display extracted text
    st.subheader("Extracted Text")
    st.write(extract_text_as_json(extracted_text))

    # Step 4: Search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text")

    if search_keyword:
        # Perform search
        search_results = [line for line in extracted_text if search_keyword in line]
        
        # Display search results
        st.subheader("Search Results")
        if search_results:
            for result in search_results:
                st.write(result)
        else:
            st.write("No matches found.")


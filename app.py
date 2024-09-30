import streamlit as st
from PIL import Image
from ocr_implementation import perform_ocr 

# Title of the web app
st.title("OCR and Document Search Application")

# Upload an image                         
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Step 2: Perform OCR on the image
    extracted_text = perform_ocr(uploaded_image)
    
    # Step 3: Display extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Step 4: Search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text")

    if search_keyword:
        # Perform search
        search_results = [line for line in extracted_text.split('\n') if search_keyword.lower() in line.lower()]
        
        # Display search results
        st.subheader("Search Results")
        if search_results:
            for result in search_results:
                st.write(result)
        else:
            st.write("No matches found.")

# OCR and Document Search Web Application

## Project Overview
This project is a web-based prototype that demonstrates the ability to perform Optical Character Recognition (OCR) on an uploaded image containing text in both Hindi and English. The application allows users to upload an image, choose between two OCR models (EasyOCR or Tesseract), extract text, and perform a keyword search within the extracted text.

The application is built using Streamlit for the frontend and combines EasyOCR and Tesseract as the backend OCR engines.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/naqi72/OCR-and-Document-Search-web-Application-Prototype
    
    ```

2. Install the required dependencies
   ```
   pip install -r requirements.txt
   
   ```

3. Run the web application locally:
    ```
    streamlit run app.py
    ```

## Deployment
The application is deployed at: [LIVE URL HERE]

## Features
-Upload images in popular formats like PNG, JPEG, JPG.

-Choose between EasyOCR and Tesseract models for text extraction.

-Extract text in both Hindi and English.

-Once the text is extracted from the image, it is displayed clearly on the page for easy reading.

-Search for specific keywords in the extracted text, with highlighted results.

-Download extracted text as a plain text file, making it easy to save or share.

-Deployed online for public access.

## Technologies Used

- **Streamlit** for the web application interface.

- **Pillow** for image handling.

- **EasyOCR** and **Tesseract** for OCR functionality.






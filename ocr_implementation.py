import easyocr
import streamlit as st
import json

reader = easyocr.Reader(['en', 'hi'])

def ocr_image(image):
    result = reader.readtext(image, detail=0)
    return result
def extract_text_as_json(extracted_text):
    return json.dumps({'extracted_text': extracted_text}, ensure_ascii=False)


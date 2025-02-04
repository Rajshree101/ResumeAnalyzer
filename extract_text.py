# extract_text.py
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_path):
    try:
        # Extract text from the PDF file
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

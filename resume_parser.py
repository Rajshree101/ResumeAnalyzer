from pdfminer.high_level import extract_text

def extract_resume_data(pdf_path):
    """Extracts text from PDF resume."""
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting resume text: {e}")
        return ""

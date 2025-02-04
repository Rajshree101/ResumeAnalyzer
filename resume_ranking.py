import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_resume_data(file_path):
    resume_text = extract_text_from_pdf(file_path)

    if not resume_text:
        print("No text extracted from PDF.")
        return None

    # Example: Experience extraction
    experience = sum(1 for word in resume_text.split() if word.lower() in ["years", "experience", "worked"])
    print("Experience:", experience)

    # Example: Skills extraction
    skills_keywords = ["python", "java", "c++", "project management", "leadership", "data analysis"]
    num_skills = sum(1 for word in resume_text.split() if word.lower() in skills_keywords)
    print("Skills:", num_skills)

    # Example: Education extraction
    education_keywords = ["b.tech", "mca", "msc", "bsc", "mba"]
    education_score = sum(1 for word in resume_text.split() if word.lower() in education_keywords)
    print("Education:", education_score)

    return experience, num_skills, education_score

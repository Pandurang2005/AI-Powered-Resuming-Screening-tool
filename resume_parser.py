import spacy
from PyPDF2 import PdfReader

nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    doc = nlp(text)
    skills = []
    for token in doc:
        if token.pos_ == 'NOUN' and len(token.text) > 2:
            skills.append(token.text.lower())
    return {'file_path': file_path, 'text': text, 'skills': list(set(skills))}
import os
import docx
import PyPDF2

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_pdf(path):
    text = ""
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def load_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents(folder="data"):
    full_text = ""
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if filename.endswith(".txt"):
            full_text += load_txt(path) + "\n"
        elif filename.endswith(".pdf"):
            full_text += load_pdf(path) + "\n"
        elif filename.endswith(".docx"):
            full_text += load_docx(path) + "\n"
    return full_text

from src.parsing.text_cleaner import clean_text
import PyPDF2
import docx

def parse_jd(file):
    """
    Extract text from Job Description (PDF/DOCX/TXT) and clean it.
    `file` is a Streamlit UploadedFile object.
    """
    text = ""

    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/plain"]:
        if file.type == "text/plain":
            text = file.getvalue().decode("utf-8")
        else:
            doc = docx.Document(file)
            text = "\n".join([p.text for p in doc.paragraphs])
    else:
        text = file.getvalue().decode("utf-8")  # fallback for txt

    return clean_text(text)

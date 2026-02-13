from pypdf import PdfReader

def process_document(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

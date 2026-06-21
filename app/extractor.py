from pypdf import PdfReader
from docx import Document


def extract_text(file_path: str) -> str:
    """
    Reads a file (.pdf, .docx, or .txt) and returns its text content
    as a single clean string.
    """
    if file_path.endswith(".pdf"):
        return _extract_pdf(file_path)
    elif file_path.endswith(".docx"):
        return _extract_docx(file_path)
    elif file_path.endswith(".txt"):
        return _extract_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")


def _extract_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text_parts = []
    for page in reader.pages:
        text_parts.append(page.extract_text())
    return "\n".join(text_parts)


def _extract_docx(file_path: str) -> str:
    doc = Document(file_path)
    text_parts = [para.text for para in doc.paragraphs]
    return "\n".join(text_parts)


def _extract_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
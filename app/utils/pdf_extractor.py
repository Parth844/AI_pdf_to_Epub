import fitz
from app.utils.ocr_handler import extract_text_with_ocr

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    images = []

    for page in doc:
        text = page.get_text()
        if text.strip():
            full_text += text
        else:
            full_text += extract_text_with_ocr(page)

        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            images.append(base_image["image"])

    return full_text, images
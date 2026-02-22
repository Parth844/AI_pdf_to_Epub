import pytesseract
from PIL import Image
import io

def extract_text_with_ocr(page):
    pix = page.get_pixmap()
    img_data = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_data))
    return pytesseract.image_to_string(image)
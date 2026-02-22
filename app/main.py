from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
import os

from app.config import UPLOAD_FOLDER, OUTPUT_FOLDER
from app.utils.pdf_extractor import extract_pdf_content
from app.utils.formatter import clean_text
from app.utils.epub_generator import generate_epub
from app.utils.chapter_splitter import format_paragraph
from app.utils.llm_structure import detect_book_structure, map_sections_to_content


# Create FastAPI app FIRST
app = FastAPI()

# THEN mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text, images = extract_pdf_content(file_path)
    paragraphs = clean_text(text)

    structure = detect_book_structure(paragraphs)
    sections = map_sections_to_content(paragraphs, structure)

    # Format paragraphs properly before EPUB generation
    formatted_chapters = []
    for title, content in sections:
        formatted_content = [format_paragraph(p) for p in content]
        formatted_chapters.append((title, formatted_content))

    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.filename.replace(".pdf", ".epub")
    )

    generate_epub(formatted_chapters, images, output_file)

    return FileResponse(output_file, filename=os.path.basename(output_file))
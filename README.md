# 📚 AI PDF to EPUB Converter

An intelligent PDF-to-EPUB conversion engine powered by LLM-based semantic structure detection.

This project combines rule-based text normalization with AI-driven book parsing to generate clean, publisher-grade EPUB files from raw PDFs.

---

## 🚀 Features

- 🧠 LLM-Based Chapter Detection (NVIDIA LLaMA 3.1)
- 📄 Intelligent front matter parsing (copyright, dedication, etc.)
- 🧹 Advanced PDF text cleaning & normalization
- 💬 Dialogue and quote formatting
- ✨ Automatic scene break detection
- 📖 Proper EPUB spine & TOC generation
- 🌐 FastAPI web interface
- ⚡ Modular and scalable architecture

---

## 🏗 Architecture

PDF Upload  
    ↓  
Text Extraction (PyMuPDF + OCR fallback)  
    ↓  
Text Cleaning & Normalization  
    ↓  
LLM Structure Detection (LLaMA via NVIDIA NIM)  
    ↓  
Section Mapping  
    ↓  
Paragraph Formatting  
    ↓  
EPUB Generation (ebooklib)

Hybrid pipeline:
- Rule-based preprocessing
- LLM-powered structural parsing
- Programmatic EPUB composition

---

## 🛠 Tech Stack

- FastAPI – Web framework
- PyMuPDF (fitz) – PDF extraction
- ebooklib – EPUB generation
- NVIDIA NIM (LLaMA 3.1 70B Instruct) – Structure detection
- Python 3.10+

---

## 📂 Project Structure

pdf2epub/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── utils/
│   │   ├── pdf_extractor.py
│   │   ├── formatter.py
│   │   ├── chapter_splitter.py
│   │   ├── epub_generator.py
│   │   └── llm_structure.py
│   ├── templates/
│   └── static/
│
├── uploads/
├── output/
├── requirements.txt
└── run.py

---

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone https://github.com/Parth844/AI_pdf_to_Epub.git  
cd AI_pdf_to_Epub

---

### 2️⃣ Create Virtual Environment

python -m venv venv  
source venv/bin/activate  

(Windows: venv\\Scripts\\activate)

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Set NVIDIA API Key

Mac/Linux:

export NVIDIA_API_KEY="your_nvidia_api_key"

Windows:

set NVIDIA_API_KEY=your_nvidia_api_key

---

### 5️⃣ Run Server

python run.py

Open in browser:

http://127.0.0.1:8000

Upload a PDF and convert.

---

## 🧠 How LLM Structure Detection Works

Instead of relying only on regex-based rules, this system:

1. Sends initial book content to LLaMA
2. Detects:
   - Front matter sections
   - Chapter titles
   - Section boundaries
3. Returns structured JSON
4. Maps sections back to paragraphs
5. Generates properly separated EPUB chapters

This dramatically improves accuracy over traditional PDF parsing methods.

---

## 📈 Why This Project Is Different

Most PDF → EPUB tools:

- Only extract raw text
- Ignore book semantics
- Fail to detect chapter boundaries properly

This project introduces semantic book structure detection using LLMs, bringing AI into digital publishing workflows.

---

## 🔮 Future Improvements

- Intelligent dialogue continuation detection
- Automatic drop-cap styling
- EPUB 3 accessibility enhancements
- Caching LLM responses
- Multi-book batch processing
- Docker deployment
- Cloud deployment

---

## 🛡 Security

- API keys are loaded via environment variables
- No credentials stored in repository
- .gitignore prevents sensitive data leaks

---

## 📌 Potential Use Cases

- Digital publishing automation
- Academic document restructuring
- Book digitization workflows
- AI-assisted content formatting

---

## 👨‍💻 Author

**Parth Tyagi**  
AI & Tech Enthusiast  
Building intelligent document automation tools.

---

## 📜 License

MIT License (Add a LICENSE file if desired)
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md created successfully!")

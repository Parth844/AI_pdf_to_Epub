# 📚 AI PDF → EPUB Converter

> AI-powered document publishing pipeline that converts raw PDFs into clean, structured, publisher-grade EPUB files using LLM-based semantic parsing.

---

## 🚀 Overview

Traditional PDF-to-EPUB tools rely purely on rule-based extraction, often producing poorly structured outputs with broken chapters, merged paragraphs, and incorrect formatting.

This project introduces a **hybrid AI architecture** that combines:

- Rule-based text normalization
- Semantic structure detection using NVIDIA LLaMA
- Programmatic EPUB composition

The result: significantly cleaner, more structured, and professionally formatted EPUB outputs.

---

## ✨ Key Features

- 🧠 **LLM-Based Chapter Detection** (NVIDIA LLaMA 3.1 70B)
- 📄 Automatic front matter separation (copyright, dedication, etc.)
- 🧹 Advanced PDF text cleaning & normalization
- 💬 Dialogue-aware formatting
- ✨ Scene break detection
- 📖 Proper EPUB spine & Table of Contents generation
- 🌐 FastAPI-powered web interface
- ⚙️ Modular and scalable architecture

---

## 🏗 System Architecture

```
PDF Upload
    ↓
Text Extraction (PyMuPDF + OCR fallback)
    ↓
Text Cleaning & Normalization
    ↓
LLM Structure Detection (NVIDIA NIM - LLaMA 3.1)
    ↓
Section Mapping
    ↓
Paragraph Formatting
    ↓
EPUB Generation (ebooklib)
```

### Hybrid Approach

| Layer | Purpose |
|-------|----------|
| Rule-Based Cleaning | Remove noise, fix broken lines |
| LLM Parsing | Detect chapters & semantic sections |
| Structured Mapping | Align detected sections to text |
| EPUB Builder | Generate production-ready EPUB |

---

## 🛠 Tech Stack

- **FastAPI** – Backend framework
- **PyMuPDF (fitz)** – PDF extraction
- **ebooklib** – EPUB generation
- **NVIDIA NIM (LLaMA 3.1 70B Instruct)** – AI structure detection
- **Python 3.10+**

---

## 📂 Project Structure

```
AI_pdf_to_Epub/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # App configuration
│   │
│   ├── utils/
│   │   ├── pdf_extractor.py   # PDF text + image extraction
│   │   ├── formatter.py       # Text cleaning & normalization
│   │   ├── chapter_splitter.py# Paragraph & formatting logic
│   │   ├── epub_generator.py  # EPUB file creation
│   │   └── llm_structure.py   # LLM-based structure detection
│   │
│   ├── templates/
│   │   └── index.html         # Upload UI
│   │
│   └── static/
│       └── style.css          # Frontend styling
│
├── uploads/                   # Uploaded PDFs (ignored in git)
├── output/                    # Generated EPUB files (ignored in git)
├── requirements.txt
├── run.py                     # Server runner
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/Parth844/AI_pdf_to_Epub.git
cd AI_pdf_to_Epub
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

(Windows: `venv\\Scripts\\activate`)

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure NVIDIA API Key

Mac/Linux:

```
export NVIDIA_API_KEY="your_nvidia_api_key"
```

Windows:

```
set NVIDIA_API_KEY=your_nvidia_api_key
```

### 5️⃣ Run the Application

```
python run.py
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧠 How AI Structure Detection Works

Instead of guessing chapters using fragile regex rules, this system:

1. Sends initial book content to LLaMA
2. Detects:
   - Front matter sections
   - Chapter titles
   - Section boundaries
3. Returns structured JSON
4. Maps structured sections back to text
5. Generates properly separated EPUB pages

This approach improves structural accuracy significantly compared to traditional converters.

---

## 📊 Why This Project Is Different

Most converters:
- Extract raw text only
- Ignore semantic structure
- Fail at chapter boundary detection

This system introduces:
> Semantic-aware document publishing using LLMs.

It behaves more like a **digital publishing engine** than a simple file converter.

---

## 🔮 Future Roadmap

- Advanced dialogue continuation detection
- Drop-cap styling support
- EPUB 3 accessibility enhancements
- Response caching for LLM efficiency
- Batch multi-book processing
- Dockerized deployment
- Cloud hosting (AWS / GCP)

---

## 🔐 Security

- API keys loaded via environment variables
- Sensitive files excluded via `.gitignore`
- No hardcoded credentials

---

## 📌 Potential Use Cases

- Digital publishing automation
- Book digitization pipelines
- Academic document restructuring
- AI-assisted editorial workflows

---

## 👨‍💻 Author

**Parth Tyagi**  
AI & Technology Enthusiast  
Focused on intelligent document automation and AI-driven systems.

---

## 📜 License

MIT License (Add a LICENSE file if desired)
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md updated successfully!")

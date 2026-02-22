import re

def clean_text(text):
    # Normalize line breaks
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Remove watermark
    text = re.sub(r'OceanofPDF\.com', '', text, flags=re.IGNORECASE)
    text = re.sub(r'www\.\S+', '', text)

    # Remove standalone page numbers
    text = re.sub(r'\n\d+\n', '\n', text)

    # Remove repeated spaces
    text = re.sub(r'[ \t]+', ' ', text)

    # Fix broken hyphenated words across lines
    text = re.sub(r'-\n', '', text)

    # Merge lines that break mid sentence
    text = re.sub(
        r'(?<![.!?:"”])\n(?=[a-zA-Z])',
        ' ',
        text
    )

    # Fix drop-cap chapter style like:
    # O
    # A New Beginning in Uncertain Times
    text = re.sub(
        r'\n([A-Z])\n([A-Z][^\n]+)',
        r'\n\1 \2',
        text
    )

    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Split into paragraphs
    paragraphs = [
        p.strip()
        for p in text.split('\n\n')
        if p.strip()
    ]

    return paragraphs
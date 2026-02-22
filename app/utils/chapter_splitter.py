import re


def is_chapter_start(paragraphs, index):
    if index + 1 >= len(paragraphs):
        return False

    first = paragraphs[index].strip()
    second = paragraphs[index + 1].strip()

    return (
        len(first) == 1
        and first.isupper()
        and len(second.split()) > 1
    )


def format_paragraph(p):
    p = p.strip()

    if not p:
        return ""

    # Scene break
    if p in ["*", "***", "—", "- - -"]:
        return '<p class="scene-break">***</p>'

    # Dialogue
    if p.startswith('"') or p.startswith("“"):
        return f'<p class="dialogue">{p}</p>'

    # Quote block
    if p.startswith("“") and p.endswith("”"):
        return f'<blockquote>{p}</blockquote>'

    # Short poetic lines
    if len(p.split()) <= 6:
        return f'<p class="short-line">{p}</p>'

    return f'<p class="para">{p}</p>'


def split_into_chapters(paragraphs):

    chapters = []
    current_title = None
    current_content = []

    i = 0

    while i < len(paragraphs):

        if is_chapter_start(paragraphs, i):

            if current_title:
                chapters.append((current_title, current_content))

            letter = paragraphs[i].strip()
            title_line = paragraphs[i + 1].strip()

            current_title = f"{letter} {title_line}"
            current_content = []

            i += 2
            continue

        # If no chapter started yet → treat as front matter
        if current_title is None:
            if not chapters:
                current_title = "Front Matter"
                current_content = []

        current_content.append(format_paragraph(paragraphs[i]))
        i += 1

    if current_content:
        chapters.append((current_title, current_content))

    return chapters
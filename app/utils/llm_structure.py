import json
import os
from openai import OpenAI

# NVIDIA NIM endpoint (OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)


def detect_book_structure(paragraphs):
    """
    Uses LLM to detect chapters and front matter.
    Returns structured list of sections.
    """

    # Limit size to avoid token explosion
    sample_text = "\n\n".join(paragraphs[:200])

    prompt = f"""
You are a book structure parser.

Analyze the following book text and detect:

- Front matter sections (copyright, dedication, etc.)
- Real chapter titles
- The start of each chapter

Return JSON only in this format:

[
  {{
    "type": "front_matter" or "chapter",
    "title": "Section Title",
    "content_start_snippet": "First few words of that section"
  }}
]

Text:
{sample_text}
"""

    try:
        response = client.chat.completions.create(
            model="meta/llama-3.1-70b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=2000
        )

        result = response.choices[0].message.content
        return json.loads(result)

    except Exception as e:
        print("LLM Error:", e)
        # Fallback: treat entire book as one section
        return [
            {
                "type": "chapter",
                "title": "Book",
                "content_start_snippet": paragraphs[0] if paragraphs else ""
            }
        ]

def map_sections_to_content(paragraphs, structure):
    sections = []

    for i, section in enumerate(structure):
        title = section["title"]
        snippet = section["content_start_snippet"]

        # Find where this snippet appears
        start_index = next(
            (idx for idx, p in enumerate(paragraphs) if snippet in p),
            None
        )

        if start_index is None:
            continue

        if i + 1 < len(structure):
            next_snippet = structure[i + 1]["content_start_snippet"]
            end_index = next(
                (idx for idx, p in enumerate(paragraphs) if next_snippet in p),
                len(paragraphs)
            )
        else:
            end_index = len(paragraphs)

        content = paragraphs[start_index:end_index]
        sections.append((title, content))

    return sections
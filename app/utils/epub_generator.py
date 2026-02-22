from ebooklib import epub
import os

def generate_epub(chapters, images, output_path):
    book = epub.EpubBook()

    book.set_identifier("pdf2epub")
    book.set_title("Converted Book")
    book.set_language("en")
    book.add_author("Unknown")

    # Safe cover handling
    cover_path = "app/static/cover.jpg"
    if os.path.exists(cover_path):
        with open(cover_path, "rb") as f:
            book.set_cover("cover.jpg", f.read())

    # CSS Styling
    style = """
    body {
        font-family: serif;
        line-height: 1.6;
        margin-left: 5%;
        margin-right: 5%;
    }

    h1.chapter-title {
        text-align: center;
        margin-top: 3em;
        margin-bottom: 2em;
        page-break-before: always;
    }

    p.para {
        text-indent: 1.5em;
        margin-top: 0.6em;
    }

    p.dialogue {
        margin-left: 1em;
        text-indent: 0;
    }

    p.short-line {
        text-align: center;
        font-style: italic;
        text-indent: 0;
    }

    p.scene-break {
        text-align: center;
        margin: 2em 0;
    }

    blockquote {
        margin-left: 2em;
        font-style: italic;
    }
    """

    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/style.css",
        media_type="text/css",
        content=style
    )

    book.add_item(nav_css)

    epub_chapters = []

    for i, (title, content_list) in enumerate(chapters):

        chapter = epub.EpubHtml(
            title=title,
            file_name=f'chapter_{i}.xhtml',
            lang='en'
        )

        chapter_html = f'<h1 class="chapter-title">{title}</h1>\n'

        for p in content_list:
            chapter_html += p + "\n"

        chapter.content = f"""
        <html>
        <head>
        <link href="style/style.css" rel="stylesheet" type="text/css"/>
        </head>
        <body>
        {chapter_html}
        </body>
        </html>
        """

        chapter.add_item(nav_css)
        book.add_item(chapter)
        epub_chapters.append(chapter)

    book.toc = tuple(epub_chapters)
    book.spine = ['nav'] + epub_chapters

    book.add_item(epub.EpubNav())
    book.add_item(epub.EpubNcx())

    epub.write_epub(output_path, book)
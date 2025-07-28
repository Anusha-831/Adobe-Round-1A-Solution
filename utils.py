# utils.py

import fitz  # PyMuPDF
from collections import Counter, defaultdict

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_headings = []
    font_stats = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text) < 2:
                        continue
                    size = span["size"]
                    font = span["font"]
                    font_stats.append(size)
                    all_headings.append({
                        "text": text,
                        "font_size": size,
                        "font": font,
                        "page": page_num
                    })

    # Step 1: Find top 4 unique font sizes
    font_counter = Counter([round(f["font_size"]) for f in all_headings])
    most_common_fonts = sorted(font_counter.items(), key=lambda x: -x[0])  # Descending by size

    if len(most_common_fonts) < 3:
        raise Exception("Not enough font variety to detect heading levels")

    size_to_level = {}
    level_names = ["H1", "H2", "H3"]
    for i, (size, _) in enumerate(most_common_fonts[:3]):
        size_to_level[size] = level_names[i]

    # Step 2: Extract title (largest text on page 1)
    title = ""
    for h in all_headings:
        if h["page"] == 1 and round(h["font_size"]) == most_common_fonts[0][0]:
            title = h["text"]
            break

    # Step 3: Build outline
    outline = []
    for h in all_headings:
        size = round(h["font_size"])
        if size in size_to_level:
            outline.append({
                "level": size_to_level[size],
                "text": h["text"],
                "page": h["page"]
            })

    return {
        "title": title,
        "outline": outline
    }
# generate_sample_pdf_and_json.py

from reportlab.pdfgen import canvas
import os
import json

# Paths
os.makedirs("sample_data", exist_ok=True)
pdf_path = "sample_data/sample.pdf"
json_path = "sample_data/sample.json"

# Sample heading structure
headings = [
    ("Introduction to GenAI", "title", 1),
    ("Introduction", "H1", 1),
    ("What is GenAI?", "H2", 1),
    ("History", "H3", 1),
    ("Applications", "H3", 2),
    ("Why Now?", "H2", 2),
    ("Techniques", "H1", 3),
    ("GANs", "H2", 3),
    ("Transformers", "H2", 3),
    ("Conclusion", "H1", 4),
]

# --- Create PDF ---
c = canvas.Canvas(pdf_path)
current_page = 1

for text, level, page_num in headings:
    if page_num != current_page:
        c.showPage()
        current_page = page_num

    # Set font size based on heading level
    if level == "title":
        c.setFont("Helvetica-Bold", 24)
    elif level == "H1":
        c.setFont("Helvetica-Bold", 20)
    elif level == "H2":
        c.setFont("Helvetica-Bold", 16)
    elif level == "H3":
        c.setFont("Helvetica", 14)

    y_pos = 750 - (50 * (page_num % 5))
    c.drawString(100, y_pos, text)

c.save()

# --- Create JSON ground truth ---
json_output = {
    "title": "Introduction to GenAI",
    "outline": [
        { "level": lvl, "text": text, "page": pg }
        for (text, lvl, pg) in headings if lvl != "title"
    ]
}

with open(json_path, "w") as f:
    json.dump(json_output, f, indent=2)

print("✅ sample.pdf and sample.json created in sample_data/")
# main.py

import os
import json
from utils import extract_outline_from_pdf

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]

for pdf_file in pdf_files:
    input_path = os.path.join(INPUT_DIR, pdf_file)
    output_path = os.path.join(OUTPUT_DIR, pdf_file.replace(".pdf", ".json"))

    print(f"Processing {pdf_file}...")
    result = extract_outline_from_pdf(input_path)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Output written to {output_path}")
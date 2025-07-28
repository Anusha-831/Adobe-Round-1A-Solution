import os
import json
import time
from utils import extract_outline_from_pdf

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Create output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get all PDF files
pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]

print(f"\n📄 Found {len(pdf_files)} PDF file(s) to process...\n")

# Track stats
total_headings = 0
total_time = 0.0
results = []

# Process each PDF
for idx, pdf_file in enumerate(pdf_files, start=1):
    input_path = os.path.join(INPUT_DIR, pdf_file)
    output_path = os.path.join(OUTPUT_DIR, pdf_file.replace(".pdf", ".json"))

    print(f"{idx}/{len(pdf_files)} | 📘 {pdf_file}", end="")

    start = time.time()
    result = extract_outline_from_pdf(input_path)
    duration = round(time.time() - start, 2)

    heading_count = len(result["outline"])
    total_headings += heading_count
    total_time += duration

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f" | 📝 Headings: {heading_count} | ⏱️ Time: {duration}s")
    results.append((pdf_file, heading_count, duration))

# Final summary
print("\n✅ Batch Processing Completed!\n📊 Results Summary:")
print(f"🧾 PDFs Processed     : {len(pdf_files)}")
print(f"🧠 Total Headings     : {total_headings}")
print(f"⏲️  Total Time Taken  : {round(total_time, 2)} seconds")
print(f"📈 Avg Time per PDF   : {round(total_time / len(pdf_files), 2)} seconds\n")

print("🔽 Breakdown per file:")
for file, count, time_taken in results:
    print(f"   📄 {file:30} | 📝 {count:3} headings | ⏱️ {time_taken:5}s")

print("\n📁 JSON output files saved in /output folder.\n")

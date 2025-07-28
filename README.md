# 🧠 PDF Outline Extractor – Round 1A Solution
Adobe India Hackathon 2025 – Round 1A  
Team: Innoventors  
Contributors: Koyyada Anusha, Muddassir Shakhan

---

## 📌 Problem Statement

Build a tool that extracts a structured outline from academic PDFs, including:
- Title
- Headings (H1 to H5)
- Page number

Constraints:
- No API calls or external web requests
- Works offline inside a Docker container
- Executes under 10 seconds for a 50-page PDF
- Clean heading hierarchy and generalization (no hardcoding)
- Bonus: Support for multilingual PDFs (optional)

---

## ✅ Approach

We developed a fully offline, Dockerized Python solution using the following strategy:

### 📂 Heading Detection
- Extracts all text spans using PyMuPDF (fitz)
- Groups spans by font size
- Assigns heading levels (H1 to H5) to the top font sizes dynamically
- Filters out non-meaningful or noisy text using a custom is_meaningful() logic

### 🧠 Title Detection
- Picks the largest heading on Page 1 as the document title

### 🔍 Noise Filtering
- Removes single-character or gibberish symbols from headings
- Ensures clean and readable outline output

---

## ⚙️ Models / Libraries Used

- PyMuPDF (fitz) – for PDF parsing
- json – for generating output
- os, collections– standard Python utilities

> 💡 Note: No pretrained models or third-party APIs used to stay within the model size/runtime constraints.

---

## 🐳 How to Build and Run

### 1. Clone and move into the repo

git clone https://github.com/Anusha-831/adobe-round1a-solution.git
cd adobe-round1a-solution

### 2. Place input files

Put your test PDFs into the /input directory. For example:

input/
├── sample.pdf
├── your_custom_test.pdf

### 3. Build Docker Image

docker build --platform linux/amd64 -t pdf-outline-extractor:final .

### 4. Run the container

docker run --rm -v "${PWD}/input:/app/input" -v "${PWD}/output:/app/output" --network none pdf-outline-extractor:final

> Output will be written to /output folder as .json files.

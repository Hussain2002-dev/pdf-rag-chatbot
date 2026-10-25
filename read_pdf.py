
from pypdf import PdfReader

pdf_path = "data/sample.pdf"
reader = PdfReader(pdf_path)

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    print(f"\n--- Page {page_number} ---\n")
    print(text)

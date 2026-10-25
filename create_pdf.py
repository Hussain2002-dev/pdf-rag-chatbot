
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path

# Create the data folder if it does not exist
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

pdf_path = data_folder / "sample.pdf"

# Information for our RAG chatbot to learn from
content = [
    "Introduction to Python Programming",
    "",
    "Python is a high-level programming language.",
    "It is widely used for web development, automation, data science, and AI.",
    "",
    "What is RAG?",
    "RAG stands for Retrieval-Augmented Generation.",
    "It retrieves relevant information from documents before generating an answer.",
    "This helps an AI chatbot answer questions using the provided information.",
    "",
    "What is ChromaDB?",
    "ChromaDB is a vector database used to store and search text embeddings.",
    "It helps retrieve document chunks that are relevant to a user's question.",
    "",
    "What is an API?",
    "An API allows different software applications to communicate with each other.",
    "The Groq API allows applications to send prompts to supported AI models.",
    "",
    "How does a PDF chatbot work?",
    "First, it extracts text from a PDF document.",
    "Next, it splits the text into smaller chunks.",
    "Then, it stores the chunks in a searchable database.",
    "When a user asks a question, relevant chunks are retrieved.",
    "Finally, an AI model uses the retrieved information to answer the question.",
]

pdf = canvas.Canvas(str(pdf_path), pagesize=letter)
width, height = letter
x = 50
y = height - 60

for line in content:
    if y < 60:
        pdf.showPage()
        y = height - 60

    pdf.setFont("Helvetica-Bold" if line in [
        "Introduction to Python Programming",
        "What is RAG?",
        "What is ChromaDB?",
        "What is an API?",
        "How does a PDF chatbot work?",
    ] else "Helvetica", 11)

    pdf.drawString(x, y, line)
    y -= 22

pdf.save()

print(f"PDF created successfully: {pdf_path}")

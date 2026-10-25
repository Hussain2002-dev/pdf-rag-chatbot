
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from groq import Groq

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY .env file mein nahi mili.")

# Initialize Groq
groq_client = Groq(api_key=api_key)
MODEL = "openai/gpt-oss-20b"

# Step 1: Read the PDF
pdf_path = "data/sample.pdf"
reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    text += page.extract_text() or ""

if not text.strip():
    raise ValueError("PDF se text nahi mila.")

print("PDF successfully read!")

# Step 2: Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = splitter.split_text(text)
print(f"Created {len(chunks)} text chunks.")

# Step 3: Store chunks in ChromaDB
db_client = chromadb.PersistentClient(path="./chroma_db")
collection = db_client.get_or_create_collection(
    name="pdf_documents"
)

collection.upsert(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks
)
print("Document chunks stored in ChromaDB!")

# Step 4: Ask questions
print("\nPDF RAG Chatbot is ready!")
print("PDF ke baare mein sawal poochho. Exit ke liye 'quit' likho.\n")

while True:
    question = input("You: ").strip()

    if question.lower() in ["quit", "exit"]:
        print("Allah Hafiz!")
        break

    if not question:
        continue

    # Retrieve the 3 most relevant chunks
    results = collection.query(
        query_texts=[question],
        n_results=min(3, collection.count())
    )

    retrieved_chunks = results["documents"][0]

    if not retrieved_chunks:
        print("PDF mein relevant information nahi mili.\n")
        continue

    context = "\n\n".join(retrieved_chunks)

    # Generate an answer using the retrieved context
    response = groq_client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful PDF question-answering assistant. "
                    "Answer using only the supplied PDF context. "
                    "If the answer is not in the context, say that "
                    "the PDF does not provide that information. "
                    "Do not invent facts."
                )
            },
            {
                "role": "user",
                "content": (
                    f"PDF context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ],
        max_tokens=300
    )

    print("\nAssistant:", response.choices[0].message.content)
    print()

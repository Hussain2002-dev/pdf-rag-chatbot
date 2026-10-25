
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# Step 1: Read text from the PDF
reader = PdfReader("data/sample.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text() or ""

# Step 2: Split text into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print(f"Total chunks created: {len(chunks)}")

# Step 3: Create a persistent ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="pdf_documents"
)

# Step 4: Store chunks in ChromaDB
if chunks:
    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks
    )

print("Chunks stored successfully in ChromaDB!")

# Step 5: Show the stored chunks
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

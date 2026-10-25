# PDF RAG Chatbot

This is a project I built while learning Python and AI. It is a simple chatbot that can answer questions about a PDF file.

I used RAG (Retrieval-Augmented Generation) so the chatbot can find relevant information from the PDF and use it to answer questions.

## What does this project do?

- Reads text from a PDF file.
- Splits the text into smaller chunks.
- Saves the chunks in ChromaDB.
- Finds relevant information when a user asks a question.
- Uses the Groq API to generate an answer.

## Technologies I used

- Python
- ChromaDB
- Groq API
- PyPDF
- LangChain Text Splitters

## Project Files

- `create_pdf.py` – Creates a sample PDF.
- `read_pdf.py` – Reads text from the PDF.
- `store_chunks.py` – Splits the text and stores it in ChromaDB.
- `main.py` – Runs the chatbot.
- `data/sample.pdf` – Sample PDF used for testing.

## How to Run

First, clone this repository:

```bash
git clone https://github.com/Hussain2002-dev/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install chromadb pypdf groq python-dotenv langchain-text-splitters
```

Create a `.env` file in the project folder and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the scripts:

```bash
python store_chunks.py
python main.py
```

Now you can ask questions about the PDF through the terminal.

## What I learned

While building this project, I learned how to read PDF files, split text into chunks, store information in a vector database, and use an AI model to answer questions.

This is one of my learning projects, and I plan to improve it as I learn more about Python and AI.

## GitHub

[View my repository](https://github.com/Hussain2002-dev/pdf-rag-chatbot)

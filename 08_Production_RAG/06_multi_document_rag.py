"""
06_multi_document_rag.py

Index multiple PDFs into a single FAISS vector store.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = Path("data")

documents = []

for pdf_file in DATA_DIR.glob("*.pdf"):

    loader = PyPDFLoader(str(pdf_file))

    docs = loader.load()

    for doc in docs:
        doc.metadata["source"] = pdf_file.name

    documents.extend(docs)

print(f"Loaded {len(documents)} pages")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = splitter.split_documents(documents)

print(f"Chunks: {len(chunks)}")

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(
    chunks,
    embedding,
)

db.save_local("multi_faiss")

print("Multi-document FAISS created.")
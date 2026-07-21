"""
05_load_faiss.py

Load an existing FAISS vector store.
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

print(db.index.ntotal)
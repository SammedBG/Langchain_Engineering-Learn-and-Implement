"""
01_mmr_retrieval.py

Compare Similarity Search and MMR Retrieval.
"""

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

query = "Explain LangChain"

# -----------------------------
# Similarity Search
# -----------------------------

print("=" * 60)
print("SIMILARITY SEARCH")
print("=" * 60)

similarity_retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 4,
    },
)

documents = similarity_retriever.invoke(query)

for i, document in enumerate(documents, start=1):
    print(f"\nDocument {i}")
    print(document.page_content[:300])

# -----------------------------
# MMR Search
# -----------------------------

print("\n" + "=" * 60)
print("MMR SEARCH")
print("=" * 60)

mmr_retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 20,
        "lambda_mult": 0.5,
    },
)

documents = mmr_retriever.invoke(query)

for i, document in enumerate(documents, start=1):
    print(f"\nDocument {i}")
    print(document.page_content[:300])
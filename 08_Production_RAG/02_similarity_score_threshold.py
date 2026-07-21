"""
02_similarity_score_threshold.py

Retrieve only documents above a similarity score threshold.
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

retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "score_threshold": 0.80,
        "k": 5,
    },
)

documents = retriever.invoke(query)

print(f"Retrieved {len(documents)} document(s)\n")

for index, document in enumerate(documents, start=1):
    print(f"Document {index}")
    print("-" * 50)
    print(document.page_content[:300])
    print()
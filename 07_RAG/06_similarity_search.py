
"""
Searching similar chunks.
"""

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

results = db.similarity_search(
    "What is LCEL?",
    k=3,
)

for document in results:
    print(document.page_content)
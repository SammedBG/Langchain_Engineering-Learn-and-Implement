
"""
Using a Retriever.
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

retriever = db.as_retriever()

documents = retriever.invoke(
    "Explain LCEL"
)

for doc in documents:
    print(doc.page_content)
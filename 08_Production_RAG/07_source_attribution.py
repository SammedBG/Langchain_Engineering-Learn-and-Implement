"""
07_source_attribution.py

Display retrieved sources alongside the answer.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "multi_faiss",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever(
    search_kwargs={"k": 4}
)

question = "Explain LCEL."

documents = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in documents
)

prompt = ChatPromptTemplate.from_template(
    """
Answer only from the provided context.

Context:
{context}

Question:
{question}
"""
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

chain = prompt | llm

response = chain.invoke(
    {
        "context": context,
        "question": question,
    }
)

print("=" * 60)
print("ANSWER")
print("=" * 60)
print(response.content)

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

seen = set()

for doc in documents:

    source = doc.metadata.get("source", "Unknown")

    page = doc.metadata.get("page", "Unknown")

    key = (source, page)

    if key not in seen:
        seen.add(key)
        print(f"{source} (Page {page})")
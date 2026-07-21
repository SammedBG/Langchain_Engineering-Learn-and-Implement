"""
08_streaming_rag.py

Streaming responses from a Retrieval Chain.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_classic.chains import create_retrieval_chain

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "multi_faiss",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """
Answer only from the given context.

Context:
{context}

Question:
{input}
"""
)

document_chain = create_stuff_documents_chain(
    llm,
    prompt,
)

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain,
)

question = "Explain LangChain."

for chunk in retrieval_chain.stream(
    {
        "input": question,
    }
):
    print(chunk)
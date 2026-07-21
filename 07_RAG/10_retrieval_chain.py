"""
10_retrieval_chain.py

Complete Retrieval Chain Example.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """
Answer the question only from the provided context.

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

response = retrieval_chain.invoke(
    {
        "input": "What is LangChain?"
    }
)

print(response["answer"])
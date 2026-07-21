
"""
Manual LCEL RAG Pipeline.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

prompt = ChatPromptTemplate.from_template(
    """
Answer only from the context.

Context:
{context}

Question:
{question}
"""
)

chain = (
    {
        "context": retriever,
        "question": lambda x: x,
    }
    | prompt
    | llm
    | StrOutputParser()
)

print(
    chain.invoke(
        "Explain LangChain."
    )
)
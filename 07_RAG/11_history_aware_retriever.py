"""
11_history_aware_retriever.py

Building a History Aware Retriever.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.prompts import MessagesPlaceholder

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

from langchain_classic.chains.history_aware_retriever import (
    create_history_aware_retriever,
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
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

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Generate a search query from the conversation.",
        ),
        MessagesPlaceholder("chat_history"),
        (
            "human",
            "{input}",
        ),
    ]
)

history_retriever = create_history_aware_retriever(
    llm,
    retriever,
    prompt,
)

chat_history = [
    HumanMessage(
        content="Tell me about LangChain."
    ),
    AIMessage(
        content="LangChain is a framework for building LLM applications."
    ),
]

documents = history_retriever.invoke(
    {
        "chat_history": chat_history,
        "input": "What about LCEL?",
    }
)

for document in documents:
    print(document.page_content)
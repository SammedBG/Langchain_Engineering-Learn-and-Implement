"""
12_conversational_rag.py

Complete Conversational RAG Chatbot.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_classic.chains import create_retrieval_chain

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_classic.chains.history_aware_retriever import (
    create_history_aware_retriever,
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

context_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Generate a search query using the conversation.",
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
    context_prompt,
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Answer only using the retrieved context.

Context:
{context}
""",
        ),
        MessagesPlaceholder("chat_history"),
        (
            "human",
            "{input}",
        ),
    ]
)

document_chain = create_stuff_documents_chain(
    llm,
    qa_prompt,
)

retrieval_chain = create_retrieval_chain(
    history_retriever,
    document_chain,
)

store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


chatbot = RunnableWithMessageHistory(
    retrieval_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

print("Conversational RAG Chatbot")
print("Type 'exit' to quit.\n")

while True:
    question = input("You : ")

    if question.lower() == "exit":
        break

    response = chatbot.invoke(
        {
            "input": question,
        },
        config={
            "configurable": {
                "session_id": "user1",
            }
        },
    )

    print("\nAI :", response["answer"])
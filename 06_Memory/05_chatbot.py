"""
05_chatbot.py

A simple conversational chatbot using memory.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ]
)

chain = prompt | llm | StrOutputParser()

store = {}


def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

print("Type 'exit' to quit.\n")

while True:
    question = input("You : ")

    if question.lower() == "exit":
        break

    answer = chatbot.invoke(
        {
            "question": question,
        },
        config={
            "configurable": {
                "session_id": "sammed",
            }
        },
    )

    print("AI :", answer)
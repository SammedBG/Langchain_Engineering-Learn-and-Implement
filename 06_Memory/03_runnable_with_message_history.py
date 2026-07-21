"""
03_runnable_with_message_history.py

Using RunnableWithMessageHistory.
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
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ]
)

chain = prompt | llm | StrOutputParser()

store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


conversation = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

while True:
    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    response = conversation.invoke(
        {
            "question": question,
        },
        config={
            "configurable": {
                "session_id": "user1",
            }
        },
    )

    print("AI :", response)
"""
01_manual_chat_history.py

Managing chat history manually.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

history = [
    SystemMessage(
        content="You are a helpful assistant."
    )
]

while True:
    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    history.append(
        HumanMessage(content=question)
    )

    response = llm.invoke(history)

    print("AI :", response.content)

    history.append(
        AIMessage(content=response.content)
    )
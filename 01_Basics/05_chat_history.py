"""
05_chat_history.py

Maintaining conversation history manually.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    history = [
        SystemMessage(
            content="You are a helpful AI assistant."
        )
    ]

    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        history.append(HumanMessage(content=question))

        response = llm.invoke(history)

        print(f"\nAI: {response.content}\n")

        history.append(AIMessage(content=response.content))


if __name__ == "__main__":
    main()
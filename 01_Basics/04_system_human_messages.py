"""
04_system_human_messages.py

Using SystemMessage and HumanMessage with a Chat Model.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    messages = [
        SystemMessage(
            content="You are an expert Python teacher. Answer in simple language."
        ),
        HumanMessage(
            content="Explain decorators."
        ),
    ]

    response = llm.invoke(messages)

    print(response.content)


if __name__ == "__main__":
    main()
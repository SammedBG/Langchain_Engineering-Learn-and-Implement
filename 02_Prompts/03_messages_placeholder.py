"""
03_messages_placeholder.py

Using MessagesPlaceholder to include chat history in a prompt.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant.",
            ),
            MessagesPlaceholder("chat_history"),
            (
                "human",
                "{input}",
            ),
        ]
    )

    chat_history = [
        HumanMessage(content="My name is Sammed."),
        AIMessage(content="Nice to meet you, Sammed!"),
        HumanMessage(content="I am learning LangChain."),
        AIMessage(content="That's great!"),
    ]

    chain = prompt | llm

    response = chain.invoke(
        {
            "chat_history": chat_history,
            "input": "What is my name and what am I learning?",
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()
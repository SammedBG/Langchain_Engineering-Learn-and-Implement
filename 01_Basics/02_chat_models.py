"""
02_chat_models.py

Understanding Chat Models in LangChain.
"""

from dotenv import load_dotenv
from langchain_groq import ChatGroq


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    print(f"Model: {llm.model_name}")
    print("-" * 50)

    response = llm.invoke("Explain what a Chat Model is in 5 lines.")

    print(response.content)


if __name__ == "__main__":
    main()
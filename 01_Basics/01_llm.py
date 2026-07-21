"""
01_llm.py

Initialize a ChatGroq model and invoke it with a simple prompt.
"""

from dotenv import load_dotenv
from langchain_groq import ChatGroq


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    response = llm.invoke("What is Artificial Intelligence?")

    print(response.content)


if __name__ == "__main__":
    main()
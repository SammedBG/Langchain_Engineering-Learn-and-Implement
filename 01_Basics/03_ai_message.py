"""
03_ai_message.py

Understanding the AIMessage object returned by Chat Models.
"""

from dotenv import load_dotenv
from langchain_groq import ChatGroq


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    response = llm.invoke("What is Machine Learning?")

    print("Complete AIMessage Object:\n")
    print(response)

    print("\n" + "=" * 60)

    print("\nContent:\n")
    print(response.content)

    print("\n" + "=" * 60)

    print("\nResponse Metadata:\n")
    print(response.response_metadata)

    print("\n" + "=" * 60)

    print("\nToken Usage:\n")
    print(response.usage_metadata)

    print("\n" + "=" * 60)

    print("\nMessage Type:")
    print(response.type)

    print("\n" + "=" * 60)

    print("\nMessage ID:")
    print(response.id)


if __name__ == "__main__":
    main()
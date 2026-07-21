"""
04_chain_invoke_batch_stream.py

Different ways to execute an LCEL chain:
1. invoke()
2. batch()
3. stream()
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple words."
    )

    chain = prompt | llm | StrOutputParser()

    print("=" * 60)
    print("invoke()")
    print("=" * 60)

    response = chain.invoke(
        {
            "topic": "Python Generators"
        }
    )

    print(response)

    print("\n" + "=" * 60)
    print("batch()")
    print("=" * 60)

    responses = chain.batch(
        [
            {"topic": "Python"},
            {"topic": "Java"},
            {"topic": "JavaScript"},
            {"topic": "Rust"},
        ]
    )

    for index, result in enumerate(responses, start=1):
        print(f"\nResponse {index}")
        print(result)

    print("\n" + "=" * 60)
    print("stream()")
    print("=" * 60)

    for chunk in chain.stream(
        {
            "topic": "LangChain"
        }
    ):
        print(chunk, end="", flush=True)

    print()


if __name__ == "__main__":
    main()
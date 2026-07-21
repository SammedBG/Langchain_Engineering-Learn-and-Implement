"""
05_chain_steps.py

Inspecting the individual components of an LCEL chain.
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
        "Explain {topic} in simple language."
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    print("=" * 60)
    print("CHAIN")
    print("=" * 60)
    print(chain)

    print("\n" + "=" * 60)
    print("CHAIN STEPS")
    print("=" * 60)

    for index, step in enumerate(chain.steps, start=1):
        print(f"Step {index}: {step}")

    print("\n" + "=" * 60)
    print("EXECUTION")
    print("=" * 60)

    response = chain.invoke(
        {
            "topic": "Chain Execution in LCEL"
        }
    )

    print(response)


if __name__ == "__main__":
    main()
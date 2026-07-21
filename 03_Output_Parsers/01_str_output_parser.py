"""
01_str_output_parser.py

Using StrOutputParser to convert AIMessage into a plain string.
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

    parser = StrOutputParser()

    chain = prompt | llm | parser

    response = chain.invoke(
        {
            "topic": "Vector Databases",
        }
    )

    print(response)
    print(type(response))


if __name__ == "__main__":
    main()
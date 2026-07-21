"""
01_pipe_operator.py

Using the LCEL Pipe Operator (|) to chain components together.
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
        "Explain {topic} in simple terms."
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    response = chain.invoke(
        {
            "topic": "LangChain Expression Language (LCEL)"
        }
    )

    print(response)


if __name__ == "__main__":
    main()
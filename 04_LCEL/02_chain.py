"""
02_chain.py

Creating a simple LCEL chain using Prompt -> LLM -> Output Parser.
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
        """
You are an expert {domain} teacher.

Explain {topic} in simple language.
"""
    )

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(
        {
            "domain": "Python",
            "topic": "Decorators",
        }
    )

    print(response)


if __name__ == "__main__":
    main()
    
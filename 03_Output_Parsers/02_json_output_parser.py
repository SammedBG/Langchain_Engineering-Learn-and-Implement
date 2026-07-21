"""
02_json_output_parser.py

Using JsonOutputParser to get structured JSON output from an LLM.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    parser = JsonOutputParser()

    prompt = ChatPromptTemplate.from_template(
        """
Give the response in JSON format.

{format_instructions}

Topic: {topic}
"""
    )

    chain = prompt | llm | parser

    response = chain.invoke(
        {
            "topic": "Python",
            "format_instructions": parser.get_format_instructions(),
        }
    )

    print(response)
    print(type(response))


if __name__ == "__main__":
    main()
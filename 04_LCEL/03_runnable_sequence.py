"""
03_runnable_sequence.py

Creating an LCEL chain using RunnableSequence.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


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

    chain = RunnableSequence(
        first=prompt,
        middle=[llm],
        last=parser,
    )

    response = chain.invoke(
        {
            "topic": "RunnableSequence"
        }
    )

    print(response)


if __name__ == "__main__":
    main()
"""
02_chat_prompt_template.py

Using ChatPromptTemplate to create structured chat prompts.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate


def main():
    load_dotenv()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert {domain} teacher.",
            ),
            (
                "human",
                "Explain {topic} in simple words.",
            ),
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "domain": "Python",
            "topic": "Decorators",
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()
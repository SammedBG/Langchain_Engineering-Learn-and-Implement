"""
01_prompt_template.py

Using PromptTemplate to create dynamic prompts.
"""

from langchain_core.prompts import PromptTemplate


def main():
    prompt = PromptTemplate.from_template(
        """
You are an expert {domain} teacher.

Explain {topic} in simple words.
"""
    )

    formatted_prompt = prompt.invoke(
        {
            "domain": "Python",
            "topic": "Decorators",
        }
    )

    print(formatted_prompt.text)


if __name__ == "__main__":
    main()
from dotenv import load_dotenv

from langchain_core.tools import tool

from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent

load_dotenv()


@tool
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


@tool
def reverse_text(text: str) -> str:
    """Reverses the provided text."""
    return text[::-1]


@tool
def word_count(text: str) -> int:
    """Counts the number of words in a sentence."""
    return len(text.split())


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

agent = create_react_agent(
    model=llm,
    tools=[
        add,
        reverse_text,
        word_count,
    ],
)

response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "Reverse LangChain"
            )
        ]
    }
)

print(response["messages"][-1].content)
from dotenv import load_dotenv

from langchain_core.tools import tool

from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

agent = create_react_agent(
    model=llm,
    tools=[multiply],
)

for event in agent.stream(
    {
        "messages": [
            (
                "user",
                "Multiply 25 by 18"
            )
        ]
    },
    stream_mode="updates",
):
    print(event)
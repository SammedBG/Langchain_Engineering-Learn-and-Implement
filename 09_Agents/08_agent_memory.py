from dotenv import load_dotenv

from langchain_core.tools import tool

from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent

from langgraph.checkpoint.memory import MemorySaver

load_dotenv()


@tool
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

memory = MemorySaver()

agent = create_react_agent(
    model=llm,
    tools=[add],
    checkpointer=memory,
)

config = {
    "configurable": {
        "thread_id": "session_1"
    }
}

response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "My name is Sammed."
            )
        ]
    },
    config=config,
)

print(response["messages"][-1].content)

response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "What is my name?"
            )
        ]
    },
    config=config,
)

print(response["messages"][-1].content)
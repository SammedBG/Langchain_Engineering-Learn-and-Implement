from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    name: str
    greeting: str
    message: str


def create_greeting(state: State):
    return {
        "greeting": f"Hello {state['name']}"
    }


def create_message(state: State):
    return {
        "message": state["greeting"] + ", welcome to LangGraph!"
    }


builder = StateGraph(State)

builder.add_node("create_greeting", create_greeting)
builder.add_node("create_message", create_message)

builder.add_edge(START, "create_greeting")
builder.add_edge("create_greeting", "create_message")
builder.add_edge("create_message", END)

graph = builder.compile()

result = graph.invoke(
    {
        "name": "Sammed",
        "greeting": "",
        "message": ""
    }
)

print(result)
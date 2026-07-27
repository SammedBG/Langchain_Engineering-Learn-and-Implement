from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str


def chatbot(state: State):
    return {
        "message": state["message"] + " LangGraph!"
    }


builder = StateGraph(State)

builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")

builder.add_edge("chatbot", END)

graph = builder.compile()

result = graph.invoke(
    {
        "message": "Hello"
    }
)

print(result)
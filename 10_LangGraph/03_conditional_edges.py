from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    question: str


def router(state: State):

    if "company" in state["question"].lower():
        return "search"

    return "answer"


def search_documents(state: State):
    print("Searching company documents...")
    return {}


def answer(state: State):
    print("Generating answer...")
    return {}


builder = StateGraph(State)

builder.add_node("search", search_documents)
builder.add_node("answer", answer)

builder.add_conditional_edges(
    START,
    router,
)

builder.add_edge("search", END)
builder.add_edge("answer", END)

graph = builder.compile()

graph.invoke(
    {
        "question": "What is Python?"
    }
)
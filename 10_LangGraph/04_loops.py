from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END,
)


class State(TypedDict):
    count: int


def increment(state: State):

    print(
        f"Current Count: {state['count']}"
    )

    return {
        "count": state["count"] + 1
    }


def should_continue(state: State):

    if state["count"] < 5:
        return "increment"

    return END


builder = StateGraph(State)

builder.add_node(
    "increment",
    increment,
)

builder.add_edge(
    START,
    "increment",
)

builder.add_conditional_edges(
    "increment",
    should_continue,
)

graph = builder.compile()

result = graph.invoke(
    {
        "count": 0
    }
)

print(result)
from dotenv import load_dotenv

from langchain_core.messages import (
    HumanMessage,
    ToolMessage,
)

from langchain_core.tools import tool

from langchain_groq import ChatGroq

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

llm = llm.bind_tools([multiply])

messages = [
    HumanMessage(
        content="Multiply 15 and 8"
    )
]

response = llm.invoke(messages)

tool_call = response.tool_calls[0]

result = multiply.invoke(
    tool_call["args"]
)

tool_message = ToolMessage(
    content=str(result),
    tool_call_id=tool_call["id"],
)

messages.append(response)
messages.append(tool_message)

final_response = llm.invoke(messages)

print(final_response.content)
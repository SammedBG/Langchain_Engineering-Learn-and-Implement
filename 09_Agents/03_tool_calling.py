from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

llm_with_tools = llm.bind_tools(
    [multiply]
)

response = llm_with_tools.invoke(
    [
        HumanMessage(
            content="Multiply 15 and 8"
        )
    ]
)

print(response)
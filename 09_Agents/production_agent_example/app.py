from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent

from langgraph.checkpoint.memory import MemorySaver

from tools.calculator import add
from tools.text_tools import word_count
from tools.rag_tool import retriever_tool

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

memory = MemorySaver()

agent = create_react_agent(
    model=llm,
    tools=[
        add,
        word_count,
        retriever_tool,
    ],
    checkpointer=memory,
)

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

while True:

    question = input("You : ")

    if question.lower() == "exit":
        break

    print("AI : ", end="", flush=True)

    for token, metadata in agent.stream(
        {
            "messages": [
                (
                    "user",
                    question
                )
            ]
        },
        config=config,
        stream_mode="messages",
    ):
        if token.content:
            print(token.content, end="", flush=True)

    print()
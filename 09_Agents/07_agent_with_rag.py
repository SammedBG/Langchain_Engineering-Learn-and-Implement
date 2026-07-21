from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.tools import create_retriever_tool

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "multi_faiss",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    name="company_knowledge",
    description=(
        "Search the company knowledge base for "
        "internal documentation."
    ),
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

agent = create_react_agent(
    model=llm,
    tools=[retriever_tool],
)

response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "Explain LCEL."
            )
        ]
    }
)

print(response["messages"][-1].content)
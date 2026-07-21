from langchain_core.tools import create_retriever_tool

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore/faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)

retriever = db.as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    name="company_knowledge",
    description="Search company documentation."
)
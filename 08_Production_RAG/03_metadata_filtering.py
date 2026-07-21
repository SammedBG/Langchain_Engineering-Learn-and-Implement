"""
03_metadata_filtering.py

Filtering documents using metadata.
"""

from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [

    Document(
        page_content="LangChain is an AI framework.",

        metadata={
            "topic": "AI",
            "source": "langchain.pdf",
        },
    ),

    Document(
        page_content="React uses components.",

        metadata={
            "topic": "Frontend",
            "source": "react.pdf",
        },
    ),

    Document(
        page_content="Docker creates containers.",

        metadata={
            "topic": "DevOps",
            "source": "docker.pdf",
        },
    ),

]

db = FAISS.from_documents(
    documents,
    embedding,
)

retriever = db.as_retriever(
    search_kwargs={
        "k": 2,
        "filter": {
            "topic": "AI",
        },
    },
)

results = retriever.invoke(
    "Explain LangChain"
)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)

"""
Creating LangChain Document objects.
"""

from langchain_core.documents import Document

document = Document(
    page_content="LangChain makes building LLM applications easier.",
    metadata={
        "source": "notes",
        "topic": "langchain",
    },
)

print(document)
print(document.page_content)
print(document.metadata)
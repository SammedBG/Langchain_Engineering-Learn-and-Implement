
"""
Loading a PDF using PyPDFLoader.
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/langchain.pdf")

documents = loader.load()

print(f"Pages : {len(documents)}")

print(documents[0].page_content[:500])
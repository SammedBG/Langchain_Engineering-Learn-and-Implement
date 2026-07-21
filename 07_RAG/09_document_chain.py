
"""
create_stuff_documents_chain example.
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_template(
    """
Answer using only the context.

Context:
{context}

Question:
{input}
"""
)

chain = create_stuff_documents_chain(
    llm,
    prompt,
)

print(chain)
"""
02_runnable_passthrough.py

Passing input unchanged while adding new values.
"""

from langchain_core.runnables import RunnablePassthrough


chain = RunnablePassthrough()

response = chain.invoke(
    {
        "name": "Sammed",
        "role": "Developer",
    }
)

print(response)
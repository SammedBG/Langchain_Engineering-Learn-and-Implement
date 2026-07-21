"""
01_runnable_lambda.py

Creating custom logic using RunnableLambda.
"""

from langchain_core.runnables import RunnableLambda


def uppercase(text: str):
    return text.upper()


chain = RunnableLambda(uppercase)

response = chain.invoke("hello langchain")

print(response)
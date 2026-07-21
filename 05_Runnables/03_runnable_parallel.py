"""
03_runnable_parallel.py

Executing multiple runnables simultaneously.
"""

from langchain_core.runnables import RunnableLambda, RunnableParallel


uppercase = RunnableLambda(lambda x: x.upper())
length = RunnableLambda(len)
reverse = RunnableLambda(lambda x: x[::-1])

chain = RunnableParallel(
    uppercase=uppercase,
    length=length,
    reverse=reverse,
)

response = chain.invoke("LangChain")

print(response)
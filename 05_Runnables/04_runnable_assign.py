"""
04_runnable_assign.py

Adding computed fields to an existing dictionary.
"""

from langchain_core.runnables import RunnableLambda, RunnablePassthrough


chain = RunnablePassthrough.assign(
    uppercase=RunnableLambda(lambda x: x["name"].upper()),
    length=RunnableLambda(lambda x: len(x["name"])),
)

response = chain.invoke(
    {
        "name": "Sammed"
    }
)

print(response)
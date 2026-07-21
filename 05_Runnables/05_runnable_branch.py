"""
05_runnable_branch.py

Routing execution based on conditions.
"""

from langchain_core.runnables import RunnableBranch, RunnableLambda


chain = RunnableBranch(
    (
        lambda x: x >= 18,
        RunnableLambda(lambda _: "Adult"),
    ),
    RunnableLambda(lambda _: "Minor"),
)

print(chain.invoke(25))
print(chain.invoke(15))
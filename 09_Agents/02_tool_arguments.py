from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


print(add.name)
print(add.description)
print(add.args)

result = add.invoke(
    {
        "a": 8,
        "b": 12,
    }
)

print(result)
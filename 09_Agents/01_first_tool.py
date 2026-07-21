from langchain_core.tools import tool


@tool
def greet(name: str) -> str:
    """Greets a user by name."""
    return f"Hello {name}!"


print(greet.name)
print(greet.description)
print(greet.args)

result = greet.invoke(
    {
        "name": "Sammed"
    }
)

print(result)
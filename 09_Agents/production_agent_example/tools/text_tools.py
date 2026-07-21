from langchain_core.tools import tool


@tool
def word_count(text: str) -> int:
    """Count the number of words."""
    return len(text.split())
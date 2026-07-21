"""
02_in_memory_history.py

Using InMemoryChatMessageHistory.
"""

from langchain_core.chat_history import InMemoryChatMessageHistory

history = InMemoryChatMessageHistory()

history.add_user_message("Hello")

history.add_ai_message("Hi!")

history.add_user_message("How are you?")

for message in history.messages:
    print(message)
"""
04_multiple_sessions.py

Managing multiple chat sessions.
"""

from langchain_core.chat_history import InMemoryChatMessageHistory

store = {}


def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


user1 = get_history("user1")
user2 = get_history("user2")

user1.add_user_message("Hello")

user2.add_user_message("Hi")

print(user1.messages)

print(user2.messages)
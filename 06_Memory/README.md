# 06 - Memory

## Overview

Memory enables LangChain applications to retain conversation context across multiple interactions. Instead of treating each request independently, memory allows the model to reference previous messages, enabling natural multi-turn conversations.

---

## Files

| File | Description |
|------|-------------|
| `01_manual_chat_history.py` | Maintain conversation history using a Python list |
| `02_in_memory_history.py` | Store messages with `InMemoryChatMessageHistory` |
| `03_runnable_with_message_history.py` | Integrate memory into an LCEL chain |
| `04_multiple_sessions.py` | Manage separate conversation histories using session IDs |
| `05_chatbot.py` | Build a complete conversational chatbot with memory |

---

## Learning Objectives

After completing this module, you'll understand:

- Manual chat history management
- `InMemoryChatMessageHistory`
- `RunnableWithMessageHistory`
- Session-based memory
- Multi-user conversations
- Building stateful chatbots

---

## Memory Flow

```text
User
  │
  ▼
Prompt
  │
  ▼
Previous Messages
  │
  ▼
LLM
  │
  ▼
Response
  │
  ▼
Store in Memory
```

---

## Memory Components

### Manual History

Maintain messages yourself using a Python list of `SystemMessage`, `HumanMessage`, and `AIMessage`.

### InMemoryChatMessageHistory

A built-in message store for maintaining chat history during runtime.

### RunnableWithMessageHistory

Automatically injects previous messages into an LCEL chain and updates history after each interaction.

### Session IDs

Each session ID maps to its own independent conversation history, enabling multiple users or chats simultaneously.

---

## Key Takeaways

- Memory provides conversational context.
- `InMemoryChatMessageHistory` is suitable for runtime memory.
- `RunnableWithMessageHistory` integrates memory seamlessly with LCEL.
- Session IDs isolate conversations.
- Production systems typically replace in-memory storage with databases such as Redis, MongoDB, or PostgreSQL.

---

## Next Module

**07_RAG**

Topics include:

- Documents
- Document Loaders
- Text Splitters
- Embeddings
- Vector Stores (FAISS)
- Retrievers
- Retrieval Chains
- Conversational RAG
- History-Aware Retrieval
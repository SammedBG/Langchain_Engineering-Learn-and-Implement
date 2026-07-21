# 08 - Production RAG

## Overview

A basic RAG application works well for small demos, but production systems require additional techniques to improve retrieval quality, scalability, transparency, and user experience.

In this module, you'll learn how to build enterprise-ready Retrieval-Augmented Generation (RAG) systems using advanced retrieval strategies, metadata filtering, persistent vector databases, multi-document search, source attribution, and streaming responses.

---

## Prerequisites

Before starting this module, you should understand:

- Documents
- Document Loaders
- Text Splitters
- Embeddings
- FAISS
- Retrievers
- Manual RAG
- Retrieval Chains
- Conversational RAG

---

## Files

| File | Description |
|------|-------------|
| `01_mmr_retrieval.py` | Compare Similarity Search and Maximum Marginal Relevance (MMR) |
| `02_similarity_score_threshold.py` | Retrieve only documents above a similarity threshold |
| `03_metadata_filtering.py` | Filter documents using metadata |
| `04_save_faiss.py` | Save a FAISS vector store to disk |
| `05_load_faiss.py` | Load an existing FAISS vector store |
| `06_multi_document_rag.py` | Build a RAG system over multiple PDFs |
| `07_source_attribution.py` | Display document citations with answers |
| `08_streaming_rag.py` | Stream responses from a retrieval chain |

---

# Production RAG Pipeline

```text
                     Documents
                         │
                         ▼
                 Document Loader
                         │
                         ▼
                  Text Splitter
                         │
                         ▼
                   Embeddings
                         │
                         ▼
                  Vector Store
                         │
                  Save FAISS Index
                         │
──────────────────────────────────────────────
                  Application Starts
                         │
                         ▼
                 Load FAISS Index
                         │
                         ▼
                  User Question
                         │
                         ▼
              Metadata Filtering
                         │
                         ▼
                 MMR / Similarity
                         │
                         ▼
                   Retrieved Chunks
                         │
                         ▼
                      Prompt
                         │
                         ▼
                        LLM
                         │
                         ▼
             Answer + Source Attribution
                         │
                         ▼
                Streaming Response
```

---

# Learning Objectives

After completing this module, you'll understand:

- Maximum Marginal Relevance (MMR)
- Similarity Score Threshold
- Metadata Filtering
- Persistent FAISS Storage
- Multi-Document Retrieval
- Source Attribution
- Streaming Responses
- Production Architecture
- Best Practices

---

# Lesson 1 — MMR Retrieval

Maximum Marginal Relevance retrieves documents that are:

- Relevant to the query
- Different from each other

Instead of returning similar chunks repeatedly, MMR increases context diversity.

```python
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 20,
        "lambda_mult": 0.5,
    },
)
```

---

# Lesson 2 — Similarity Score Threshold

Instead of always returning the top **k** documents, retrieve only documents whose similarity score exceeds a chosen threshold.

```python
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "score_threshold": 0.80,
        "k": 5,
    },
)
```

Benefits:

- Reduces irrelevant context
- Reduces hallucinations
- Improves answer quality

---

# Lesson 3 — Metadata Filtering

Metadata narrows the search space before similarity search.

Example metadata:

```python
metadata = {
    "source": "langchain.pdf",
    "topic": "AI",
    "page": 12,
}
```

Filter example:

```python
retriever = db.as_retriever(
    search_kwargs={
        "filter": {
            "topic": "AI"
        }
    }
)
```

Benefits:

- Faster retrieval
- Better precision
- Enterprise access control
- Document organization

---

# Lesson 4 — Saving FAISS

Create the vector database once.

```python
db.save_local("faiss_index")
```

Generated files:

```text
faiss_index/

index.faiss

index.pkl
```

---

# Lesson 5 — Loading FAISS

Reuse the saved index.

```python
db = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)
```

Benefits:

- Faster startup
- No embedding regeneration
- Lower compute cost

---

# Lesson 6 — Multi-Document RAG

Instead of indexing one document:

```text
LangChain.pdf
```

Index multiple documents:

```text
LangChain.pdf

Python.pdf

Docker.pdf

React.pdf

AWS.pdf
```

Store them in one vector database.

Each chunk retains metadata indicating its source document.

---

# Lesson 7 — Source Attribution

Show users where an answer came from.

Example:

```text
Answer

LCEL stands for LangChain Expression Language.

Sources

langchain.pdf (Page 12)

langchain.pdf (Page 13)
```

Benefits:

- Transparency
- Trust
- Easy verification
- Better user experience

---

# Lesson 8 — Streaming Responses

Instead of waiting for the complete response:

```python
response = chain.invoke(question)
```

Stream tokens as they are generated:

```python
for chunk in chain.stream(question):
    print(chunk)
```

Benefits:

- Better responsiveness
- ChatGPT-like experience
- Improved perceived performance

---

# Production Architecture

```text
                 PDFs
                   │
                   ▼
          Ingestion Pipeline
                   │
                   ▼
          Vector Database
                   │
────────────────────────────────────
              User Query
                   │
                   ▼
             API Server
                   │
                   ▼
              Retriever
                   │
                   ▼
                 LLM
                   │
                   ▼
      Answer + Citations + Streaming
```

---

# Best Practices

- Build embeddings only during ingestion
- Save the FAISS index
- Load the existing index at application startup
- Store useful metadata with every chunk
- Prefer MMR for large document collections
- Use metadata filtering whenever possible
- Display source citations
- Stream responses to improve user experience
- Separate ingestion and serving pipelines
- Keep prompts, retrieval, and API logic in separate modules

---

# Production Folder Structure

```text
rag_project/

│

├── data/

├── ingestion/

│     loader.py

│     splitter.py

│     embeddings.py

│     build_index.py

│

├── vectorstore/

│     faiss_index/

│

├── retrieval/

│     retriever.py

│     filters.py

│     citations.py

│

├── llm/

│     model.py

│     prompts.py

│

├── chains/

│     rag_chain.py

│

├── api/

│     app.py

│

└── config.py
```

---

# Skills Acquired

After completing this module, you can build production-ready RAG systems featuring:

- Intelligent retrieval
- Diverse document selection
- Persistent vector storage
- Metadata-aware search
- Multi-document retrieval
- Source attribution
- Streaming responses
- Enterprise-ready architecture

---

# Module Summary

In this module, you transformed a basic RAG application into a production-ready system by learning how to optimize retrieval, manage vector databases efficiently, search across multiple documents, provide trustworthy citations, and deliver responses in real time. These techniques form the foundation of scalable enterprise AI assistants.

---

# Next Module

## 09_Agents

Topics:

- What are AI Agents?
- LLM vs Agent
- Tools
- Tool Calling
- `@tool` Decorator
- `create_react_agent`
- Agent Execution Loop
- Multi-Tool Agents
- Memory + Agents
- Production Agent Architecture
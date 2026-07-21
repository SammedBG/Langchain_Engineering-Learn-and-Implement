
# 07 - Retrieval-Augmented Generation (RAG)

## Overview

Retrieval-Augmented Generation (RAG) enables Large Language Models to answer questions using external knowledge instead of relying only on their training data.

The workflow consists of loading documents, splitting them into smaller chunks, generating embeddings, storing those embeddings in a vector database, retrieving the most relevant chunks, and providing them to the LLM as context.

---

## Files

| File | Description |
|------|-------------|
| `01_document.py` | Create `Document` objects |
| `02_document_loader.py` | Load PDF documents |
| `03_text_splitter.py` | Split documents into chunks |
| `04_embeddings.py` | Generate embeddings |
| `05_vector_store.py` | Build a FAISS vector store |
| `06_similarity_search.py` | Search similar documents |
| `07_retriever.py` | Use a retriever |
| `08_manual_rag.py` | Build a manual LCEL RAG pipeline |
| `09_document_chain.py` | Use `create_stuff_documents_chain` |
| `10_retrieval_chain.py` | Build a retrieval chain |
| `11_history_aware_retriever.py` | Context-aware retrieval using chat history |
| `12_conversational_rag.py` | End-to-end conversational RAG |

---

## RAG Pipeline

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
Vector Store (FAISS)
    │
    ▼
Retriever
    │
    ▼
Prompt
    │
    ▼
LLM
    │
    ▼
Answer
```

---

## Learning Objectives

After completing this module, you'll understand:

- LangChain `Document`
- Document Loaders
- Recursive Text Splitting
- Embedding Models
- FAISS Vector Stores
- Similarity Search
- Retrievers
- Manual LCEL RAG
- Document Chains
- Retrieval Chains
- History-Aware Retrieval
- Conversational RAG

---

## Next Module

**08_Production_RAG**

Topics include:

- MMR Retrieval
- Similarity Score Threshold
- Metadata Filtering
- Save & Load FAISS
- Multi-document RAG
- Source Attribution
- Streaming Responses
- Production Best Practices
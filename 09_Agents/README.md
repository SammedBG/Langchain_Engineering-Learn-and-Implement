# Module 09 – Agents

This module introduces AI Agents in LangChain and LangGraph. Unlike traditional LLM applications that simply generate text, Agents can reason about a task, decide when external tools are required, invoke those tools, observe the results, and continue reasoning until they produce a final answer.

By the end of this module, you'll be able to build production-ready AI assistants with custom tools, Retrieval-Augmented Generation (RAG), memory, and streaming.

---

## Topics Covered

### 01. Introduction to AI Agents
- What is an AI Agent?
- LLM vs Agent
- ReAct (Reason + Act)
- Agent Architecture
- Real-world Applications

---

### 02. Tools
- What are Tools?
- Built-in vs Custom Tools
- Tool Metadata
- Tool Descriptions
- Tool Selection

---

### 03. Creating Custom Tools
- `@tool`
- Tool Inputs
- Tool Outputs
- Docstrings
- Tool Invocation

---

### 04. Structured Tools
- StructuredTool
- Pydantic Schemas
- Multiple Parameters
- Validation
- Tool Metadata

---

### 05. Tool Calling
- Function Calling
- `bind_tools()`
- `response.tool_calls`
- Tool Requests
- Tool Arguments

---

### 06. Manual Tool Execution
- Reading Tool Calls
- Executing Tools
- ToolMessage
- Agent Conversation Loop

---

### 07. create_react_agent()
- Automatic Tool Execution
- ReAct Loop
- Agent Invocation
- Response Structure

---

### 08. Multi-Step Reasoning
- Multiple Tool Calls
- Chained Reasoning
- Intermediate Observations
- Final Responses

---

### 09. Multi-Tool Agent
- Multiple Custom Tools
- Automatic Tool Selection
- Dynamic Execution

---

### 10. Agent + RAG
- Retriever as Tool
- `create_retriever_tool()`
- Dynamic Retrieval
- Enterprise RAG Architecture

---

### 11. Agent Memory
- MemorySaver
- Checkpointers
- Thread IDs
- Persistent Conversations

---

### 12. Streaming
- `agent.stream()`
- `updates`
- `messages`
- `values`
- Live Token Streaming

---

### 13. Production Agent
- Modular Project Structure
- Multiple Tools
- RAG
- Memory
- Streaming
- Production Best Practices

---

## Folder Structure

```
09_Agents/

01_first_tool.py
02_structured_tool.py
03_tool_calling.py
04_manual_tool_execution.py
05_first_agent.py
06_multi_tool_agent.py
07_agent_with_rag.py
08_agent_memory.py
09_streaming_agent.py
10_production_agent.py

README.md
```

---

## Learning Outcomes

After completing this module, you should be able to:

- Build AI Agents using LangGraph
- Create custom tools
- Implement tool calling
- Build multi-tool workflows
- Convert retrievers into tools
- Add conversational memory
- Stream responses
- Design production-ready AI assistants

---

## Technologies Used

- Python
- LangChain
- LangGraph
- LangSmith (optional)
- Groq
- FAISS
- Hugging Face Embeddings
- dotenv

---

## Next Module

➡ Module 10 – LangGraph
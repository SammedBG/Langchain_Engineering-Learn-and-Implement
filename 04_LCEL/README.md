# 04 - LangChain Expression Language (LCEL)

## Overview

LangChain Expression Language (LCEL) is the modern way to build AI applications in LangChain.

Instead of creating long classes or manually calling each component, LCEL allows you to connect prompts, models, retrievers, parsers, and custom functions using the pipe (`|`) operator.

LCEL makes applications:

- Simple
- Readable
- Reusable
- Modular
- Production-ready

---

## Files

| File | Description |
|------|-------------|
| `01_pipe_operator.py` | Introduction to the LCEL Pipe (`|`) Operator |
| `02_chain.py` | Creating a simple Prompt → LLM → Parser chain |
| `03_runnable_sequence.py` | Building chains using `RunnableSequence` |
| `04_chain_invoke_batch_stream.py` | Using `invoke()`, `batch()`, and `stream()` |
| `05_chain_steps.py` | Inspecting and understanding chain components |

---

## Learning Objectives

After completing this module, you'll understand:

- What LCEL is
- Why LCEL was introduced
- Pipe Operator (`|`)
- Runnable Chains
- RunnableSequence
- Chain execution
- invoke()
- batch()
- stream()
- Chain inspection

---

## LCEL Flow

```
Input
  │
  ▼
Prompt
  │
  ▼
LLM
  │
  ▼
Output Parser
  │
  ▼
Final Output
```

---

## The Pipe Operator

The Pipe Operator connects one Runnable to another.

```
Prompt
    |
    ▼
LLM
    |
    ▼
Output Parser
```

Instead of writing multiple function calls, LCEL creates a clean execution pipeline.

Example:

```python
chain = prompt | llm | StrOutputParser()
```

---

## RunnableSequence

The Pipe Operator internally creates a `RunnableSequence`.

These two are equivalent:

```python
chain = prompt | llm | parser
```

```python
chain = RunnableSequence(
    first=prompt,
    middle=[llm],
    last=parser
)
```

---

## Chain Execution Methods

### invoke()

Runs the chain once.

```python
response = chain.invoke(data)
```

---

### batch()

Runs the same chain for multiple inputs.

```python
responses = chain.batch(inputs)
```

---

### stream()

Streams tokens as they are generated.

```python
for chunk in chain.stream(data):
    print(chunk)
```

---

## Why LCEL?

LCEL offers several advantages:

- Cleaner code
- Easier debugging
- Better readability
- Component reusability
- Native streaming support
- Parallel execution support
- Easy integration with RAG
- Easy integration with Agents
- Easy integration with LangGraph

---

## Module Summary

In this module, you learned how to:

- Connect LangChain components using the Pipe Operator
- Build execution pipelines
- Create RunnableSequences
- Execute chains using invoke(), batch(), and stream()
- Inspect chain structure and execution flow

These concepts form the foundation for advanced LangChain development.

---

## Next Module

**05_Runnables**

You'll learn:

- RunnableLambda
- RunnablePassthrough
- RunnableParallel
- RunnableAssign
- RunnableBranch
- Custom Runnable Pipelines
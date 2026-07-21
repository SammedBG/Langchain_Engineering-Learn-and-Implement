# 05 - Runnables

## Overview

Runnables are the core execution units in LangChain.

Everything in LCEL is built around Runnables. Prompts, chat models,
retrievers, output parsers, and custom functions all implement the Runnable interface.

---

## Files

| File | Description |
|------|-------------|
| 01_runnable_lambda.py | Create custom runnable functions |
| 02_runnable_passthrough.py | Pass data through unchanged |
| 03_runnable_parallel.py | Execute multiple runnables simultaneously |
| 04_runnable_assign.py | Add computed fields to dictionaries |
| 05_runnable_branch.py | Conditional execution |

---

## Runnable Types

### RunnableLambda

Wraps any Python function.

```python
RunnableLambda(func)
```

---

### RunnablePassthrough

Returns the input unchanged.

Useful when enriching data.

---

### RunnableParallel

Runs multiple runnables simultaneously.

```
          Input
        /   |   \
      A     B     C
       \    |    /
        Combined Output
```

---

### RunnableAssign

Adds new computed keys.

Example

Input

```python
{"name":"Sammed"}
```

↓

Output

```python
{
    "name":"Sammed",
    "uppercase":"SAMMED",
    "length":6
}
```

---

### RunnableBranch

Runs different pipelines depending on conditions.

```
if condition:
    branch A
else:
    branch B
```

---

## Why Runnables?

They make applications

- Modular
- Reusable
- Parallelizable
- Production Ready

Every modern LangChain application relies on Runnables.

---

## Next Module

**06_Memory**

Topics:

- Chat Message History
- RunnableWithMessageHistory
- Session Management
- Conversation Memory
- Multi-user Chat
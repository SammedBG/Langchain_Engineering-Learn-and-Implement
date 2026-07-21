## `03_Output_Parsers/README.md`

````markdown
# 03 - Output Parsers

## Overview

Output Parsers transform the raw response returned by an LLM into the format required by your application.

Instead of manually extracting data from an `AIMessage`, LangChain provides parsers to convert the response into strings, JSON, lists, Pydantic models, and more.

---

## Files

| File | Description |
|------|-------------|
| `01_str_output_parser.py` | Converts an `AIMessage` into a plain Python string. |
| `02_json_output_parser.py` | Converts the LLM response into a Python dictionary (JSON). |

---

## Learning Objectives

After completing this module, you will understand:

- What Output Parsers are
- Why Output Parsers are needed
- How `StrOutputParser` works
- How `JsonOutputParser` works
- How to generate structured output from an LLM

---

## Module Flow

```

Prompt
│
▼
LLM
│
▼
AIMessage
│
▼
Output Parser
│
▼
Python Object

```

---

## Output Parser Types

- StrOutputParser
- JsonOutputParser
- PydanticOutputParser
- XML Output Parser
- CSV Output Parser
- Custom Output Parser

---

## When to Use

### StrOutputParser

Use when the application only needs plain text.

Example:

- Chatbots
- Question Answering
- Summarization

---

### JsonOutputParser

Use when structured data is required.

Example:

- APIs
- Dashboards
- Data Extraction
- Automation
- Agents

---

## Example

Without Parser

```

AIMessage
↓

response.content

```

With StrOutputParser

```

AIMessage
↓

StrOutputParser

↓

str

```

With JsonOutputParser

```

AIMessage
↓

JsonOutputParser

↓

dict

```

---

## Next Module

**04_LCEL**

You'll learn:

- Pipe Operator (`|`)
- LCEL Chains
- RunnableSequence
- Chain Composition
- Modern LangChain Pipelines

```
````

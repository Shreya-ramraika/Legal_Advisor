# ⚖️ LegalMind AI — Multi-Agent Legal Intelligence System

> 🚀 Capstone Project | Agentic AI | 2026
> 🧠 Built with LangGraph, RAG, and Multi-Agent Reasoning

---

## 🎯 Project Overview

LegalMind AI is an **agentic multi-agent legal assistant** designed to provide **accurate, grounded, and safe legal guidance** for Indian law.

It combines:

* 🔎 **Retrieval-Augmented Generation (RAG)**
* 🤖 **Tool-augmented reasoning**
* 🧠 **Self-reflection & evaluation loop**
* 💬 **Conversation memory (multi-turn)**

👉 The system ensures **high reliability, safety, and domain control**.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Groq API key

```bash
# Windows
set GROQ_API_KEY=your_key_here

# Linux/Mac
export GROQ_API_KEY=your_key_here
```

Get API key: https://console.groq.com

---

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🏗️ System Architecture (LangGraph)

```
User Query
   ↓
[memory_node]        → conversation context
   ↓
[router_node]        → route: retrieve / tool / out_of_scope
   ↓
 ┌───────────────┬───────────────┬────────────────┐
 │ retrieve_node │ tool_node     │ out_of_scope   │
 │ (RAG)         │ (custom tools)│ (safe decline) │
 └───────────────┴───────────────┴────────────────┘
   ↓
[generate_answer]    → LLM reasoning
   ↓
[eval_node]          → faithfulness check + retry loop
   ↓
[save_node]          → memory persistence (thread_id)
   ↓
Final Response
```

---

## 🧠 Key Capabilities

### ✅ 1. LangGraph Multi-Agent System

* 8-node structured agent workflow
* Conditional routing
* Retry-based evaluation loop

---

### ✅ 2. RAG Knowledge Base

* 15 curated legal documents
* ChromaDB vector store
* Grounded responses (no hallucination)

---

### ✅ 3. Conversation Memory

* Thread-based memory (`thread_id`)
* Multi-turn context awareness
* Sliding window mechanism

---

### ✅ 4. Self-Reflection (Evaluation Node)

* Faithfulness scoring (0–1)
* Automatic retry if score < 0.75
* Prevents hallucinated answers

---

### ✅ 5. Tool Usage (Beyond RAG)

* ⚖️ IPC Section Lookup
* 📅 Legal Deadline Calculator
* ⚠️ Risk Assessment (0–10)
* 🧠 Legal Advice Mode (structured guidance)

---

### ✅ 6. Deployment

* Streamlit interactive UI
* Real-time responses
* Metrics visualization

---

## 📚 Knowledge Base (15 Docs)

Includes:

* IPC Sections (302, 420, 498A)
* FIR & Legal Procedures
* Consumer Protection Act
* Domestic Violence Act
* Labour Laws
* Property & Tenant Rights
* POCSO Act

---

## 🛠️ Tech Stack

| Layer      | Tech                        |
| ---------- | --------------------------- |
| LLM        | Groq (LLaMA 3 Instant)      |
| Framework  | LangGraph                   |
| Retrieval  | ChromaDB                    |
| Embeddings | SentenceTransformers        |
| UI         | Streamlit                   |
| Evaluation | Custom Faithfulness Scoring |

---

## 🧪 Red-Team Testing (Safety & Robustness)

| Test Type          | Example              | Result       |
| ------------------ | -------------------- | ------------ |
| Out-of-Scope       | “Best restaurant?”   | ✅ Declined   |
| False Premise      | Wrong IPC claim      | ✅ Corrected  |
| Prompt Injection   | Reveal system prompt | ✅ Blocked    |
| Hallucination      | Fake citation        | ✅ Avoided    |
| Emotional Distress | Abuse case           | ✅ Empathetic |

---

## 📊 Evaluation Metrics

* **Faithfulness Score** → ensures grounded answers
* **Risk Score (0–10)** → identifies severity
* **Retry Mechanism** → improves answer reliability

---

## ✨ Advanced Features

* 🧭 Domain detection (legal-only system)
* 🔒 Safe refusal for out-of-scope queries
* ⚡ Fast inference (Groq instant model)
* 📚 Source transparency (retrieved docs shown)
* 💬 Chat memory across turns

---

## 📁 Project Structure

```
legalMind/
├── agent.py
├── app.py
├── config.py
├── requirements.txt
│
├── nodes/
├── tools/
├── utils/
│
└── knowledge_base/
    ├── doc_001.txt
    ├── ...
```

---

## ⚠️ Disclaimer

This system provides **informational legal guidance only**.
It is **not a substitute for professional legal advice**.

For help:
📞 NALSA Legal Aid: **15100**

---

## 🏆 Conclusion

LegalMind AI demonstrates how **Agentic AI systems** can:

* Combine reasoning + retrieval + tools
* Maintain safety and reliability
* Deliver domain-specific intelligence

👉 Built as a **production-style multi-agent system**, not just a chatbot.

---

# 🧠 RAG-Based Policy Chatbot

A Retrieval-Augmented Generation (RAG) chatbot designed to answer company policy questions accurately while strictly avoiding hallucinations.  
The system prioritizes **correctness, refusal, and explainability** over speculative answers.

Link : https://rag-mini-project.streamlit.app/

---

## 📌 Overview

This project implements a **policy question-answering assistant** using a Retrieval-Augmented Generation (RAG) architecture.  
User queries are answered **only** using retrieved policy document context and a strict prompting strategy.

The chatbot uses the **Groq API** with the following model:

MODEL = "llama-3.1-8b-instant"


---

## 🏗️ System Architecture

User Question
-->
Query Embedding
-->
Vector Similarity Search (Top-K = 3)
-->
Relevant Policy Chunks
-->
Prompt Injection
-->
LLM Answer


---

## 📂 Data Assumptions

The assignment stated that policy documents would be provided; however, no documents were included in the materials I received.

To proceed within the deadline, I created **representative policy documents** covering:
- Refund Policy
- Cancellation Policy
- Shipping Policy

These documents were intentionally kept realistic but simple to focus on:
- Retrieval quality
- Prompt engineering
- Hallucination avoidance

**Note:**  
The system is fully data-agnostic. Real company policy documents can be ingested without any code changes.

---

## ✂️ Chunking Strategy

- **Chunk Size:** 500 tokens  
- **Chunk Overlap:** 90 tokens  

### Rationale

Policy documents are clause-dense and context-sensitive.  
A 500-token chunk preserves semantic meaning without diluting context.  
Overlap prevents information loss when clauses span chunk boundaries.

---

## 🔍 Retrieval Strategy

- **Vector Store:** ChromaDB  
- **Embedding Model:** all-MiniLM-L6-v2  
- **Top-K Retrieval:** 3  

Limiting retrieval to the top 3 chunks reduces noise and lowers hallucination risk by keeping the context focused.

---

## 🧠 Prompt Engineering

### Prompt
- Simple instruction to answer using provided context
- Explicit rules forbidding prior knowledge
- Clear refusal instructions
- Structured output format with evidence

This iteration significantly improved answer grounding and refusal behavior.

---

## 🚫 Hallucination Control

The system is explicitly designed to:
- Answer **only** from retrieved context
- Refuse confidently when information is missing
- Avoid inference, assumptions, or generalization

Example refusal:
> “The provided documents do not contain this information.”

This behavior is intentional and preferred over speculative answers.

---

## 🧪 Evaluation

The evaluation set includes three question categories:

| Question Type | Expected Behavior | Result |
|--------------|------------------|--------|
| Fully answerable | Correct answer with citation | ✅ |
| Partially answerable | Partial answer + clarification | ⚠️ |
| Unanswerable | Explicit refusal | ✅ |

The system consistently prioritizes **correctness over completeness**.

---

## ⚖️ Trade-Offs & Future Improvements

With additional time, the following improvements could be explored:
- Chunk reranking for improved precision
- Sentence-level source attribution
- Confidence calibration using retrieval scores
- Logging and monitoring for production deployment

---

## 🏁 Conclusion

This project emphasizes **safe and production-oriented RAG design**.  
Rather than maximizing answer rate, the chatbot focuses on **trustworthy, explainable, and auditable responses**, which are essential for real-world policy assistants.

---

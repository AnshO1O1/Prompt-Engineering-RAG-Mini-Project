RAG Policy Assistant
Objective
Build a Retrieval-Augmented Generation (RAG) system that answers questions over company policy documents while avoiding hallucinations and clearly handling missing information.

Architecture Overview
The system follows a basic Retrieval-Augmented Generation (RAG) flow:

Documents → Chunking → Embeddings → Vector Store (ChromaDB) → Semantic Retrieval (Top-k) → Prompt + Context → LLM → Answer

The system follows a standard RAG pipeline where generation is strictly grounded in retrieved documents.

Data Preparation
Policy Documents
Representative company policy documents were used:

Refund Policy
Cancellation Policy
Shipping Policy
The documents are stored as plain text and are sufficient to demonstrate answerable, partially answerable, and unanswerable queries.

Chunking Strategy
Documents are split using RecursiveCharacterTextSplitter with:

Chunk size: 400 characters
Chunk overlap: 80 characters
This preserves clause-level meaning in policy text while preventing information loss at chunk boundaries.

RAG Pipeline
Embeddings generated using sentence-transformers/all-MiniLM-L6-v2
Chunks stored in a Chroma vector database
Semantic similarity search with top-k = 3
Retrieved context passed to the LLM for answer generation
Restricting retrieval to top-k reduces noise and hallucinations.

Prompt Engineering
A strict prompt is used to enforce:

Answers based only on retrieved context
Explicit refusal when information is missing
Structured output format:
Answer
Evidence
Confidence
This design improves grounding and answer reliability.

Evaluation
An evaluation set includes:

Fully answerable questions
Partially answerable questions
Unanswerable questions
Evaluation focuses on accuracy, hallucination avoidance, and clarity. Results are documented separately.

Edge Case Handling
If no relevant documents are retrieved, the system responds that the information is not available.
If a question is outside the knowledge base, the system explicitly refuses to answer.
LLM Backend
The system uses a hosted LLM via the Groq API for fast, low-latency generation.
The LLM layer is modular and can be replaced without changes to the RAG pipeline.

Trade-offs and Improvements
With more time, the system could be extended with:

Retrieval reranking
Automated evaluation metrics
Source attribution per chunk

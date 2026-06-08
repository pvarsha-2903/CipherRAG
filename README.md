# CipherRAG
### A Cryptographically Secure Retrieval-Augmented Generation Framework

---

## What is CipherRAG?

Standard RAG systems store document chunks as plain, readable text inside 
vector databases. A single database breach exposes everything. Worse, even 
vector embeddings can be reverse-engineered to recover original content.

CipherRAG solves this by encrypting every document chunk with AES-256-GCM 
before storage, decrypting only at query time, and protecting all keys 
through envelope encryption — the same pattern used by AWS and Google Cloud.

---

## The Problem This Solves

- Document chunks stored as plaintext = one breach exposes everything
- Vector embeddings can be inverted to recover original text (Morris et al., 2023)
- No existing open-source RAG framework addresses encryption at the core

---

## Architecture
Document → Chunker → Encryption (AES-256-GCM) → Vector Store
↓
Key Manager (DEK + KEK)
↓
Query → Embed → Retrieve → Decrypt → LLM → Answer

---

## Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3.12 |
| Encryption | AES-256-GCM via `cryptography` library |
| Embeddings | sentence-transformers (coming soon) |
| Vector Database | ChromaDB (coming soon) |
| LLM | Claude API (coming soon) |

---

## Project Status

| Module | Description | Status |
|--------|-------------|--------|
| Module 1 | RAG — Concepts & First Principles | ✅ Complete |
| Module 2 | Cryptography — Concepts & First Principles | ✅ Complete |
| Module 3 | CipherRAG Architecture Design | ✅ Complete |
| Module 4 | Document Loader + Chunker | ✅ Complete |
| Module 5 | AES-256-GCM Encryption + Key Manager | ✅ Complete |
| Module 6 | Embeddings | 🔄 In Progress |
| Module 7 | Vector Store | ⏳ Upcoming |
| Module 8 | Retrieval | ⏳ Upcoming |
| Module 9 | LLM Integration | ⏳ Upcoming |

> Modules 1–3 are concept and architecture modules.
> Full notes and documentation available in the `/docs` folder.

---

---

---

## Research Foundation

This project is built on the following academic work:

- Lewis et al. (2020) — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- NIST FIPS 197 (2023) — Advanced Encryption Standard
- Morris et al. (2023) — Text Embeddings Reveal (Almost) As Much As Text
- Zeng et al. (2024) — Privacy Issues in RAG

---

## Author

**P. Varsha**
3rd Year Undergraduate — Independent Research Project
# CipherRAG — Threat Model

## Overview

CipherRAG is designed to defend against three distinct threat surfaces.

## Threat 1 — Database Breach
An attacker gains direct access to the vector database and attempts 
to read stored document chunks.

**Defended by:** Encryption Module — all chunks are encrypted with 
AES-256-GCM before storage. Stolen data is computationally unreadable 
without the corresponding DEK and KEK.

## Threat 2 — Embedding Inversion
An attacker exploits the mathematical structure of vector embeddings 
to reconstruct original text. Morris et al. (2023) demonstrated this 
is possible with up to 92% accuracy on standard RAG systems.

**Defended by:** Embedding Module — embeddings are generated from 
already-encrypted chunks, not plaintext. Any inversion attempt 
recovers ciphertext, not readable content.

## Threat 3 — Key Theft
An attacker targets the master Key Encryption Key (KEK) directly, 
bypassing document encryption entirely.

**Defended by:** Key Manager — envelope encryption separates DEKs 
from the KEK. The KEK is never stored in the database. In this 
prototype the KEK is stored locally. Production deployment would 
require a Hardware Security Module (HSM) or managed key service 
such as AWS KMS — this remains an open direction for future work.

## Scope
This threat model covers the prototype implementation. Network-level 
attacks, side-channel attacks, and physical device compromise are 
outside the scope of this research.
from ingestion.document_loader import load_document
from ingestion.chunker import chunk_text
from crypto.encryption import generate_key, encrypt_chunk
from embeddings.embedder import embed_text

text = load_document("data/documents/sample.txt")
chunks = chunk_text(text, chunk_size=10, overlap=2)

key = generate_key()

first_chunk = chunks[0]
print(f"Original chunk: {first_chunk}")

ciphertext, iv, tag = encrypt_chunk(first_chunk, key)
ciphertext_str = ciphertext.hex()

embedding = embed_text(ciphertext_str)
print(f"\nEmbedding dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
from ingestion.document_loader import load_document
from ingestion.chunker import chunk_text

text = load_document("data/documents/sample.txt")
chunks = chunk_text(text, chunk_size=10, overlap=2)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i} ---")
    print(chunk)
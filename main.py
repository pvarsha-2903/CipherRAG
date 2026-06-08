from ingestion.document_loader import load_document
from ingestion.chunker import chunk_text
from crypto.encryption import generate_key, encrypt_chunk, decrypt_chunk
from crypto.key_manager import generate_kek, encrypt_dek, decrypt_dek

text = load_document("data/documents/sample.txt")
chunks = chunk_text(text, chunk_size=10, overlap=2)

kek = generate_kek()
print("KEK generated")

dek = generate_key()
print(f"DEK generated: {dek.hex()}")

encrypted_dek, dek_iv, dek_tag = encrypt_dek(dek, kek)
print(f"DEK encrypted: {encrypted_dek}")

recovered_dek = decrypt_dek(encrypted_dek, kek, dek_iv, dek_tag)
print(f"DEK recovered: {recovered_dek.hex()}")

print(f"DEK match: {dek == recovered_dek}")

first_chunk = chunks[0]
ciphertext, iv, tag = encrypt_chunk(first_chunk, dek)
decrypted = decrypt_chunk(ciphertext, recovered_dek, iv, tag)
print(f"\nOriginal:  {first_chunk}")
print(f"Decrypted: {decrypted}")
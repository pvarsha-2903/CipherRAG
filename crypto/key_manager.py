import os
from crypto.encryption import encrypt_chunk, decrypt_chunk

def generate_kek():
    return os.urandom(32)

def encrypt_dek(dek, kek):
    encrypted_dek, iv, tag = encrypt_chunk(dek.hex(), kek)
    return encrypted_dek, iv, tag

def decrypt_dek(encrypted_dek, kek, iv, tag):
    dek_hex = decrypt_chunk(encrypted_dek, kek, iv, tag)
    return bytes.fromhex(dek_hex)
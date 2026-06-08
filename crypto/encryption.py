import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key():
    return os.urandom(32)

def encrypt_chunk(plaintext, key):
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    plaintext_bytes = plaintext.encode('utf-8')
    ciphertext_with_tag = aesgcm.encrypt(iv, plaintext_bytes, None)
    ciphertext = ciphertext_with_tag[:-16]
    tag = ciphertext_with_tag[-16:]
    return ciphertext, iv, tag

def decrypt_chunk(ciphertext, key, iv, tag):
    aesgcm = AESGCM(key)
    ciphertext_with_tag = ciphertext + tag
    plaintext_bytes = aesgcm.decrypt(iv, ciphertext_with_tag, None)
    return plaintext_bytes.decode('utf-8')
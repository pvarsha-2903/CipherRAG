from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    embedding = model.encode(text)
    return embedding.tolist()

def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        embedding = embed_text(chunk)
        embeddings.append(embedding)
    return embeddings
import os

def load_document(file_path):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    return text
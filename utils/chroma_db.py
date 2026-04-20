import chromadb

def init_chromadb(embedder):
    client = chromadb.Client()
    return client.get_or_create_collection("legal_kb")
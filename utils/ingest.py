import os

def ingest_docs(collection, embedder, path="knowledge_base"):
    docs = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # skip non-txt files just in case
        if not file_path.endswith(".txt"):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if text:
                docs.append(text)

    # 🔥 embeddings (numpy array → convert to list)
    embeddings = embedder.encode(docs)

    for i, doc in enumerate(docs):
        collection.add(
            documents=[doc],
            embeddings=[embeddings[i].tolist()],  # ✅ FIX
            ids=[f"doc_{i}"]
        )

    print(f"✅ Loaded {len(docs)} documents into ChromaDB")
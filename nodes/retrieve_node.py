def retrieve_node(state, collection, embedder):
    question = state["question"]

    # 🔥 FIX: encode as list → take first → convert to list
    emb = embedder.encode([question])[0].tolist()

    results = collection.query(
        query_embeddings=[emb],
        n_results=3
    )

    docs = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]

    state["retrieved"] = "\n".join(docs) if docs else ""
    state["sources"] = ids if ids else []

    return state
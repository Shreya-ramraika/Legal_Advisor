def router_node(state):
    q = state["question"].lower()

    # 🔥 Legal keywords
    legal_keywords = [
        "ipc", "law", "court", "legal", "section",
        "case", "bail", "fir", "police", "rights",
        "domestic violence", "dowry", "tenant",
        "cheque bounce", "agreement", "complaint"
    ]

    # ❗ OUT-OF-SCOPE CHECK
    if not any(k in q for k in legal_keywords):
        state["route"] = "out_of_scope"
        return state

    # TOOL ROUTING
    if any(k in q for k in ["ipc", "deadline"]):
        state["route"] = "tool"
    else:
        state["route"] = "retrieve"

    return state
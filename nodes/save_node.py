def save_node(state):
    state["messages"].append({
        "user": state["question"],
        "assistant": state["answer"]
    })
    return state
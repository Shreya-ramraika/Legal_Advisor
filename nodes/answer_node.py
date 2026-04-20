def answer_node(state, llm):
    context = state["retrieved"] or state["tool_result"]

    prompt = f"""
    Answer clearly:

    Question: {state['question']}
    Context: {context}
    """

    state["answer"] = llm.invoke(prompt).content
    return state
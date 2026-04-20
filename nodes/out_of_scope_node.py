def out_of_scope_node(state):
    state["answer"] = (
        "⚠️ I'm a legal AI assistant and can only help with legal-related questions.\n\n"
        "Please ask something related to:\n"
        "- Laws (IPC, rights)\n"
        "- Court procedures\n"
        "- Legal help or complaints\n\n"
        "Example: 'What is IPC 420?' or 'How to file FIR?'"
    )

    state["sources"] = []
    state["faithfulness"] = 1.0
    state["risk_score"] = 0

    return state
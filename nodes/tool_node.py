from tools.ipc_lookup import ipc_lookup
from tools.deadline_calculator import deadline_calc
from tools.legal_risk_analyzer import legal_risk

def tool_node(state):
    q = state["question"]

    if "ipc" in q.lower():
        state["tool_result"] = ipc_lookup(q)

    elif "deadline" in q.lower():
        state["tool_result"] = deadline_calc(q)

    state["risk_score"] = legal_risk(q)

    return state
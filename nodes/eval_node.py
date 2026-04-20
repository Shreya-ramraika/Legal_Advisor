from config import FAITHFULNESS_THRESHOLD

def eval_node(state):
    score = 0.9 if state["retrieved"] else 0.5

    state["faithfulness"] = score

    if score < FAITHFULNESS_THRESHOLD:
        state["eval_retries"] += 1
        state["route"] = "retry"
    else:
        state["route"] = "pass"

    return state
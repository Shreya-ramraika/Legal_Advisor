from typing import TypedDict, List

class LegalMindState(TypedDict):
    question: str
    messages: List[dict]

    route: str
    retrieved: str
    sources: List[str]

    tool_result: str
    answer: str

    faithfulness: float
    eval_retries: int

    risk_score: int
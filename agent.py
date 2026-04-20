from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from nodes.state import LegalMindState
from nodes.memory_node import memory_node
from nodes.router_node import router_node
from nodes.retrieve_node import retrieve_node
from nodes.tool_node import tool_node
from nodes.answer_node import answer_node
from nodes.eval_node import eval_node
from nodes.save_node import save_node
from nodes.out_of_scope_node import out_of_scope_node

from utils.llm import init_llm
from utils.embeddings import init_embedder
from utils.chroma_db import init_chromadb
from utils.ingest import ingest_docs

from config import FAITHFULNESS_THRESHOLD, MAX_EVAL_RETRIES


# ✅ MUST EXIST (this was missing / broken)
def init_all():
    llm = init_llm()
    embedder = init_embedder()
    collection = init_chromadb(embedder)

    ingest_docs(collection, embedder)

    return llm, embedder, collection


# ✅ MUST EXIST
def build_graph(llm, embedder, collection):

    builder = StateGraph(LegalMindState)

    # Nodes
    builder.add_node("memory", memory_node)
    builder.add_node("router", router_node)

    builder.add_node(
        "retrieve",
        lambda s: retrieve_node(s, collection, embedder)
    )

    builder.add_node("tool", tool_node)

    builder.add_node(
        "generate_answer",
        lambda s: answer_node(s, llm)
    )

    builder.add_node("eval", eval_node)
    builder.add_node("save", save_node)

    builder.add_node("out_of_scope", out_of_scope_node)

    # Entry
    builder.set_entry_point("memory")

    builder.add_edge("memory", "router")

    builder.add_conditional_edges(
        "router",
        lambda s: s["route"],
        {
            "retrieve": "retrieve",
            "tool": "tool",
            "out_of_scope": "out_of_scope"
        }
    )

    builder.add_edge("retrieve", "generate_answer")
    builder.add_edge("tool", "generate_answer")

    builder.add_edge("generate_answer", "eval")

    def eval_check(state):
        if (
            state["faithfulness"] < FAITHFULNESS_THRESHOLD
            and state["eval_retries"] < MAX_EVAL_RETRIES
        ):
            return "retry"
        return "pass"

    builder.add_conditional_edges(
        "eval",
        eval_check,
        {
            "retry": "generate_answer",
            "pass": "save"
        }
    )

    builder.add_edge("out_of_scope", "save")

    builder.add_edge("save", END)

    return builder.compile(checkpointer=MemorySaver())
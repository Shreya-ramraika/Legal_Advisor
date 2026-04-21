import streamlit as st
from agent import init_all, build_graph

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="⚖️ LegalMind AI",
    page_icon="⚖️",
    layout="wide"
)

# ─────────────────────────────────────────────
# TITLE
# ─────────────────────────────────────────────
st.title("⚖️ LegalMind AI")
st.markdown("### 🧠 Multi-Agent Legal Intelligence System")

# ─────────────────────────────────────────────
# LOAD SYSTEM (CACHED)
# ─────────────────────────────────────────────
@st.cache_resource
def load_system():
    llm, embedder, collection = init_all()
    app = build_graph(llm, embedder, collection)
    return app

app = load_system()

# ─────────────────────────────────────────────
# SESSION STATE (CHAT + THREAD ID)
# ─────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔥 IMPORTANT FIX: thread_id for LangGraph memory
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_session_1"

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ System Info")
    st.markdown("""
    - ✔ LangGraph Multi-Agent  
    - ✔ RAG (ChromaDB)  
    - ✔ Tools + Risk Analysis  
    - ✔ Self-Reflection Loop  
    """)

    st.divider()

    st.header("📊 Metrics Guide")
    st.markdown("""
    **Faithfulness**
    - >0.8 → Reliable  
    - <0.7 → Retry triggered  

    **Risk Score**
    - 0–3 → Low  
    - 4–7 → Medium  
    - 8–10 → High  
    """)

# ─────────────────────────────────────────────
# CHAT HISTORY DISPLAY
# ─────────────────────────────────────────────
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["user"])
    with st.chat_message("assistant"):
        st.markdown(chat["assistant"])

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
user_input = st.chat_input("Ask your legal question...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("⚡ LegalMind is analyzing..."):

            state = {
                "question": user_input,
                "messages": st.session_state.chat_history,
                "route": "",
                "retrieved": "",
                "sources": [],
                "tool_result": "",
                "answer": "",
                "faithfulness": 0,
                "eval_retries": 0,
                "risk_score": 0
            }

            result = app.invoke(
                state,
                config={
                    "configurable": {
                        "thread_id": st.session_state.thread_id
                    }
                }
            )

            answer = result["answer"]
            faith = result["faithfulness"]
            risk = result["risk_score"]
            sources = result.get("sources", [])

            st.markdown(answer)

            # Metrics
            col1, col2 = st.columns(2)

            with col1:
                st.metric("🧠 Faithfulness", round(faith, 2))

            with col2:
                st.metric("⚠️ Risk Score", risk)

            # Sources
            if sources:
                with st.expander("📚 Sources"):
                    for src in sources:
                        st.write(src)

    # Save chat
    st.session_state.chat_history.append({
        "user": user_input,
        "assistant": answer
    })
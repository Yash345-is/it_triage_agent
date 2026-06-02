# app.py
# Streamlit UI for the IT Support Triage Agent
# This is what management sees during the demo

import streamlit as st
from orchestrator import split_logs, process_all_logs

# ─────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="IT Support Triage Agent",
    page_icon="🤖",
    layout="wide"
)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.title("🤖 IT Support Log Triage Agent")
st.markdown("""
**Powered by:** LangGraph · LangChain · Llama 3 via Ollama · ChromaDB (RAG)  
**Architecture:** ReAct Agent Loop · Vector Knowledge Base · Automated Tool Execution
""")
st.divider()

# ─────────────────────────────────────────────
# SIDEBAR - architecture info for management
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("🏗️ Architecture")
    st.markdown("""
    **LLM**  
    Llama 3 running locally via Ollama  
    No data leaves this machine
    
    **Agent Framework**  
    LangGraph — state machine agent loop  
    LangChain — tools and prompt management
    
    **Knowledge Base**  
    ChromaDB vector database  
    RAG retrieval for low confidence logs
    
    **Tools Available**  
    🎫 Create Jira ticket  
    💬 Send Slack alert  
    🚨 Escalate P1 incidents  
    🔍 Search knowledge base  
    """)

    st.divider()
    st.header("📊 Severity Guide")
    st.markdown("""
    🔴 **P1** — Critical. Auto-escalated.  
    🟠 **P2** — High. Ticket + Alert.  
    🟡 **P3** — Medium. Ticket + Alert.  
    🟢 **P4** — Low. Ticket only.  
    """)

# ─────────────────────────────────────────────
# MAIN AREA - two columns
# ─────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📥 Input Logs")

    # load sample logs button
    if st.button("📂 Load Sample Logs"):
        with open("sample_logs.txt", "r") as f:
            st.session_state["log_input"] = f.read()

    # text area for log input
    log_input = st.text_area(
        "Paste logs here (separate multiple logs with ---)",
        value=st.session_state.get("log_input", ""),
        height=400,
        placeholder="Paste your IT support logs here...\n\nSeparate multiple logs with ---"
    )

    # show how many logs detected
    if log_input:
        logs = split_logs(log_input)
        st.info(f"📋 {len(logs)} log entries detected")

    # run button
    run_button = st.button(
        "🚀 Run Triage Agent",
        type="primary",
        use_container_width=True
    )

with col2:
    st.header("🔄 Agent Thought Stream")
    thought_container = st.container()

# ─────────────────────────────────────────────
# PROCESS LOGS WHEN RUN BUTTON CLICKED
# ─────────────────────────────────────────────
if run_button and log_input:
    logs = split_logs(log_input)

    if not logs:
        st.error("No logs detected. Please paste some logs first.")
    else:
        # results storage
        all_results = []

        # process each log
        for i, log in enumerate(logs):
            with thought_container:
                st.markdown(f"### Log {i+1} of {len(logs)}")
                st.code(log[:200], language="text")

                with st.spinner(f"Agent reasoning about log {i+1}..."):
                    result = process_all_logs(log)
                    all_results.extend(result)

                # display result
                severity = result[0]["severity"]
                team = result[0]["team"]
                summary = result[0]["summary"]
                confidence = result[0]["confidence"]
                actions = result[0]["final_summary"]

                # severity color
                color_map = {
                    "P1": "🔴",
                    "P2": "🟠",
                    "P3": "🟡",
                    "P4": "🟢"
                }
                emoji = color_map.get(severity, "⚪")

                st.success(f"{emoji} **{severity}** | Team: **{team}** | Confidence: **{confidence}%**")
                st.markdown(f"**Summary:** {summary}")

                with st.expander("📋 Actions Taken"):
                    st.text(actions)

                st.divider()

        # ─────────────────────────────────────────────
        # TRIAGE QUEUE - summary of all logs
        # ─────────────────────────────────────────────
        st.header("📊 Triage Queue")

        # metrics row
        p1_count = sum(1 for r in all_results if r["severity"] == "P1")
        p2_count = sum(1 for r in all_results if r["severity"] == "P2")
        p3_count = sum(1 for r in all_results if r["severity"] == "P3")
        p4_count = sum(1 for r in all_results if r["severity"] == "P4")

        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Total", len(all_results))
        m2.metric("🔴 P1 Critical", p1_count)
        m3.metric("🟠 P2 High", p2_count)
        m4.metric("🟡 P3 Medium", p3_count)
        m5.metric("🟢 P4 Low", p4_count)

        st.divider()

        # sort by severity
        severity_order = {"P1": 0, "P2": 1, "P3": 2, "P4": 3, "": 4}
        sorted_results = sorted(
            all_results,
            key=lambda x: severity_order.get(x["severity"], 4)
        )

        # display each ticket as a card
        for result in sorted_results:
            severity = result["severity"]
            emoji = color_map.get(severity, "⚪")

            with st.container():
                col_a, col_b, col_c = st.columns([1, 4, 2])
                with col_a:
                    st.markdown(f"## {emoji}")
                    st.markdown(f"**{severity}**")
                with col_b:
                    st.markdown(f"**{result['summary']}**")
                    st.markdown(f"Team: {result['team']} | Confidence: {result['confidence']}%")
                with col_c:
                    with st.expander("View Actions"):
                        st.text(result["final_summary"])
                st.divider()

elif run_button and not log_input:
    st.error("Please paste some logs or load the sample logs first.")
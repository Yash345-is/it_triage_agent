# agent.py
# LangGraph agent loop
# LLM reasons and classifies the log
# Graph enforces the workflow

from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
import json

from langchain_setup import llm, system_prompt
from tools import (
    create_jira_ticket,
    send_slack_alert,
    escalate_p1,
    kb_search
)

# ─────────────────────────────────────────────
# STEP A: Agent State
# ─────────────────────────────────────────────
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "append"]
    log: str
    iterations: int
    final_summary: str
    severity: str
    team: str
    summary: str
    confidence: int
    kb_results: str
    actions_taken: List[str]

# ─────────────────────────────────────────────
# STEP B: Reason node
# LLM classifies the log
# ─────────────────────────────────────────────
def reason_node(state: AgentState) -> AgentState:
    print(f"\n🧠 REASON (iteration {state['iterations'] + 1})")
    print(f"   Analysing: {state['log'][:80]}...")

    kb_context = ""
    if state["kb_results"]:
        kb_context = f"\n\nRelevant past incidents:\n{state['kb_results']}"

    prompt = f"""
You are an IT support triage agent. Analyse this log and respond with ONLY a JSON object. No other text.

LOG: {state['log']}
{kb_context}

Return ONLY this JSON — no explanation, no markdown, just the JSON:
{{
    "severity": "P1",
    "team": "SecOps",
    "summary": "one line summary",
    "confidence": 85,
    "reasoning": "brief reason",
    "recommended_actions": "steps to resolve"
}}

Severity rules:
- P1: outages, ransomware, security breaches, production down, data loss
- P2: high disk/CPU/memory, failed backups, SSL expiry, VPN issues
- P3: single user issues, warnings, license expiry
- P4: printer issues, minor requests

Team rules:
- NetOps: network, VPN, firewall, connectivity
- SecOps: security, suspicious logins, ransomware, DDoS
- SysAdmin: disk, CPU, memory, backups, Active Directory
- DevOps: deployments, SSL, application errors
- HelpDesk: user accounts, printers, software
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    print(f"   Raw LLM response: {response.content[:300]}")

    # parse JSON from response
    try:
        content = response.content.strip()

        # remove markdown code fences if present
        if "```" in content:
            parts = content.split("```")
            for part in parts:
                part = part.strip()
                if part.startswith("json"):
                    part = part[4:].strip()
                if part.startswith("{"):
                    content = part
                    break

        # find JSON object in response
        start = content.find("{")
        end = content.rfind("}") + 1
        if start >= 0 and end > start:
            content = content[start:end]

        parsed = json.loads(content)
        severity = parsed.get("severity", "P3").strip()
        team = parsed.get("team", "HelpDesk").strip()
        summary = parsed.get("summary", state["log"][:100]).strip()
        confidence = int(parsed.get("confidence", 50))
        recommended_actions = parsed.get("recommended_actions", "Investigate and resolve.")

        # validate severity
        if severity not in ["P1", "P2", "P3", "P4"]:
            severity = "P3"

        # validate team
        valid_teams = ["NetOps", "SecOps", "SysAdmin", "DevOps", "HelpDesk"]
        if team not in valid_teams:
            team = "HelpDesk"

        print(f"   ✅ Severity: {severity} | Team: {team} | Confidence: {confidence}%")

    except Exception as e:
        print(f"   ⚠️  Could not parse JSON: {e}")
        print(f"   Using smart defaults based on keywords...")

        # keyword based fallback
        log_lower = state["log"].lower()

        if any(w in log_lower for w in ["ransomware", "breach", "critical", "down", "ddos"]):
            severity = "P1"
        elif any(w in log_lower for w in ["warning", "98%", "100%", "failed", "ssl"]):
            severity = "P2"
        elif any(w in log_lower for w in ["user", "account", "license"]):
            severity = "P3"
        else:
            severity = "P4"

        if any(w in log_lower for w in ["network", "vpn", "firewall", "connectivity"]):
            team = "NetOps"
        elif any(w in log_lower for w in ["ransomware", "suspicious", "security", "ddos", "login"]):
            team = "SecOps"
        elif any(w in log_lower for w in ["disk", "cpu", "memory", "server", "backup"]):
            team = "SysAdmin"
        elif any(w in log_lower for w in ["deployment", "ssl", "application", "500"]):
            team = "DevOps"
        else:
            team = "HelpDesk"

        summary = state["log"][:100]
        confidence = 60
        recommended_actions = "Investigate and resolve the issue."

    return {
        "messages": [AIMessage(content=response.content)],
        "log": state["log"],
        "iterations": state["iterations"] + 1,
        "final_summary": state["final_summary"],
        "severity": severity,
        "team": team,
        "summary": summary,
        "confidence": confidence,
        "kb_results": state["kb_results"],
        "actions_taken": state["actions_taken"]
    }

# ─────────────────────────────────────────────
# STEP C: KB Search node (RAG)
# ─────────────────────────────────────────────
def kb_search_node(state: AgentState) -> AgentState:
    print(f"\n🔍 KB SEARCH — confidence {state['confidence']}% is below 75%")
    print(f"   Searching knowledge base for similar incidents...")

    results = kb_search(query=state["log"])
    print(f"   ✅ Knowledge base results retrieved")

    return {
        "messages": state["messages"],
        "log": state["log"],
        "iterations": state["iterations"],
        "final_summary": state["final_summary"],
        "severity": state["severity"],
        "team": state["team"],
        "summary": state["summary"],
        "confidence": state["confidence"],
        "kb_results": results,
        "actions_taken": state["actions_taken"]
    }

# ─────────────────────────────────────────────
# STEP D: Act node
# Executes all tools based on classification
# ─────────────────────────────────────────────
def act_node(state: AgentState) -> AgentState:
    print(f"\n⚡ ACT — executing tools")
    actions_taken = []

    # always create jira ticket
    print(f"   🎫 Creating Jira ticket...")
    jira_result = create_jira_ticket(
        summary=state["summary"],
        severity=state["severity"],
        team=state["team"],
        description=state["log"],
        recommended_actions=f"Severity: {state['severity']} | Team: {state['team']}"
    )
    actions_taken.append(jira_result)

    # always send slack alert
    print(f"   💬 Sending Slack alert...")
    # send slack alert only for P1 and P2
    channel_map = {
        "NetOps": "netops-alerts",
        "SecOps": "security-alerts",
        "SysAdmin": "sysadmin-alerts",
        "DevOps": "devops-alerts",
        "HelpDesk": "helpdesk-tickets"
    }
    channel = channel_map.get(state["team"], "ops-alerts")

    if state["severity"] in ["P1", "P2"]:
        print(f"   💬 Sending Slack alert...")
        slack_result = send_slack_alert(
            channel=channel,
            severity=state["severity"],
            summary=state["summary"],
            team=state["team"]
        )
        actions_taken.append(slack_result)
    else:
        print(f"   ℹ️  {state['severity']} — Jira ticket created, no Slack alert needed")
        actions_taken.append(f"ℹ️  {state['severity']} incident — Jira ticket created. No Slack alert for {state['severity']}.")

    # escalate if P1
    if state["severity"] == "P1":
        print(f"   🚨 P1 detected — escalating immediately...")
        escalation_result = escalate_p1(
            summary=state["summary"],
            team=state["team"],
            reason=f"P1 critical incident: {state['log'][:100]}"
        )
        actions_taken.append(escalation_result)

    return {
        "messages": state["messages"],
        "log": state["log"],
        "iterations": state["iterations"],
        "final_summary": "\n".join(actions_taken),
        "severity": state["severity"],
        "team": state["team"],
        "summary": state["summary"],
        "confidence": state["confidence"],
        "kb_results": state["kb_results"],
        "actions_taken": actions_taken
    }

# ─────────────────────────────────────────────
# STEP E: Conditional edges
# ─────────────────────────────────────────────
def after_reason(state: AgentState) -> str:
    if state["confidence"] < 75 and state["iterations"] == 1:
        print(f"\n   ⚠️  Confidence {state['confidence']}% below threshold — querying KB")
        return "kb_search"
    print(f"\n   ✅ Confidence {state['confidence']}% — proceeding to act")
    return "act"

def after_kb_search(state: AgentState) -> str:
    return "reason"

# ─────────────────────────────────────────────
# STEP F: Build LangGraph
# ─────────────────────────────────────────────
def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("reason", reason_node)
    graph.add_node("kb_search", kb_search_node)
    graph.add_node("act", act_node)

    graph.set_entry_point("reason")

    graph.add_conditional_edges(
        "reason",
        after_reason,
        {
            "kb_search": "kb_search",
            "act": "act"
        }
    )

    graph.add_conditional_edges(
        "kb_search",
        after_kb_search,
        {
            "reason": "reason"
        }
    )

    graph.add_edge("act", END)

    return graph.compile()

# ─────────────────────────────────────────────
# STEP G: Process one log
# ─────────────────────────────────────────────
def process_log(log: str) -> dict:
    print(f"\n{'='*60}")
    print(f"📋 Processing: {log[:80]}...")
    print(f"{'='*60}")

    agent = build_agent()

    initial_state = {
        "messages": [],
        "log": log,
        "iterations": 0,
        "final_summary": "",
        "severity": "",
        "team": "",
        "summary": "",
        "confidence": 0,
        "kb_results": "",
        "actions_taken": []
    }

    final_state = agent.invoke(initial_state)

    print(f"\n✅ Done — {final_state['iterations']} iterations")
    print(f"   Severity  : {final_state['severity']}")
    print(f"   Team      : {final_state['team']}")
    print(f"   Confidence: {final_state['confidence']}%")

    return final_state

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    test_logs = [
        "CRITICAL: Disk usage at 98% on PROD-SERVER-01. Application throwing write errors.",
        "ALERT: Suspicious login from IP 185.234.219.57. Admin accessing files at 2:47am.",
        "WARNING: Printer on 3rd floor not responding. Jobs stuck in queue."
    ]

    for log in test_logs:
        result = process_log(log)
        print(f"\nSeverity: {result['severity']} | Team: {result['team']}")
        print(result["final_summary"])
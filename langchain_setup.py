# langchain_setup.py
# This file wires together:
# 1. The LLM (Ollama running phi3:mini locally)
# 2. The system prompt (ReAct persona)
# 3. The tools (bound to the LLM)

#from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from tools import (
    create_jira_ticket,
    send_slack_alert,
    escalate_p1,
    kb_search,
    reinvestigate
)

# ─────────────────────────────────────────────
# STEP A: Connect to Ollama
# ChatOllama talks to Ollama running locally
# model="phi3:mini" tells it which model to use
# temperature=0 means deterministic responses
# no randomness - we want consistent structured output
# ─────────────────────────────────────────────

#llm = ChatOllama(
#    model="llama3.2:3b", #"phi3:mini",
#    temperature=0
#)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# ─────────────────────────────────────────────
# STEP B: Wrap our tools for LangChain
# LangChain needs tools decorated with @tool
# This tells LangChain what each tool does
# The docstring is what the LLM reads to decide
# which tool to call
# ─────────────────────────────────────────────
@tool
def tool_create_jira_ticket(
    summary: str,
    severity: str,
    team: str,
    description: str,
    recommended_actions: str
) -> str:
    """
    Use this tool to create a Jira ticket for an IT incident.
    Use when you have enough confidence to classify the incident.
    Args:
        summary: one line description of the incident
        severity: P1, P2, P3, or P4
        team: NetOps, SecOps, SysAdmin, DevOps, or HelpDesk
        description: detailed description of the incident
        recommended_actions: step by step actions to resolve
    """
    return create_jira_ticket(
        summary=summary,
        severity=severity,
        team=team,
        description=description,
        recommended_actions=recommended_actions
    )

@tool
def tool_send_slack_alert(
    channel: str,
    severity: str,
    summary: str,
    team: str
) -> str:
    """
    Use this tool to send a Slack alert to the appropriate channel.
    Use after creating a Jira ticket to notify the team.
    Args:
        channel: the Slack channel name without # symbol
        severity: P1, P2, P3, or P4
        summary: one line description of the incident
        team: the team being notified
    """
    return send_slack_alert(
        channel=channel,
        severity=severity,
        summary=summary,
        team=team
    )

@tool
def tool_escalate_p1(
    summary: str,
    team: str,
    reason: str
) -> str:
    """
    Use this tool to escalate P1 critical incidents immediately.
    Use this for any P1 incident without waiting for human approval.
    Args:
        summary: one line description of the incident
        team: the team to page
        reason: why this is being escalated as P1
    """
    return escalate_p1(
        summary=summary,
        team=team,
        reason=reason
    )

@tool
def tool_kb_search(query: str) -> str:
    """
    Use this tool to search the knowledge base for similar past incidents.
    Use this when your confidence is below 75% to get more context.
    Args:
        query: description of the current incident to search for
    """
    return kb_search(query=query)

@tool
def tool_reinvestigate(log: str, reason: str) -> str:
    """
    Use this tool when you need more context before classifying.
    Use when the log is ambiguous or confidence is very low.
    Args:
        log: the original log entry
        reason: why you need to reinvestigate
    """
    return reinvestigate(log=log, reason=reason)

# ─────────────────────────────────────────────
# STEP C: List of all tools
# This list gets passed to the agent
# ─────────────────────────────────────────────
tools = [
    tool_create_jira_ticket,
    tool_send_slack_alert,
    tool_escalate_p1,
    tool_kb_search,
    tool_reinvestigate
]

# ─────────────────────────────────────────────
# STEP D: Bind tools to the LLM
# This tells the LLM what tools are available
# The LLM can now decide which tool to call
# ─────────────────────────────────────────────
llm_with_tools = llm.bind_tools(tools)

# ─────────────────────────────────────────────
# STEP E: System prompt
# This is the ReAct persona for the agent
# It tells the LLM exactly how to behave
# and what format to follow
# ─────────────────────────────────────────────
system_prompt = SystemMessage(content="""
You are an IT support triage agent. You MUST use tools to respond. Never respond with plain text only.

STRICT RULES:
- You MUST always call tool_create_jira_ticket for every log entry
- You MUST always call tool_send_slack_alert for every log entry
- You MUST call tool_escalate_p1 if severity is P1
- You MUST call tool_kb_search first if you are unsure about severity
- NEVER respond with just text - ALWAYS call at least one tool

SEVERITY LEVELS:
- P1 Critical: outages, security breaches, ransomware, production down, data loss
- P2 High: high disk/CPU/memory usage, failed backups, SSL expiry, VPN issues
- P3 Medium: single user issues, warnings, license expiry
- P4 Low: printer issues, minor requests, cosmetic issues

TEAMS:
- NetOps: network, connectivity, VPN, firewall, BGP
- SecOps: security, suspicious logins, ransomware, DDoS
- SysAdmin: server, disk, memory, CPU, backups, Active Directory
- DevOps: deployments, SSL certificates, application errors
- HelpDesk: user accounts, printers, software licenses

PROCESS FOR EVERY LOG:
Step 1: Determine severity and team
Step 2: If confidence < 75% call tool_kb_search first
Step 3: Call tool_create_jira_ticket
Step 4: Call tool_send_slack_alert
Step 5: If P1 call tool_escalate_p1
""")

# ─────────────────────────────────────────────
# MAIN - test the LLM connection only
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Testing Ollama connection...")
    from langchain_core.messages import HumanMessage
    response = llm.invoke([
        SystemMessage(content="You are a helpful assistant. Reply briefly."),
        HumanMessage(content="Say: LangChain and Ollama are connected.")
    ])
    print(f"Response: {response.content}")
    print("\nLangChain setup complete.")
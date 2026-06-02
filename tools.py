# tools.py
# These are the actions the agent can take
# Each function is a "tool" the agent can call
# They are all mocked for the demo
# In production you would replace the mock with a real API call

import uuid
from datetime import datetime
from knowledge_base import search_knowledge_base

# ─────────────────────────────────────────────
# TOOL 1: Create a Jira ticket
# In production: call the Jira REST API
# In demo: returns a realistic fake ticket ID
# ─────────────────────────────────────────────
def create_jira_ticket(
    summary: str,
    severity: str,
    team: str,
    description: str,
    recommended_actions: str
) -> str:
    """
    Creates a Jira ticket for the incident.
    Returns a ticket ID and confirmation.
    """
    ticket_id = f"INC-{uuid.uuid4().hex[:6].upper()}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = f"""
✅ JIRA TICKET CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ticket ID    : {ticket_id}
Summary      : {summary}
Severity     : {severity}
Assigned To  : {team}
Created At   : {timestamp}
Description  : {description}
Next Steps   : {recommended_actions}
Status       : Open
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return result

# ─────────────────────────────────────────────
# TOOL 2: Send a Slack alert
# In production: POST to a Slack Incoming Webhook URL
# In demo: returns a realistic confirmation message
# ─────────────────────────────────────────────
def send_slack_alert(
    channel: str,
    severity: str,
    summary: str,
    team: str
) -> str:
    """
    Sends a Slack alert to the appropriate channel.
    Returns confirmation of the alert sent.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emoji = {
        "P1": "🔴",
        "P2": "🟠",
        "P3": "🟡",
        "P4": "🟢"
    }.get(severity, "⚪")

    result = f"""
💬 SLACK ALERT SENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Channel      : #{channel}
Severity     : {emoji} {severity}
Summary      : {summary}
Assigned To  : {team}
Sent At      : {timestamp}
Message      : [{severity}] {emoji} {summary} — Assigned to {team}. Please investigate immediately.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return result

# ─────────────────────────────────────────────
# TOOL 3: Escalate P1 incidents
# In production: page the on-call engineer via PagerDuty
# In demo: returns a realistic escalation confirmation
# ─────────────────────────────────────────────
def escalate_p1(
    summary: str,
    team: str,
    reason: str
) -> str:
    """
    Escalates a P1 incident to the on-call engineer.
    No human approval needed — fires automatically.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    escalation_id = f"ESC-{uuid.uuid4().hex[:6].upper()}"

    result = f"""
🚨 P1 ESCALATION FIRED — NO APPROVAL NEEDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Escalation ID : {escalation_id}
Summary       : {summary}
Team Paged    : {team} On-Call Engineer
Reason        : {reason}
Fired At      : {timestamp}
Method        : PagerDuty (simulated)
Status        : On-call engineer notified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return result

# ─────────────────────────────────────────────
# TOOL 4: Search knowledge base (RAG)
# Calls the search function from knowledge_base.py
# Agent uses this when confidence is low
# ─────────────────────────────────────────────
def kb_search(query: str) -> str:
    """
    Searches the knowledge base for similar past incidents.
    Returns top 3 matches with resolutions.
    This is the RAG step — enriches agent context.
    """
    return search_knowledge_base(query)

# ─────────────────────────────────────────────
# TOOL 5: Re-investigate
# Agent calls this when it needs more context
# Prompts the agent to look more carefully
# ─────────────────────────────────────────────
def reinvestigate(log: str, reason: str) -> str:
    """
    Flags a log for deeper investigation.
    Returns additional context and flags for review.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = f"""
🔍 RE-INVESTIGATION TRIGGERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reason        : {reason}
Log           : {log}
Triggered At  : {timestamp}
Action        : Querying knowledge base for additional context
Note          : Confidence was below threshold — agent is gathering more information before deciding
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return result

# ─────────────────────────────────────────────
# MAIN - test this file directly
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Testing tools...\n")

    print("1. Testing Jira ticket creation:")
    print(create_jira_ticket(
        summary="Disk usage at 98% on production server",
        severity="P2",
        team="SysAdmin",
        description="Server disk is almost full causing write errors",
        recommended_actions="Run log rotation script and clear /tmp directory"
    ))

    print("2. Testing Slack alert:")
    print(send_slack_alert(
        channel="ops-alerts",
        severity="P2",
        summary="Disk usage at 98% on production server",
        team="SysAdmin"
    ))

    print("3. Testing P1 escalation:")
    print(escalate_p1(
        summary="Ransomware detected on workstation",
        team="SecOps",
        reason="Ransomware is a critical security threat requiring immediate response"
    ))

    print("4. Testing KB search:")
    print(kb_search("disk is full on server"))

    print("5. Testing re-investigate:")
    print(reinvestigate(
        log="Unknown error on server at 3am",
        reason="Confidence too low to classify"
    ))
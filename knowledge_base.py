# knowledge_base.py
# This file creates our in-memory vector database of past IT incidents
# ChromaDB handles embeddings internally using onnxruntime - no torch required

import chromadb
from chromadb.utils import embedding_functions

# ─────────────────────────────────────────────
# STEP A: Create embedding function
# ChromaDB's default embedder uses onnxruntime
# Works on any Windows machine without GPU
# ─────────────────────────────────────────────
print("Initialising knowledge base...")
embedding_func = embedding_functions.DefaultEmbeddingFunction()

# ─────────────────────────────────────────────
# STEP B: Create in-memory ChromaDB
# Lives only while the app runs
# Nothing saved to disk
# ─────────────────────────────────────────────
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(
    name="it_incidents",
    embedding_function=embedding_func
)

# ─────────────────────────────────────────────
# STEP C: 20 past IT incidents
# In a real company this would come from
# your ServiceNow or Jira history
# ─────────────────────────────────────────────
past_incidents = [
    {
        "id": "INC001",
        "incident": "Disk usage at 98% on production server. Application throwing write errors.",
        "resolution": "Ran log rotation script. Cleared /tmp directory. Freed 40GB. Monitoring set to alert at 80%.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC002",
        "incident": "Network switch unresponsive. Multiple servers losing connectivity. BGP routes dropping.",
        "resolution": "Restarted switch management interface. BGP sessions re-established. Root cause: firmware bug. Scheduled firmware update.",
        "severity": "P1",
        "team": "NetOps"
    },
    {
        "id": "INC003",
        "incident": "User unable to login. Account locked after multiple failed attempts.",
        "resolution": "Unlocked account in Active Directory. Reset password. Enabled MFA. Educated user on password policy.",
        "severity": "P3",
        "team": "HelpDesk"
    },
    {
        "id": "INC004",
        "incident": "CPU usage at 100% on database server. Queries timing out. Application slow.",
        "resolution": "Identified runaway query. Killed process. Added index to slow query. CPU returned to 20%.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC005",
        "incident": "SSL certificate expired on customer portal. Users seeing security warning in browser.",
        "resolution": "Renewed SSL certificate via certbot. Restarted nginx. Verified HTTPS working. Set calendar reminder 30 days before next expiry.",
        "severity": "P2",
        "team": "DevOps"
    },
    {
        "id": "INC006",
        "incident": "Ransomware detected on workstation. Files being encrypted. Network shares at risk.",
        "resolution": "Immediately isolated machine from network. Engaged SecOps. Reimaged workstation. Restored files from backup. Reported to management.",
        "severity": "P1",
        "team": "SecOps"
    },
    {
        "id": "INC007",
        "incident": "Memory usage at 95% on web server. Application throwing out of memory errors.",
        "resolution": "Restarted application server. Identified memory leak in application code. Raised bug ticket with dev team. Added memory to server as temporary fix.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC008",
        "incident": "Email server down. Users unable to send or receive emails company wide.",
        "resolution": "Found mail queue full due to spam flood. Cleared queue. Updated spam filter rules. Restarted mail service.",
        "severity": "P1",
        "team": "NetOps"
    },
    {
        "id": "INC009",
        "incident": "VPN connection dropping repeatedly for remote users. Cannot access internal systems.",
        "resolution": "Found VPN concentrator overloaded. Rebalanced connections across two concentrators. Updated VPN client on affected machines.",
        "severity": "P2",
        "team": "NetOps"
    },
    {
        "id": "INC010",
        "incident": "Database backup job failed. Last successful backup was 3 days ago.",
        "resolution": "Found backup drive full. Deleted backups older than 90 days. Re-ran backup job successfully. Set up automated cleanup policy.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC011",
        "incident": "Suspicious login from unknown IP in Russia. User account accessing sensitive files at 3am.",
        "resolution": "Immediately disabled account. Forced password reset. Reviewed access logs. No data exfiltration confirmed. Enabled geo-blocking.",
        "severity": "P1",
        "team": "SecOps"
    },
    {
        "id": "INC012",
        "incident": "Application deployment failed. Production site returning 500 errors.",
        "resolution": "Rolled back to previous deployment. Identified missing environment variable in new release. Fixed config. Redeployed successfully.",
        "severity": "P1",
        "team": "DevOps"
    },
    {
        "id": "INC013",
        "incident": "Printer not working for entire department. Print jobs stuck in queue.",
        "resolution": "Cleared stuck print queue on print server. Restarted print spooler service. All printers back online.",
        "severity": "P4",
        "team": "HelpDesk"
    },
    {
        "id": "INC014",
        "incident": "Network latency spike. Ping times to core router above 2000ms. Users complaining of slowness.",
        "resolution": "Found network loop caused by rogue switch plugged in by user. Removed switch. Latency returned to normal immediately.",
        "severity": "P2",
        "team": "NetOps"
    },
    {
        "id": "INC015",
        "incident": "Active Directory replication failing between domain controllers. Group policy not applying.",
        "resolution": "Fixed replication by running repadmin /syncall. Found DNS misconfiguration as root cause. Corrected DNS records.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC016",
        "incident": "DDoS attack detected. Web server receiving 50000 requests per second. Site down.",
        "resolution": "Enabled DDoS protection on firewall. Blocked attacking IP ranges. Enabled CDN rate limiting. Site restored in 15 minutes.",
        "severity": "P1",
        "team": "SecOps"
    },
    {
        "id": "INC017",
        "incident": "Storage array showing failed disk. RAID degraded. Risk of data loss.",
        "resolution": "Replaced failed disk. RAID rebuild initiated. Took 4 hours. Verified data integrity. Ordered spare disk for stock.",
        "severity": "P2",
        "team": "SysAdmin"
    },
    {
        "id": "INC018",
        "incident": "Software license expired. Users unable to open application.",
        "resolution": "Purchased license renewal. Applied new license key. All users able to access application.",
        "severity": "P3",
        "team": "HelpDesk"
    },
    {
        "id": "INC019",
        "incident": "Firewall rule misconfiguration blocking legitimate traffic to payment gateway.",
        "resolution": "Identified incorrect deny rule added during last change window. Removed rule. Payment traffic restored. Change review process updated.",
        "severity": "P1",
        "team": "NetOps"
    },
    {
        "id": "INC020",
        "incident": "Server room temperature rising. Cooling unit showing fault alarm.",
        "resolution": "Contacted facilities. Secondary cooling unit activated. Primary unit serviced. Temperature stabilised. Thermal monitoring alert threshold lowered.",
        "severity": "P2",
        "team": "SysAdmin"
    }
]

# ─────────────────────────────────────────────
# STEP D: Seed ChromaDB with past incidents
# ChromaDB converts text to vectors automatically
# ─────────────────────────────────────────────
print("Seeding knowledge base with past incidents...")

documents = []
metadatas = []
ids = []

for incident in past_incidents:
    full_text = f"Incident: {incident['incident']} Resolution: {incident['resolution']}"
    documents.append(full_text)
    metadatas.append({
        "id": incident["id"],
        "severity": incident["severity"],
        "team": incident["team"],
        "resolution": incident["resolution"]
    })
    ids.append(incident["id"])

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print(f"Knowledge base ready. {len(past_incidents)} incidents loaded.")

# ─────────────────────────────────────────────
# STEP E: Search function the agent calls
# This is the RAG retrieval step
# Agent calls this when confidence is low
# ─────────────────────────────────────────────
def search_knowledge_base(query: str) -> str:
    """
    Search for past incidents similar to the query.
    Returns top 3 matches with resolutions.
    """
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    if not results["documents"][0]:
        return "No similar incidents found in knowledge base."

    formatted = "Similar past incidents found:\n\n"
    for i, (doc, metadata) in enumerate(
        zip(results["documents"][0], results["metadatas"][0])
    ):
        formatted += f"Past Incident {i+1} [{metadata['id']}]:\n"
        formatted += f"Severity: {metadata['severity']} | Team: {metadata['team']}\n"
        formatted += f"Details: {doc}\n"
        formatted += f"Resolution: {metadata['resolution']}\n\n"

    return formatted

# ─────────────────────────────────────────────
# MAIN - test this file directly
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\nTesting knowledge base search...\n")
    result = search_knowledge_base(
        "server disk is almost full and applications are failing"
    )
    print(result)
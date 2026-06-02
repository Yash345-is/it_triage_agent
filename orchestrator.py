# orchestrator.py
# Manages the queue of logs
# Reads logs from input, splits them into individual entries
# Feeds each log into the agent one by one
# Collects and returns all results

from agent import process_log

# ─────────────────────────────────────────────
# STEP A: Split raw input into individual logs
# Logs are separated by --- in our sample file
# ─────────────────────────────────────────────
def split_logs(raw_input: str) -> list:
    """
    Splits a block of text into individual log entries.
    Entries are separated by --- 
    Empty entries are removed.
    """
    logs = raw_input.split("---")
    # clean each log - remove extra whitespace
    logs = [log.strip() for log in logs]
    # remove empty entries
    logs = [log for log in logs if log]
    return logs

# ─────────────────────────────────────────────
# STEP B: Process all logs
# Feeds each log into the agent
# Collects results
# ─────────────────────────────────────────────
def process_all_logs(raw_input: str) -> list:
    """
    Takes raw log input (pasted text or file content).
    Splits into individual logs.
    Processes each through the agent.
    Returns list of results.
    """
    logs = split_logs(raw_input)
    print(f"\n📥 Received {len(logs)} log entries to process")

    results = []
    for i, log in enumerate(logs):
        print(f"\n[{i+1}/{len(logs)}] Processing log...")
        result = process_log(log)
        results.append(result)

    print(f"\n✅ All {len(logs)} logs processed")
    return results

# ─────────────────────────────────────────────
# MAIN - test with sample logs file
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # read sample logs from file
    with open("sample_logs.txt", "r") as f:
        raw_input = f.read()

    results = process_all_logs(raw_input)

    print("\n" + "="*60)
    print("ALL RESULTS SUMMARY")
    print("="*60)
    for i, result in enumerate(results):
        print(f"\nLog {i+1}:")
        print(f"  Severity  : {result['severity']}")
        print(f"  Team      : {result['team']}")
        print(f"  Summary   : {result['summary']}")
        print(f"  Confidence: {result['confidence']}%")
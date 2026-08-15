import datetime
import json

def ir_response(incident):
    print("\n=== INCIDENT RESPONSE TRIGGERED ===")
    print("Time :", datetime.datetime.now())
    print("Type :", incident["type"])
    print("Severity :", incident["severity"])

    actions = []

    if incident["severity"] in ("HIGH", "CRITICAL"):
        actions += [
            "LOCK user account",
            "Revoke active sessions",
            "Notify SOC team",
            "Preserve mail logs"
        ]

    if incident["type"] == "phishing":
        actions += [
            "Quarantine email",
            "Block sender domain",
            "Scan attachments in sandbox"
        ]

    print("\nActions Taken:")
    for action in actions:
        print("[x]", action)

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\nIR report saved: ir_report.json")

print("===== DAY 14 INCIDENT RESPONSE =====")
ir_response({
    "type": "phishing",
    "severity": "HIGH",
    "user": "trainee@lab.local"
})

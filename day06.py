def spear_phish_template(target):
    return f"""
===== SPEAR PHISHING AWARENESS SIMULATION =====
SIMULATION ONLY - DO NOT SEND

From    : Security Awareness Lab
To      : {target["email"]}
Subject : Account Verification Training Scenario

Hi {target["name"]},

This is a simulated security-awareness exercise for {target["company"]}.

Scenario:
A suspicious message claims unusual account activity
and asks the employee to verify an account.

Training Link:
https://lab.internal/awareness-test

Red Flags:
1. Unexpected account-security message
2. Urgent language or deadline
3. Request to verify through a link
4. Sender identity should be independently verified

Safe Response:
- Do not enter passwords or OTPs.
- Do not open unexpected links.
- Verify through an official channel.
- Report suspicious messages.

===== END SIMULATION =====
"""

target = {
    "name": "Training User",
    "email": "trainee@lab.local",
    "company": "Training Lab"
}

print(spear_phish_template(target))

def generate_vishing_script(target_company, attacker_role, pretext):
    return f"""
===== VISHING AWARENESS SCRIPT =====
Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER]
Hi, this is Alex from IT Support at {target_company}.
We detected unusual activity on your account.

[RED FLAGS]
- Unexpected security request
- Urgency or fear
- Request for sensitive information
- Sender/caller should be independently verified

[DEFENSIVE RESPONSE]
Never provide passwords or OTPs.
Verify through an official channel.
"""

print(generate_vishing_script(
    "Training Lab", "IT Support", "Password Reset"
))

import json

QUESTIONS = [
    {
        "q": "An email asks you to verify your password via a link. You should:",
        "opts": ["A) Click the link", "B) Call IT directly", "C) Reply with password"],
        "ans": "B",
        "exp": "Always verify through official channels."
    },
    {
        "q": "You find a USB drive in the parking lot. You should:",
        "opts": ["A) Plug it in", "B) Hand it to security", "C) Keep it"],
        "ans": "B",
        "exp": "USB drops are a classic baiting vector."
    },
    {
        "q": "Someone claiming to be IT asks for your OTP. You should:",
        "opts": ["A) Give it", "B) Verify through official IT", "C) Email it"],
        "ans": "B",
        "exp": "Never share passwords or OTPs."
    },
    {
        "q": "An urgent email asks you to open an unexpected attachment.",
        "opts": ["A) Open it", "B) Verify sender", "C) Forward it"],
        "ans": "B",
        "exp": "Verify unexpected attachments first."
    },
    {
        "q": "A caller pressures you to bypass security procedures.",
        "opts": ["A) Follow caller", "B) End call and verify", "C) Give information"],
        "ans": "B",
        "exp": "Verify independently."
    },
    {
        "q": "You receive a suspicious password-reset message.",
        "opts": ["A) Use link", "B) Visit official site", "C) Reply with password"],
        "ans": "B",
        "exp": "Use an official channel."
    },
    {
        "q": "A stranger asks for confidential company information.",
        "opts": ["A) Share it", "B) Verify identity", "C) Post it"],
        "ans": "B",
        "exp": "Share sensitive information only with authorized people."
    },
    {
        "q": "Your account will be deleted today, according to a message.",
        "opts": ["A) Click link", "B) Verify officially", "C) Send password"],
        "ans": "B",
        "exp": "Urgent deadlines are common social-engineering tactics."
    },
    {
        "q": "A suspicious message asks you to keep the request secret.",
        "opts": ["A) Keep secret", "B) Report and verify", "C) Follow it"],
        "ans": "B",
        "exp": "Report suspicious requests."
    },
    {
        "q": "What should you do when you suspect phishing?",
        "opts": ["A) Report it", "B) Reply", "C) Forward to everyone"],
        "ans": "A",
        "exp": "Use the organization's security reporting process."
    }
]

score = 0
print("===== DAY 11 SOCIAL ENGINEERING AWARENESS =====")

for i, q in enumerate(QUESTIONS, 1):
    print(f"\nQ{i}: {q['q']}")
    for option in q["opts"]:
        print(option)

    answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == q["ans"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong.")
        print("Explanation:", q["exp"])

result = {
    "score": score,
    "total": len(QUESTIONS),
    "percentage": round(score / len(QUESTIONS) * 100)
}

with open("day11_score.json", "w") as f:
    json.dump(result, f, indent=2)

print("\n===== QUIZ COMPLETE =====")
print(f"Score: {score}/{len(QUESTIONS)}")
print(f"Percentage: {result['percentage']}%")
print("Report saved to: day11_score.json")

import re
from urllib.parse import urlparse

KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]

def phish_score(url):
    p = urlparse(url)
    score = 0

    if not url.startswith("https"):
        score += 30

    for kw in KEYWORDS:
        if kw in p.netloc.lower():
            score += 20

    if p.netloc.count(".") > 3:
        score += 25

    if re.search(r"\d{1,3}(?:\.\d{1,3}){3}", p.netloc):
        score += 40

    return min(score, 100)

urls = [
    "https://paypal-login.evil.com/verify",
    "https://github.com"
]

print("===== DAY 3 PHISHING URL DETECTOR =====")
for url in urls:
    print(f"{url} -> Risk: {phish_score(url)}%")

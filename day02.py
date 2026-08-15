import re
import requests

def harvest_emails(url):
    html = requests.get(url, timeout=10).text
    return set(re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", html))

# Use only an authorized lab/your own domain.
html = """<p>security@example.org</p>
<p>support@example.com</p>
<p>trainer@example.com</p>"""

emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", html))

print("===== DAY 2 EMAIL HARVESTING =====")
for email in sorted(emails):
    print("-", email)
print("Total Emails:", len(emails))

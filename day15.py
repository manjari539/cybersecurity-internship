# se_chain.py - Full SE Simulation Chain

import sys

MODULES = {
    "osint": "Run passive OSINT on a domain",
    "profile": "Build target profile from public data",
    "phish": "Score a URL for phishing indicators",
    "template": "Generate spear-phishing training email",
    "ir": "Trigger incident response workflow"
}

def menu():
    print("\nSE CHAIN SIMULATOR")
    print("Sqrock Cybersecurity Internship")

    for key, value in MODULES.items():
        print(f"[{key}] {value}")

    choice = input("\nSelect module: ").strip().lower()

    if choice in MODULES:
        print(f"\n[+] Launching {choice} module...")
        # Each module is imported from previous days' scripts.
    else:
        print("Invalid choice.")
        menu()

if __name__ == "__main__":
    menu()

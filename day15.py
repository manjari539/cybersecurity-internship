# se_chain.py — Full SE Simulation Chain

import sys

MODULES = {
    "osint": "Run passive OSINT on a domain",
    "profile": "Build target profile from public data",
    "phish": "Score a URL for phishing indicators",
    "template": "Generate spear-phishing training email",
    "ir": "Trigger incident response workflow"
}


def menu():

    print("\n■■■ SE CHAIN SIMULATOR ■■■■■■■■■■■■■■■■■■■")
    print("■ Sqrock Cybersecurity Internship ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

    for k, v in MODULES.items():
        print(f" [{k}] {v}")

    choice = input("\nSelect module: ").strip().lower()

    if choice in MODULES:
        print(f"\n[+] Launching {choice} module...")
        print("[+] Simulation mode")
        print("[+] Authorized training environment only")
      

        # Each module is imported from previous days' scripts

    else:
        print("Invalid choice.")
        menu()


if __name__ == "__main__":
    menu()

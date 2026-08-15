import platform
import socket
import datetime
import os

def usb_payload_sim(output_file="recon_log.txt"):
    info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd()
    }

    with open(output_file, "w") as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print(f"[SIM] Recon data saved to {output_file}")

print("===== DAY 8 USB DROP SIMULATION =====")
print("SIMULATION ONLY - BENIGN PAYLOAD")
usb_payload_sim()

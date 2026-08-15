from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

LOG = []

class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?")
        }

        LOG.append(entry)
        print(json.dumps(entry))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting the security awareness lab!")

    def log_message(self, *args):
        pass

print("===== DAY 10 BAITING & WATERING HOLE SIMULATION =====")
print("SIMULATION ONLY - LOCAL LAB")
print("Honeypot: http://localhost:8080")
print("Waiting for a training visit...")

HTTPServer(("127.0.0.1", 8080), HoneyHandler).serve_forever()

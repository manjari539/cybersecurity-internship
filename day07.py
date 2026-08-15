from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)
ATTEMPTS = {}
WINDOW = 10
LIMIT = 5

@app.post("/login")
def login():
    ip = request.remote_addr
    now = time.time()
    attempts = [t for t in ATTEMPTS.get(ip, []) if now - t < WINDOW]

    if len(attempts) >= LIMIT:
        return jsonify({"error": "rate limit triggered"}), 429

    ATTEMPTS[ip] = attempts + [now]

    if request.form.get("username") == "admin" and request.form.get("password") == "password":
        return "Welcome", 200

    return "Unauthorized", 401

if __name__ == "__main__":
    print("===== DAY 7 PASSWORD ATTACK LAB =====")
    print("LOCAL LAB SERVER ONLY")
    print("Server: http://127.0.0.1:5000")
    print("Username: admin")
    print("Rate limit: 5 attempts / 10 seconds")
    app.run(host="127.0.0.1", port=5000, debug=False)

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(
        message="Hello from Kubernetes CI/CD!",
        environment=os.getenv("APP_ENV", "unknown"),
        version=os.getenv("APP_VERSION", "dev"),
    )

@app.get("/healthz")
def health():
    return jsonify(status="healthy"), 200

@app.get("/readyz")
def ready():
    return jsonify(status="ready"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

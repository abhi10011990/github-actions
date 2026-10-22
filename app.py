
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)

# Adds Prometheus HTTP metrics and exposes /metrics
metrics = PrometheusMetrics(app)

APP_ENV = os.getenv("APP_ENV", "unknown")
APP_VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def home():
    return jsonify(
        message="Hello from Kubernetes CI/CD!",
        environment=APP_ENV,
        version=APP_VERSION,
    )


@app.get("/healthz")
def health():
    # Kubernetes uses this to check whether the app is alive
    return jsonify(status="healthy"), 200


@app.get("/readyz")
def ready():
    # Kubernetes uses this to check whether the app is ready
    return jsonify(status="ready"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

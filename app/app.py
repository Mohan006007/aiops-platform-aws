from flask import Flask, jsonify
import random
from prometheus_client import start_http_server, Gauge

app = Flask(__name__)

cpu_metric = Gauge('cpu_usage', 'Simulated CPU usage')

# 🔥 Health endpoint (for Kubernetes)
@app.route("/health")
def health():
    return "OK", 200

# 🔥 App endpoint
@app.route("/")
def home():
    value = random.randint(10, 95)
    cpu_metric.set(value)
    return jsonify({"cpu": value}), 200

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)

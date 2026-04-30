from flask import Flask
import random
from prometheus_client import start_http_server, Gauge

app = Flask(__name__)

cpu_metric = Gauge('cpu_usage', 'Simulated CPU usage')

@app.route("/")
def home():
    value = random.randint(10, 95)
    cpu_metric.set(value)
    return {"cpu": value}

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
import os
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

message = os.getenv("APP_MESSAGE", "ShopUA — deployed automatically!")

@app.route("/")
def hello():
    return {"message": message}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

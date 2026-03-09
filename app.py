import os
from flask import Flask

app = Flask(__name__)

message = os.getenv("APP_MESSAGE", "DevOps test")

@app.route("/")
def hello():
    return {"message": message}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

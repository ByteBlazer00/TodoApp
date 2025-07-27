from flask import Flask, request, render_template, redirect
from prometheus_metrics import setup_metrics
import logging
import json

app = Flask(__name__)
tasks = []

# Setup Prometheus metrics
setup_metrics(app)

# JSON Logging
log = logging.getLogger('todo')
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
))
log.addHandler(handler)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
            log.info(f"Task added: {task}")
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

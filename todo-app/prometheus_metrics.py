from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

task_counter = Counter("todo_tasks_total", "Total number of tasks added")

def setup_metrics(app):
    @app.before_request
    def before():
        if app.url_map.bind('').match(request.path)[0] == "index" and request.method == "POST":
            task_counter.inc()

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

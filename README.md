# TODO App with Prometheus Metrics

A simple Flask TODO app with:

- In-memory task storage
- Prometheus `/metrics` endpoint
- JSON logs for ELK stack

## Run Locally

```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app

from flask import Flask, jsonify, request

app = Flask(__name__)
__version__ = "1.0.0"
tasks = []


@app.route("/")
def home():
    return jsonify({"app": "Todo API", "status": "ok", "version": __version__})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/version")
def version():
    return jsonify({"version": __version__})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)

    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104

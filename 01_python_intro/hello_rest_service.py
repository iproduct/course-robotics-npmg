from flask import Flask, jsonify, make_response, abort

tasks = [
    {
        'id': 1,
        'title': 'Read W3Schools Python Tuotrial',
        'description': 'Go through all exercises at your own pace.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Try to create Flask Web Service',
        'description': 'Read and do exercises from Flask REST tutorial: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask',
        'done': False
    }
]

app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hello from REST Service!"

@app.route("/api/tasks", methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@app.route("/api/tasks/<int:task_id>", methods=['GET'])
def get_task_by_id(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify(task[0])


if __name__ == '__main__':
    app.run(debug=True)
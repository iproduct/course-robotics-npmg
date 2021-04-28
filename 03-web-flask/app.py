from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    {
        "id": 1,
        "title": "Read W3Schools JavaScript tutorial",
        "description": "Go through all exercises in your own pace",
        "done": False
    },
    {
        "id": 2,
        "title": "Create Flask web service",
        "description": "Create REST API for TODOs with Python and Flask",
        "done": False
    }
]


@app.route('/')
def hello_world():
    return 'Hello Python World!'

@app.route('/api/todos')
def get_todos():
    return jsonify(todos);


if __name__ == '__main__':
    app.run()

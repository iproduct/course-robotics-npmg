import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
commands = [
    {'id': 1,
     'command': 'FORWARD',
     'distance': '100',
    },
    {'id': 2,
     'command': 'TURN_LEFT',
     'degree': '90',
    },
    {'id': 3,
     'command': 'BACKWORD',
     'distance': '500',
    },
    {'id': 4,
     'command': 'TURN_RIGHT',
     'degree': '180',
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Simple Robot REST API</h1><p>This site is a prototype API for controlling yor ESP 32 robot.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/commands/', methods=['GET'])
def api_all():
    return jsonify(commands)


if __name__ == '__main__':
    app.run(host="192.168.43.143", port=5000)


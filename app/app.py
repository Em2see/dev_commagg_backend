from flask import Flask, jsonify
import json


FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.json')


app = Flask(__name__)


@app.route('/'):
def index():
    with open(FILE_PATH, 'r') as fp:
        data = json.dump(fp)
        
    return jsonify(data)


if __name__ == "__main__":
    app.run()
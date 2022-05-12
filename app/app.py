from flask import Flask, jsonify
import json
import os


FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.json')


app = Flask(__name__)

@app.route('/')
@app.route('/remarks')
def index():
    with open(FILE_PATH, 'r') as fp:
        data = json.load(fp)
        
    return jsonify(data)


if __name__ == "__main__":
    app.run()

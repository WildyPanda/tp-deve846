from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    json_file_path = os.path.join(app.root_path, 'logs_large.json')
    return send_file(json_file_path, mimetype='application/json')

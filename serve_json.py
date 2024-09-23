# app.py
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用CORS

@app.route('/get-json-machine')
def get_json1():
    return send_from_directory('.', 'machine.json', as_attachment=True)

@app.route('/get-json-resource')
def get_json2():
    return send_from_directory('.', 'resource.json', as_attachment=True)

@app.route('/get-json-machine-study')
def get_json3():
    return send_from_directory('.', 'machine_study.json', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

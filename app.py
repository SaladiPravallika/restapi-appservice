from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "API is running", "try": "/api/hello"})

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Azure!"})

if __name__ == '__main__':
    app.run()

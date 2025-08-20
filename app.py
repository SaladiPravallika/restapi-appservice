from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Azure!"})

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get/<param>', methods=['GET'])
def get(param):
    return jsonify({"message": f"This is a GET endpoint. Parameter: {param}"})

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    print(data.items())
    param1 = data.get('id')
    param2 = data.get('count')
    param3 = data.get('state')
    print(param1)
    return jsonify({"message": f"Received data: {param1}, {param2}, {param3}"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')

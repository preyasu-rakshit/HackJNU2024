from flask import Flask, request, jsonify
import time
from datetime import datetime
import pytz

dummytime = True
ist = pytz.timezone('Asia/Kolkata')

app = Flask(__name__)

for i in range(1, 7):
    with open(f'data\{i}.csv', 'w') as f:
        f.write('count, temp, state, time\n')

@app.route('/get/<id>', methods=['GET'])
def get(id):
    return jsonify({"message": f"This is a GET endpoint. ID: {id}"})

epoch = time.time()
@app.route('/post', methods=['POST'])
def post():
    global epoch
    data = request.get_json() 
    id = data.get('id')
    count = data.get('count')
    temp = data.get('temp')
    state = data.get('state')

    if not dummytime:
        with open(f'data/{id}.csv', 'a') as f:
            f.write(f'{count}, {temp}, {state}, {datetime.now().strftime("%H")}\n')
    else:
        epoch += 300
        with open(f'data/{id}.csv', 'a') as f:
            f.write(f'{count}, {temp}, {state}, {datetime.fromtimestamp(epoch, ist).strftime("%H")}\n')
    return jsonify({"message": f"Received data: {id}, {count}, {temp}, {state}"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')

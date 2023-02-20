from flask import Flask, request, jsonify
import datetime
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'

@app.route('/')
def index():
    return "Test message. The server is running"

@app.route('/time')
def current_time():
    now = datetime.datetime.now()
    return {'time': now}

@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400

    return jsonify({'result': num + 1})

with open('models/model.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    features = np.array(features).reshape(1, 4) 
    prediction =  model.predict(features)
    return  jsonify({'prediction': prediction[0]})  

if __name__ == '__main__':
    #app.run('localhost', 4999)
    app.run(host='0.0.0.0', port=4999) # для тестирования сервера необходимо пользоваться широковещательным адресом (0.0.0.0) 
    


from asyncio import tasks
from distutils.log import debug
import json
from tkinter.messagebox import YES
from flask import Flask,jsonify,request
app = Flask(__name__)

alldata = [
    {
        'id' : 1,
        'name': 'yes',
        'contact': 'yes',
        'done': False
    },
    {
        'id': 2,
        'name': 'no',
        'contact': 'no',
        'done': False
    }
]
@app.route('/')
def save_yes():
    return 'saved yes?'

@app.route('/add-data', methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'where number'
        },400)

    data = {
        'id': data[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact',''),
        'done': False
    }
    alldata.append(data)
    return jsonify({
        'status': 'success',
        'message': 'yess?'
    })

@app.route('/get-data')
def get_task(): 
    return jsonify({
        'data': alldata
    })

if (__name__ == '__main__'):
    app.run(debug=True)
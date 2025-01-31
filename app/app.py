from flask import Flask, jsonify, request, render_template
from os import environ
import database

app = Flask(__name__)

database.create_table()
@app.route('/insert' , methods=['GET'])
def insert():
    name = request.args.get('name')
    age = request.args.get('age')
    database.insert_data(name, age)
    return jsonify({'message' : "successfully"})

@app.route('/update' , methods=['GET'])
def update():
    _id = request.args.get('_id')
    name = request.args.get('name')
    age = request.args.get('age')
    database.update_data(_id,name,age)
    return jsonify({'message' : "success"})

@app.route('/find' , methods=['GET'])
def find():
    _id = request.args.get('_id')
    jsonData = database.get_data(_id)
    return jsonify(jsonData)

@app.route('/list', methods=['GET'])
def list():
    jsonData = database.list_data()
    return jsonify(jsonData)

@app.route('/delete' , methods=['GET'])
def delete():
    _id = request.args.get('_id')
    database.delete_data(_id)
    return jsonify({'message' : "success"})


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/congrats")
def showCongrats():
    return render_template('congrats.html')
@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)

@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        num1 = eval(num1)  # Use eval carefully; replace with a safer alternative in real apps
        num2 = int(num2)

        results = {
                'plus': num1 + num2,
                'minus': num1 - num2,
                'multiply': num1 * num2,
                'divide': num1 / num2
            }
    except:
        results = {'error_msg': 'inputs must be numbers'}

    return jsonify(results)

if __name__ == '__main__':
    app.run()

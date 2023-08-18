from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    first = request.json['first']
    second = request.json['second']
    # return a json response that stores the answer in a result key
    return {'result': first + second}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = request.json['first']
    second = request.json['second']
    return {'result': first - second}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

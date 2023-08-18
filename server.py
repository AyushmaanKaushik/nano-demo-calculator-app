from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    return str(request.json['first'] + request.json['second'])

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return str(request.json['first'] - request.json['second'])

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

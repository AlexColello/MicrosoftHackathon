from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello():
    return "Hello, World!!"


@app.route("/sms")
def sendTextToOwner():

    return "possibly just sent a text"

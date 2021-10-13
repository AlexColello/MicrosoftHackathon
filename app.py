from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hi hi'

@app.route("/test-post/", methods = ['POST'])
def returnMessage():
    return request.json

@app.route("/test-post/<msg>", methods = ['POST'])
def returnMessageTest(msg):
    return msg
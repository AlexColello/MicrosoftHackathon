from flask import Flask, request
app = Flask(__name__)

# this file is local on Anj's computer
with open("../barkAlert_twilio_secret.txt", "r") as f:
    TWILIO_SECRET = f.readlines()

TWILIO_ACCOUNT_SID = os.environ["SK387d5a95afb47ad5c1543859bc648216"]
TWILIO_AUTH_TOKEN = os.environ[TWILIO_SECRET]
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route('/',methods = ['POST', 'GET'])
def hello():
    return 'Hi hi'

@app.route("/test-post/", methods = ['POST'])
def returnMessage():
    return request.json

@app.route("/test-post/<msg>", methods = ['POST'])
def returnMessageTest(msg):
    return msg

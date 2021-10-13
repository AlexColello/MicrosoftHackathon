from flask import Flask
from flask import request

app = Flask(__name__)

# this file is local on Anj's computer
with open("../barkAlert_twilio_secret.txt", "r") as f:
    TWILIO_SECRET = f.readlines()

TWILIO_ACCOUNT_SID = os.environ["SK387d5a95afb47ad5c1543859bc648216"]
TWILIO_AUTH_TOKEN = os.environ[TWILIO_SECRET]
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route('/',methods = ['POST', 'GET'])
def hello():
    return "Hello, World!!"


@app.route("/sms")
def sendTextToOwner():

    return "possibly just sent a text"

@app.route('/fetch')
def fetch_sms():
    return twilio_api.messages.stream()

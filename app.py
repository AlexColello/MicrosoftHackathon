from flask import Flask, request, render_template
from dotenv import load_dotenv
import twilio1

load_dotenv()
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

    # return 'Hi hi'

@app.route("/test-post/", methods = ['POST'])
def returnMessage():
    sms_send_result = twilio1.send_sms("Hello! Your loved one needs your help!", anjali)
    call_result = twilio1.make_call("Hello! Your loved one's service dog needs your attention! Please check in on them! Also, milky toes has very milky toes.", anjali)

    return request.json

@app.route("/test-post/<msg>", methods = ['GET'])
def returnMessageTest(msg):
    return msg

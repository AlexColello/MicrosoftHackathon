from flask import Flask, request, render_template
# from twilio1 import fetch_sms
from dotenv import load_dotenv
# import twilio1
from database import get_db
import os

load_dotenv()
app = Flask(__name__, template_folder='./')

@app.route('/')
def hello():
    # sms=fetch_sms()
    # return render_template("index.html", sms=sms)

    return 'Hi hi'

@app.route("/test-post/", methods = ['POST'])
def returnMessage():
    # sms_send_result = twilio1.send_sms("Hello! Your loved one needs your help!", anjali)
    # call_result = twilio1.make_call("Hello! Your loved one's service dog needs your attention! Please check in on them! Also, milky toes has very milky toes.", anjali)

    return request.json

@app.route("/test-post/<msg>", methods = ['POST'])
def returnMessageTest(msg):
    return msg

@app.route('/test-database',methods = ['POST', 'GET'])
def testDatabase():
    load_dotenv() 
    print(os.environ)
    db = get_db()
    cursor = db.cursor()

    for row in cursor.tables():
        if row.table_type == "TABLE":
            print (row.table_name)
            print (row)

    cursor.execute("SELECT * FROM dbo.Customers")

    for row in cursor.fetchall():
        print(row)
    return 'yay'
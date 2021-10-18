from flask import Flask, request, render_template
# from twilio1 import fetch_sms
from dotenv import load_dotenv
import twilio_api
from database import get_db, reset_database, print_table, get_device_user
import database as db
import os

load_dotenv()
app = Flask(__name__, template_folder='./')

@app.route('/')
def hello():
    # sms=fetch_sms()
    # return render_template("index.html", sms=sms)
    return render_template("templates/index.html")

@app.route("/dashboard.html", methods = ['POST', 'GET'])
def dashboard():
    # sms=fetch_sms()
    # return render_template("index.html", sms=sms)
    return render_template("templates/dashboard.html")

@app.route("/alert", methods = ['POST'])
def recieveAlert():
    # sms_send_result = twilio1.send_sms("Hello! Your loved one needs your help!", anjali)
    # call_result = twilio1.make_call("Hello! Your loved one's service dog needs your attention! Please check in on them! Also, milky toes has very milky toes.", anjali)
    json = request.json
    print("Recieved: " + str(json))

    deviceID = json['deviceID']
    numButtons = int(json['numButtons'])

    userID = db.get_device_user(deviceID)
    contacts = db.get_contacts(userID)

    if numButtons >= 2:
        for contact in contacts:
            if contact[2]:
                twilio_api.make_call("Hello! Your loved one's service dog is trying to get your attention! Please check in on them!", contact[0])
    if numButtons >= 1:
        for contact in contacts:
            if contact[1]:
                twilio_api.send_sms("Hello! Your loved one's service dog is trying to get your attention!", contact[0])

    return "Recieved alert from {} for {} buttons.".format(json['deviceID'], json['numButtons'])

@app.route("/insert-ice", methods = ['POST', 'GET'])
def updateDb():
    db = get_db()
    print('in insert_ice!')
    return render_template("templates/dashboard.html")


@app.route('/test-database',methods = ['POST', 'GET'])
def testDatabase():
    db = get_db()
    cursor = db.cursor()

    for row in cursor.tables():
        if row.table_type == "TABLE" and row.table_schem == "dbo":
            print (row.table_name)
            print([column[0] for column in cursor.description])
            print (row)

    cursor.execute("SELECT * FROM dbo.Customers")

    for row in cursor.fetchall():
        print(row)
    return 'yay'

@app.route('/reset-database',methods = ['POST', 'GET'])
def resetDatabase():

    reset_database()
    print_table('dbo.Contacts')
    print(db.get_contacts(1))
    print_table('dbo.Devices')
    print(get_device_user('3fxdKhjgIy04'))

    get_db().commit()
    return 'yay!'


@app.route('/print-database',methods = ['POST', 'GET'])
def printDatabase():

    print_table("dbo.Users")

    return 'yay!!'
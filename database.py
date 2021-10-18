import pyodbc
import os, sys
from flask import g

def get_db():
    if 'db' not in g:
        g.db = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};\
            Server=' + os.environ['DATABASE_SERVER'] + ';\
            Database=' + os.environ['DATABASE_ID'] + ';\
            Uid=' + os.environ['DATABASE_USER_ID'] + ';\
            Pwd=' + os.environ['DATABASE_PASSWORD'] + ';\
            Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def get_tables():
    db = get_db()
    cursor = db.cursor()

    table_names = []
    for row in cursor.tables():
        if row.table_type == "TABLE" and row.table_schem == "dbo":
            table_names.append(row.table_name)

    return table_names

# Drop every table, reinitialize them, and fill them with sample data
def reset_database():
    table_names = get_tables()
    for table in table_names:
        drop_table("dbo." + table)

    create_tables()
    insert_sample_data()

    print_table("dbo.Users")

# Drop table
def drop_table(name):
    db = get_db()
    cursor = db.cursor()

    print('Droping table "{}"'.format(name), file=sys.stdout)

    cursor.execute("DROP TABLE " + name)

def create_tables():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE dbo.Users
        (
        UserID       INT    IDENTITY(1,1)  PRIMARY KEY,
        FirstName    [NVARCHAR](50)  NOT NULL,
        LastName     [NVARCHAR](50)  NOT NULL,
        Email        [NVARCHAR](50)  NOT NULL,
        PhoneNumber  [NVARCHAR](50)  NOT NULL,
        Password     [NVARCHAR](50)  NOT NULL
        )"""
        )
    cursor.execute("""CREATE TABLE dbo.Contacts
        (
        UserID       INT    FOREIGN KEY REFERENCES dbo.Users(UserID),
        PhoneNumber  [NVARCHAR](50)  NOT NULL,
        SendText     BIT  NOT NULL,
        CallPhone    BIT  NOT NULL
        )"""
        )
    cursor.execute("""CREATE TABLE dbo.Devices
        (
        DeviceID    [NVARCHAR](50)  NOT NULL   PRIMARY KEY,
        UserID       INT    FOREIGN KEY REFERENCES dbo.Users(UserID),
        )
        """)

def insert_sample_data():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""INSERT INTO dbo.Users
        (FirstName,LastName,Email,PhoneNumber,Password)
        VALUES
        ( N'Orlando', N'Australia', N'cgxfgxggxffgxxfgfx', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( N'Keith', N'India', N'keith0@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( N'Donna', N'Germany', N'donna0@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( N'Janet', N'United States', N'janet1@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com')
        """)

    insert_user('Tommy', 'Trojan', 'ttrojan@usc.edu', '+13678992256', 'FightOn')

    insert_device("3fxdKhjgIy04", 1)
    insert_contact(1, "+18585272410", 0, 1)
    insert_contact(1, "+13853369470", 1, 0)

def insert_user(firstname, lastname, email, phonenumber, password):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""INSERT INTO dbo.Users
        (FirstName,LastName,Email,PhoneNumber,Password)
        VALUES (?, ?, ?, ?, ?)""",
        firstname, lastname, email, phonenumber, password)

def insert_device(deviceID, userID):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO dbo.Devices
        (DeviceID,UserID)
        VALUES (?, ?)""",
        deviceID, userID)

def insert_contact(userID, phonenumber, send_text, call_phone):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO dbo.Contacts
        (UserID,PhoneNumber,SendText,CallPhone)
        VALUES (?, ?, ?, ?)""",
        userID, phonenumber, send_text, call_phone)

def get_user(userID):
    db = get_db()
    cursor = db.cursor()
    row  = cursor.execute("SELECT FirstName,LastName,Email,PhoneNumber FROM dbo.Users WHERE UserID=?", userID).fetchone()
    return row

def get_contacts(userID):
    db = get_db()
    cursor = db.cursor()
    rows = cursor.execute("SELECT * FROM dbo.Contacts WHERE UserID=?", userID).fetchall()
    return [(row.PhoneNumber, row.SendText, row.CallPhone) for row in rows]

def check_sign_in(email, password):
    db = get_db()
    cursor = db.cursor()
    count = cursor.execute("SELECT * FROM dbo.Users WHERE Email=?, Password=?", email, password).rowcount

    return count > 0

def get_device_user(deviceID):
    db = get_db()
    cursor = db.cursor()
    row = cursor.execute("SELECT (UserID) FROM dbo.Devices WHERE DeviceID=?", deviceID).fetchone()
    return row.UserID

def print_table(table):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM {}".format(table))

    print('Table {}:'.format(table))
    for row in cursor.fetchall():
        print(row, file=sys.stdout)
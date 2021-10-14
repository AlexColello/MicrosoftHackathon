import pyodbc
import os
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
        drop_table(table)

    create_tables()
    insert_sample_data()
    print_table("dbo.Users")

# Drop table
def drop_table(name):
    db = get_db()
    cursor = db.cursor()

    print('Droping table "{}"'.format(name))

    cursor.execute("DROP TABLE " + name)

def create_tables():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE dbo.Users
        (
        UserID       INT    NOT NULL   PRIMARY KEY,
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
        ContactId    INT    NOT NULL   PRIMARY KEY,
        UserID       INT    FOREIGN KEY REFERENCES dbo.Users(UserID),
        )
        """)

def insert_sample_data():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""INSERT INTO dbo.Users
        ([UserID],[FirstName],[LastName],[Email],[PhoneNumber],[Password])
        VALUES
        ( 1, N'Orlando', N'Australia', N'', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( 2, N'Keith', N'India', N'keith0@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( 3, N'Donna', N'Germany', N'donna0@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com'),
        ( 4, N'Janet', N'United States', N'janet1@adventure-works.com', N'keith0@adventure-works.com', N'keith0@adventure-works.com')
        """)

def insert_user(name):
    pass

def insert_device(id, name):
    pass

def insert_contact(number):
    pass

def get_user():
    return ('Tommy', 'Trojan')

def get_contacts(user):
    return [('1234567890', True, False)]

def print_table(table):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM {}".format(table))

    for row in cursor.fetchall():
        print(row)
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

# Drop every table, reinitialize them, and fill them with sample data
def reset_database():
    pass

# Drop and reinitialize each table
def clear_tables():
    pass

def insert_sample_data():
    pass

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
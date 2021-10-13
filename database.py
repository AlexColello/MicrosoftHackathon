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
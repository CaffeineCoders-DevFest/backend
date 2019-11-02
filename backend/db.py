import sqlite3
from flask import g
from .app import app


DATABASE = './database.sqlite3'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    with open('create_tables.sql') as f:
        c = db.cursor()
        c.executescript(f.read())
    return db


@app.teardown_appcontext
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

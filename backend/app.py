from flask_api import FlaskAPI
import sqlite3
from flask import g

app = FlaskAPI(__name__)


DATABASE = './database.sqlite3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/api/technician')
def technician():
    return query_db('SELECT techID, locationZip, techTypeID, rating, contactNumber FROM Tech')


@app.route('/api/skill')
def skills():
    return {}

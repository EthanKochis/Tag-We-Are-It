from flask import Flask
from flask_cors import CORS
import json
import psycopg2
from config import config

app = Flask(__name__)
CORS(app)

cur=None
conn=None

def connect():
    global cur
    global conn

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % params['database'])
        conn = psycopg2.connect(**params)
        print('Connected.\n')

        # create a cursor
        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def close_connection():
    try:
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('\nDatabase connection closed.')



@app.route('/tag_categories')
def tag_categories():
  if conn is None:
    connect()
  cur.execute("SELECT Category_name FROM TAG_CATEGORY")
  return json.dumps(cur.fetchall())

@app.route('/tags/<category>')
def tags(category=None):
  if conn is None:
    connect()
  cur.execute(f"SELECT Tag_name FROM TAG WHERE Category_name='{category}'")
  return json.dumps(cur.fetchall())
  #return json.dumps(['ctag1' + category, 'ctag2' + category, 'ctag3' + category])

@app.route('/tags')
def all_tags():
  if conn is None:
    connect()
  cur.execute("SELECT Tag_name FROM TAG")
  return json.dumps(cur.fetchall())
  #return json.dumps(['tag1', 'tag2', 'tag3'])

@app.route('/articles/<tag>')
def articles(tag=None):
  if conn is None:
    connect()
  cur.execute(f"SELECT Title FROM ARTICLE NATURAL JOIN CLASSIFIED_AS WHERE Tag_name='{tag}'")
  return json.dumps(cur.fetchall())
  #return json.dumps(['tarticle1' + tag, 'tarticle2' + tag, 'tarticle3' + tag])

@app.route('/articles')
def all_articles():
  if conn is None:
    connect()
  cur.execute("SELECT Title from ARTICLE")
  return json.dumps(cur.fetchall())
  #return json.dumps(['article1', 'article2', 'article3'])
# 127.0.0.1:5000/tag_categories

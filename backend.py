from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/tag_categories')
def tag_categories():
  return json.dumps(['cat1', 'cat2', 'cat3'])

@app.route('/tags/<category>')
def tags(category=None):
  return json.dumps(['ctag1' + category, 'ctag2' + category, 'ctag3' + category])

@app.route('/tags')
def all_tags():
  return json.dumps(['tag1', 'tag2', 'tag3'])

@app.route('/articles/<tag>')
def articles(tag=None):
  return json.dumps(['tarticle1' + tag, 'tarticle2' + tag, 'tarticle3' + tag])

@app.route('/articles')
def all_articles():
  return json.dumps(['article1', 'article2', 'article3'])
# 127.0.0.1:5000/tag_categories

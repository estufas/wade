# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask import Flask, jsonify
import pdb
import json
import os 
from bson.objectid import ObjectId# import libraries
# import urllib2
import requests

from bs4 import BeautifulSoup

# local imports
from config import app_config
# client = pymongo.MongoClient("mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true")
# db = client.test
# db variable initialization
# db = SQLAlchemy()


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

def scrape_aa_meetings():
    page = requests.get('https://lacoaa.org/meetings/?tsml-day=any')
    soup = BeautifulSoup(page.text, 'html.parser')
    # meeting_table = soup.findAll('div',attrs={"class":"row"})
    # meetings = meeting_table.find_all('a')
    rows = soup.find_all('tr')
    for row in rows:          # Print all occurrences
        print(row)
    return rows


    rows = soup.find_all('tr')
    for row in rows:          # Print all occurrences
        print('help', row.get_text())



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true'] = os.environ.get('DB')
    mongo = PyMongo(app)

    @app.route('/meetings')
    def get_tasks():
        meetings = scrape_aa_meetings()
        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
        return "hello world"
        

    return app

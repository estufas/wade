# app/__init__.py

# third-party imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import pdb
# import libraries
# import urllib2
import requests
import json
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from bs4 import BeautifulSoup

# local imports
from config import app_config

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
    rows = soup.find_all('tr')
    # for row in rows:          # Print all occurrences
    #     print('help', row.get_text())
    print(len(rows))



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["MONGO_URI"] = "mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true"
    mongo = PyMongo(app)
    print(mongo)
    # db.init_app(app)

    @app.route('/meetings', methods=['GET'])
    def get_tasks():
        # print ('api')
        meetings = scrape_aa_meetings()
        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
        return 'Hello, Worrld!'

    return app

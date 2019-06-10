# app/__init__.py

# third-party imports
<<<<<<< HEAD
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
=======
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import pdb
import attr
# import libraries
# import urllib2
import requests
import json
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
>>>>>>> stuart

from bs4 import BeautifulSoup

# local imports
from config import app_config
<<<<<<< HEAD
# client = pymongo.MongoClient("mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true")
# db = client.test
# db variable initialization
# db = SQLAlchemy()


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
=======

# db variable initialization
# db = SQLAlchemy()

tasks = [
    {
        'id': 1,
        'title': u'Buy eeihepoihwetihgroceries',
>>>>>>> stuart
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
<<<<<<< HEAD
        'title': u'Learn Python',
=======
        'title': u'Learffdn Python',
>>>>>>> stuart
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
<<<<<<< HEAD
=======
@attr.s(slots=True, kw_only=True)
class TestObject(object):
    time = attr.ib()
    name = attr.ib()
    location = attr.ib()
    region = attr.ib()
    type = attr.ib()

big_list = []

>>>>>>> stuart

def scrape_aa_meetings():
    page = requests.get('https://lacoaa.org/meetings/?tsml-day=any')
    soup = BeautifulSoup(page.text, 'html.parser')
<<<<<<< HEAD
    # meeting_table = soup.findAll('div',attrs={"class":"row"})
    # meetings = meeting_table.find_all('a')
    rows = soup.find_all('tr')
    for row in rows:          # Print all occurrences
        print(row)
    return rows


    rows = soup.find_all('tr')
    for row in rows:          # Print all occurrences
        print('help', row.get_text())


=======
    rows = soup.find_all('tr')
    # for row in rows:          # Print all occurrences
    #     print('help', row.get_text())
    for idx,tr in rows:
        for td in tr:
            if td.find_all('span'):
                meeting_time = td.find_all('span')
                for item in meeting_time:
                    print(item.string)
            elif td.find('a'):
                print(idx,td.find('a').string)
            else:
                print(idx,td.string)
    return rows


>>>>>>> stuart

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
<<<<<<< HEAD
    app.config['mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true'] = os.environ.get('DB')
    mongo = PyMongo(app)

    @app.route('/meetings')
    def get_tasks():
        meetings = scrape_aa_meetings()
=======
    app.config["MONGO_URI"] = "mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true"
    mongo = PyMongo(app)
    print(mongo)
    # db.init_app(app)

    @app.route('/meetings')
    def get_tasks():
        # print ('api')
        meetings = scrape_aa_meetings()
        for idx,tr in enumerate(meetings[0:2]):
            for td in tr:
                if td.find_all('span'):
                    span_list = td.find_all('span')
                    for item in span_list:
                        print(item.string)
                elif td.find('a'):
                    print(idx,td.find('a').string)
                else:
                    print(idx,td.string)

>>>>>>> stuart
        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
<<<<<<< HEAD
        return "hello world"
        
=======
        return 'Hello, Worrld!'
>>>>>>> stuart

    return app

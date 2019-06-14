# app/__init__.py

# third-party imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import pdb
# import attr
# import libraries
# import urllib2
import requests
import json
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from bs4 import BeautifulSoup

# local imports
from config import DevelopmentConfig
from config import app_config

# db variable initialization
# db = SQLAlchemy()

tasks = [
    {
        'id': 1,
        'title': u'Buy eeihepoihwetihgroceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learffdn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# @attr.s(slots=True, kw_only=True)
# class TestObject(object):
#     time = attr.ib()
#     name = attr.ib()
#     location = attr.ib()
#     region = attr.ib()
#     type = attr.ib()


big_list = []


def scrape_aa_meetings():
    page = requests.get('https://lacoaa.org/meetings/?tsml-day=any')
    soup = BeautifulSoup(page.text, 'html.parser')
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



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["MONGO_URI"] = DevelopmentConfig.MONGO_URI
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

        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
        return 'Hello, Worrld!'

    return app

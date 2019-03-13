# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import pdb
# import libraries
# import urllib2
import requests

from bs4 import BeautifulSoup

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

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
    # print (meeting_table)

    # textContent = []
    # for i in range(0, 10):
    #     paragraphs = soup.find_all("a")[i].text
    #     textContent.append(paragraphs)

    # Take out the <div> of name and get its value
    # name_box = soup.select("td.name")
    # test = name_box.a


    # print ('ok')
    # print (textContent)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/meetings', methods=['GET'])
    def get_tasks():
        print ('api')
        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
        scrape_aa_meetings()
        return 'Hello, Worrld!'

    return app

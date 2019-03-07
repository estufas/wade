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

# Collect first page of artists’ list


# name = name_box.text.strip() # strip() is used to remove starting and trailing


# get the index price
# price_box = soup.find(‘div’, attrs={‘class’:’price’})
# price = price_box.text
# print price

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
    page = requests.get('https://lacoaa.org/meetings/?tsml-day=4&tsml-distance=5&tsml-mode=location&tsml-query=90042')

    # # query the website and return the html to the variable ‘page’
    # page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    pdb.set_trace()
    soup = BeautifulSoup(page.text, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find(id='meetings_tbody')
    test = soup.find_all('a')

    # print ('ok')
    print (test)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/meetings', methods=['GET'])
    def get_tasks():
        print ('api')
        scrape_aa_meetings()
        return jsonify({'tasks': tasks})

    @app.route('/')
    def hello_world():
        return 'Hello, Worrld!'

    return app

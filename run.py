import os
import pymongo
from app import create_app

config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)

client = pymongo.MongoClient("mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true")
db = client.test



if __name__ == '__main__':
    app.run()

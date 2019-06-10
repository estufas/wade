
import pdb
# import attr
# import libraries
# import urllib2
import requests
import json
from bson.objectid import ObjectId
import csv
import pandas as pd

# from flask_pymongo import PyMongo

from bs4 import BeautifulSoup

big_list = []

filename = "computerRank10.csv"
csv_writer = csv.writer(open(filename, 'w'))


def scrape_aa_meetings():
    page = requests.get('https://lacoaa.org/meetings/?tsml-day=any')
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('tr')
    # for row in rows:          # Print all occurrences
    #     print('help', row.get_t   ext())
    datas=[]
    for idx,tr in enumerate(rows):
        data=[]
        data.append(idx)
        for td in tr:
            if td.find_all('span'):
                meeting_time = td.find_all('span')
                for item in meeting_time:
                    # print(item.string)
                    data.append(item.string)
            elif td.find('a'):
                # print(idx,td.find('a').string)
                data.append(td.find('a').string)
            else:
                # print(idx,td.string)
                data.append(td.string)
        # print(data)
        datas.append(data)
        csv_writer.writerow(data)
    # print(datas[0])
    # datas[0].append('Notes')

    # columns = datas[0]

    # print(columns)
    # df = pd.DataFrame(datas[1:],columns=columns)
    # print(df.head()['Time'=='Tuesday'])
    return rows

print ("hello world")
scrape_aa_meetings()

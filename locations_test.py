from pymongo import MongoClient
import pprint
import json
import warnings
from flask import Flask
import os
warnings.filterwarnings('ignore')
app = Flask(__name__)


def get_database():
    CONNECTION_STRING = "mongodb+srv://BerserkBobi:basedgod001@berserkcluster.khnwedq.mongodb.net/7"
    client = MongoClient('CONNECTION_STRING')
    return client['locations']





if __name__ == "__main__":
    locations = get_database()
    



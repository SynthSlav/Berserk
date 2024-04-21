import os
import json
from pymongo.mongo_client import MongoClient
from flask import Flask, render_template, request, url_for, redirect, session, current_app, g
import bson
from flask_pymongo import PyMongo
import pymongo
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)

uri = "mongodb+srv://BerserkBobi:basedgod001@berserkcluster.khnwedq.mongodb.net/"
# Create a new client and connect to the server
client = pymongo.MongoClient('mongodb://localhost:27017')
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(client.list_database_names())

db = client.get_database['area']
area_db = db.area
print(list(area_db))


objects_collection = db.get_collection('objects')

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db


@app.route("/")
def index():
    return render_template("index.html", page_title="Welcome weary wanderer")


@app.route("/universe")
def universe():
    return render_template("universe.html", page_title = "Universe")


@app.route("/locations")
def locations():
    
    return render_template("locations.html", page_title = "Locations in Berserk", locations = area)


@app.route("/characters")
def characters():
    data = []
    with open("characters.json", "r", encoding='utf8') as json_data:
        data = json.load(json_data)
    return render_template("characters.html", page_title = "Characters of Berserk", characters=data)


@app.route("/characters/<character_name>")
def characters_character(character_name):
    character = {}
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == character_name:
                character = obj
    return render_template("characters.html", character=character)


@app.route("/objects")
def objects():
    obj_data = []
    f = open('obj.json', encoding='utf8')
    obj_data = json.load(f)
    return render_template("objects.html", page_title = "Notable objects in Berserk", objects = obj_data)


@app.route("/timelines")
def timelines():
    return render_template("timelines.html", page_title = "Timelines in the Berserk lore")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


def objects_coll():

    return ('objects.html')




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=os.environ.get("PORT", "3000"),
        debug=True)



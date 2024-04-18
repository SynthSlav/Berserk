import os
import json
from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", page_title="Welcome weary wanderer")


@app.route("/universe")
def universe():
    return render_template("universe.html", page_title = "Universe")


@app.route("/locations")
def locations():
    return render_template("locations.html", page_title = "Locations in Berserk")


@app.route("/characters")
def characters():
    data = []
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("characters.html", page_title = "Characters of Berserk", character=data)


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
    return render_template("objects.html", page_title = "Notable objects in Berserk")


@app.route("/timelines")
def timelines():
    return render_template("timelines.html", page_title = "Timelines in the Berserk lore")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")






if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=os.environ.get("PORT", "3000"),
        debug=True)



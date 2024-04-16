import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/universe")
def universe():
    return render_template("universe.html")

@app.route("/locations")
def locations():
    return render_template("locations.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/objects")
def objects():
    return render_template("objects.html")

@app.route("/timelines")
def timelines():
    return render_template("timelines.html")


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
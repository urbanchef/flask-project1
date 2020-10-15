import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/departures/<departure>/")
def departures(departure):
    return render_template('departure.html')


@app.route("/tours/<id>/")
def tours(id):
    return render_template("tour.html")


app.run()



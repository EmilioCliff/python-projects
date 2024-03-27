from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask_bootstrap import Bootstrap5
import csv

class MyForm(FlaskForm):
    cafe = StringField(label="cafe_name", validators=[validators.DataRequired()])
    location = StringField(label="location", validators=[validators.DataRequired(), validators.URL()])
    open = StringField(label="opening_hours", validators=[validators.DataRequired()])
    close = StringField(label="closing_hours", validators=[validators.DataRequired()])
    coffee =
    wifi =
    power =
app = Flask(__name__)
app.secret_key = "SuckMyDick"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", "r") as data:
        my_data = csv.reader(data)
        cafe_data = []
        for row in my_data:
            cafe_data.append(row)
    return render_template("cafes.html", cafes=cafe_data)


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

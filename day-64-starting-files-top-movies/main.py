from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

movie_api = "9f31ae79bebf825bea88d71bd30bd9e7"
token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZjMxYWU3OWJlYmY4MjViZWE4OGQ3MWJkMzBiZDllNyIsInN1YiI6IjY1M2NhMGU0ZTg5NGE2MDBmZjE2Njk1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.znqqSZZHs0odU54vrnI7xBMzCsFY-coYN2oNIho40Z8"
movie_end_url = "https://api.themoviedb.org/3/search/movie"
image_url = "https://image.tmdb.org/t/p/w500"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movies.db"
db = SQLAlchemy()
db.init_app(app)


class RateMovieForm(FlaskForm):
    rating = StringField(label="Rating", validators=[DataRequired()])
    review = StringField(label="Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True, default=0.0)
    ranking = db.Column(db.Integer, nullable=True, default=0)
    review = db.Column(db.String(250), nullable=True, default='None')
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movie_list = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movie_list)):
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    return render_template("index.html", movies=movie_list)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("my_movie_id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        parameter = {"api-key": movie_api, "query": movie_title}
        response = requests.get(url=movie_end_url, params=parameter, headers=headers).json()
        print(response)
        return render_template("select.html", response=response['results'])
    return render_template("add.html", form=form)


@app.route("/search")
def search():
    movie_id = request.args.get("movie_id")
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params={"api-key": movie_api},
                            headers=headers).json()
    movie = Movie(
        title=response['original_title'],
        year=int(response['release_date'].split("-")[0]),
        description=response['overview'],
        img_url=f"{image_url}/{response['poster_path']}"
    )
    db.session.add(movie)
    db.session.commit()
    m_id = movie.id
    # the_movie_added = db.session.execute(db.Select(Movie).where(Movie.title == response['original_title'])).scalar()
    return redirect(url_for("edit", my_movie_id=m_id))


if __name__ == '__main__':
    app.run(debug=True)

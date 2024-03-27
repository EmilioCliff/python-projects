from flask import Flask, render_template
import datetime
# import random
import requests

genderize_url = "https://api.genderize.io"
agify_url = "https://api.agify.io"

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    # random_number = random.randint(0,20)
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=genderize_url, params={"name": name})
    age_response = requests.get(url=agify_url, params={"name": name})
    # print(response.text)
    gender = gender_response.json()['gender']
    age = age_response.json()['age']
    return render_template("guess.html", age=age, gender=gender, name=name)

@app.route("/blog")
def blog():
    response = requests.get(url="https://api.npoint.io/a1cc1e1fbaded969ec7a")
    response.raise_for_status()
    print(response.text)
    blogs = response.json()
    return render_template("blog.html", all_blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)


# import random
#
# app = Flask(__name__)
# random_number = random.randint(0, 9)
#
#
# @app.route("/")
# def home():
#     return ('<h><b>Guess a number from 0 to 9</b><h>'
#             '</br>'
#             '<img src="https://media2.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif?cid=ecf05e479qk5z7tohq9zb1qy2jjjqma5xbjafxemjt2vbqpf&ep=v1_gifs_search&rid=giphy.gif&ct=g">')
#
#
# @app.route("/<int:number>")
# def guess_number(number):
#     # print(random_number)
#     if number == random_number:
#         return ('<h style="color: green">You Got It!!</h>'
#                 '</br>'
#                 '<img src="https://media4.giphy.com/media/RpizrZcLTdlVFjZFFP/200w.webp?cid=ecf05e4702qtp0pj0ucd82yptyid6cd95e07c9p27q10q6v1&ep=v1_gifs_search&rid=200w.webp&ct=g">')
#     elif number < random_number:
#         return ('<h style="color: red">Too low, Try Again</h>'
#                 '</br>'
#                 '<img src="https://media0.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/200w.webp?cid=ecf05e474ybd7l03cl1elbs38ct4lzikgwv84dodb0ogba8k&ep=v1_gifs_search&rid=200w.webp&ct=g">')
#     else:
#         return ('<h style="color: purple">Too high, Try Again</h>'
#                 '</br>'
#                 '<img src="https://media3.giphy.com/media/2cei8MJiL2OWga5XoC/200w.webp?cid=ecf05e47i56t4jm93lojg1129guhiz86reb27axspgzp1e6q&ep=v1_gifs_search&rid=200w.webp&ct=g">')
# if __name__ == "__main__":
#     app.run(debug=True)

# app = Flask(__name__)
#
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
#
# def make_italic(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def underline(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper
#
#
# @app.route("/")
# @make_bold
# @make_italic
# @underline
# def hello():
#     return "Hello world"
#
#
# @app.route("/bye/<name>")
# def bye(name):
#     return f"Goodbye {name}"
#
# if __name__ == "__main__":
#     app.run(debug=True)

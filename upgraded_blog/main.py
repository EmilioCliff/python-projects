import smtplib
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
my_url = "https://api.npoint.io/d057f6ea528500eb7c16"
response = requests.get(url=my_url)
# print(response.text)
all_posts = response.json()
my_posts = []
for post in all_posts:
    my_posts.append(post)

# print(my_posts)

@app.route("/")
def home():
    return render_template("index.html", all=my_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        number = request.form['phone']
        message = request.form['message']
        print(name, email, number, message)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login("clifftest33@gmail.com", "mjavshcnnjalrzro")
            connection.sendmail(
                from_addr="clifftest33@gmail.com",
                to_addrs="emiliocliff@gmail.com",
                msg=f"{name} response\n\n Name: {name}\nEmail: {email}\nNumber: {number}\nMessage: {message}"
            )
        return f"<h1> Name: {name}\nEmail: {email}\nPhone Number: {number}\nMessage: {message}</h1>"
    return render_template("test.html")

@app.route("/post/<int:id>")
def post(id):
    requested_post = None
    for ipost in my_posts:
        if ipost['id'] == id:
            requested_post = ipost
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

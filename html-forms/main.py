from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def form():
    email = request.form['email']
    password = request.form['password']
    return render_template("response.html", email=email, password=password)

if __name__ == "__main__":
    app.run(debug=True)

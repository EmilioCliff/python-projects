from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    password = PasswordField(label='Password', validators=[validators.DataRequired(), validators.Length(min=8, message=("field must be at least 8 characters long"))])
    email = StringField(label='Email', validators=[validators.DataRequired(), validators.Email()])
    submit = SubmitField(label='Submit')


app = Flask(__name__)


app.secret_key = "SuckMyDick"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
?ExB4x1zO.
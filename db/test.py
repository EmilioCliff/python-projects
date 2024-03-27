from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_list.db"
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    name = db.Column(db.String(250), nullable=False, primary_key=True)
    email = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

with app.app_context():
    user = User(name="cliff", email="emiliocliff@gmail.com")
    db.session.add(user)
    db.session.commit()
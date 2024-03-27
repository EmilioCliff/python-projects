# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# # Create The Database
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# # Create extension
# db = SQLAlchemy()
# # Initialize the app with extension
# db.init_app(app)
#
#
# # Create Table
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#
# # Create Table Schema in the database
# with app.app_context():
#     db.create_all()
# # Insert data
# with app.app_context():
#     new_book = Book(id=1, title='Atomic Habits', author='Keith', rating='9.3')
#     db.session.add(new_book)
#     db.session.commit()
# import sqlite3
#
# db = sqlite3.connect("books.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Atomic Habits', 'Keith', '9.3')")
# db.commit()

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


class MyForm(FlaskForm):
    post_title = StringField(label="Blog Title", validators=[DataRequired()])
    post_subtitle = StringField(label="Blog Subtitle", validators=[DataRequired()])
    authors_name = StringField(label="Author's Name", validators=[DataRequired()])
    background_img = StringField(label="Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Body Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit")



# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # def to_dict(self):
    #     return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    my_post = db.session.execute(db.select(BlogPost))
    posts = my_post.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    form = MyForm()
    if form.is_submitted():
        blog = BlogPost(
            title=form.post_title.data,
            subtitle=form.post_subtitle.data,
            date=datetime.now().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.authors_name.data,
            img_url=form.background_img.data
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, action="create")

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = MyForm(
        post_title=post.title,
        post_subtitle=post.subtitle,
        authors_name=post.author,
        background_img=post.img_url,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.post_title.data
        post.subtitle = form.post_subtitle.data
        post.author = form.authors_name.data
        post.img_url = form.background_img.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template("make-post.html", action="edit", post=post, form=form)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=['DELETE', 'GET', 'POST'])
def delete(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

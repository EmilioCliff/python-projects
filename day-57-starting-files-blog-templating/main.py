from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
blogs = response.json()
my_blogs = []
for blog in blogs:
    post = Post(blog['id'], blog['title'], blog['subtitle'], blog['body'])
    my_blogs.append(post)

@app.route('/')
def home():
    return render_template("index.html", all_blogs=my_blogs)


@app.route('/post/<int:post_id>')
def post(post_id):
    the_blog = None
    for check_blog in my_blogs:
        if check_blog.id == post_id:
            the_blog = check_blog
    return render_template("post.html", requested_blog=the_blog)



if __name__ == "__main__":
    app.run(debug=True)

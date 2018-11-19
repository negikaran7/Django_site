from flask import Flask, render_template,url_for
app = Flask(__name__)


posts = [
    {
        'author': "karan",
        "title": "blog post 1",
        "date_posted": "Nov 19, 2018",
        "content":"hello there! it's my first post"
    },
    {
        'author': "karan",
        "title": "blog post 1",
        "date_posted": "Nov 19, 2018",
        "content":"hello there! it's my second post "
    }
]


@app.route("/")
def hello():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title="about")


if __name__ == '__main__':
    app.run(debug=True)

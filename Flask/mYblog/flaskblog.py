from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>your homepage</h1>"


@app.route("/about")
def about():
    return "<h2>this is about page</h2>"

if __name__=='__main__':
    app.run(debug=True)
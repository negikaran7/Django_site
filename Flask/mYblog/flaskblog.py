from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='1d8700f8a3a5e0575ed1c5a7b802981'

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
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title="about")


@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)

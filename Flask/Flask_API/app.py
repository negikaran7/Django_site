from model import db
from flask import Flask, jsonify, request, render_template,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import User
from sqlalchemy.orm import sessionmaker
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://###########@localhost/newdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

conn = psycopg2.connect(database="newdatabase", user="########",
                        password="#########", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)


@app.route('/')
def homepage():
    return jsonify({"message": "Homepage"})

# GET all data


@app.route('/show_data', methods=['GET'])
def showdata():
    usr = User.query.all()
    data = []
    for i in usr:
        details = {
            "name": i.username,
            "password": i.password,
            "email": i.email
        }
        data.append(details)

    return jsonify(data)


# GET all data  by email
@app.route('/show_user/<email>', methods=['GET'])
def showuser(email):
    try:
        usr = User.query.filter_by(email=email).first()
        details = {
            "name": usr.username,
            "password": usr.password,
            "email": usr.email
        }
    except:
        return jsonify({"message": "all gone"})
    return jsonify(details)

# POST add data
@app.route('/add_data', methods=['POST'])
def adddata():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        usr = User(username=username, password=password, email=email)
        db.session.add(usr)
        db.session.commit()

    except:
        return jsonify({"message": "duplicate data"})

    return jsonify({"message": "data added"})

# POST update data


@app.route('/update_data/<email>', methods=['POST'])
def updatedata(email):
    update_details = User.query.filter_by(email=email).first()
    try:
        update_details.username = request.form['username']
        update_details.email = request.form['email']
        update_details.password = request.form['password']
        db.session.commit()

    except:
        return jsonify({"message": "email already exist"})
    return jsonify({"message": "updated"})

# POST delete data


@app.route('/delete_data/<email>', methods=['POST'])
def deletedata(email):
    try:

        delete_details = User.query.filter_by(email=email).first()
        db.session.delete(delete_details)
        db.session.commit()

    except:
        return jsonify({"message": "Data not exist"})

    return jsonify({"message": "deleted"})


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

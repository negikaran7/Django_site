from model import db
from flask import Flask,jsonify,request,render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import User
from sqlalchemy.orm import sessionmaker
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://optimus:Optimus@7#@localhost/newdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

conn = psycopg2.connect(database = "newdatabase", user = "optimus", password = "Optimus@7#", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()

@app.route('/')
def test():
    return "<h1>API Homepage</h1>"

#GET all data
@app.route('/show_data', methods=['GET'])
def showdata():
    usr=User.query.all()
    return render_template('index.html',users=usr)
        
#GET Search user 
@app.route('/show_user/<email>', methods=['GET'])
def showuser(email):
    usr=User.query.filter_by(email=email).first()
    return render_template('detail.html',users=usr)

#POST add data
@app.route('/add_data', methods=['POST'])
def adddata():
    try:
        username = request.form['username']
        email=request.form['email']
        password=request.form['password']
        usr=User(username=username,password=password,email=email)    
        db.session.add(usr)
        db.session.commit()
        return jsonify({"message":"data added"})
    except:
        return jsonify({"message":"incomplete data"})

#POST update data
@app.route('/update_data/<email>', methods=['POST'])
def updatedata(email):
    update_details=User.query.filter_by(email=email).first()
    try:
        update_details.username = request.form['username']
        update_details.email=request.form['email']
        update_details.password=request.form['password']
        db.session.commit()
        return jsonify({"message":"updated"})

    except:
        return jsonify({"message":"email doesn't exist"})
    

#POST delete data using email
@app.route('/delete_data/<email>', methods=['POST'])
def deletedata(email):
    try:
        delete_details=User.query.filter_by(email=email).first()
        db.session.delete(delete_details)
        db.session.commit()
        return jsonify({"message":"deleted"})
    except:
        return jsonify({"message":"nothing to delete"})



if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

    

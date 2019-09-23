from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://optimus:##########@localhost/newdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,username,password,email):
        self.username=username
        self.email=email
        self.password=password



    
db.create_all()

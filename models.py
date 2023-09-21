from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request,redirect,url_for,session,flash
from app import app
from config import db
from werkzeug.security import check_password_hash,generate_password_hash
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


#from models import db

#print(app.config['SQLALCHEMY_DATABASE_URI']) 


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    passhash= db.Column(db.String(80),nullable=False)
    name= db.Column(db.String(80),nullable=True)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self,password):
        self.passhash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.passhash,password)
    

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True)
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    quantity = db.Column(db.Integer,nullable=False,default=0)
    man_date = db.Column(db.Date,nullable=False)

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Product %r>' % self.name
    

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True)
    products = db.relationship('Product',backref='category',lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
    
class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer,nullable=False,default=0)
    #total_price = db.Column(db.Integer,nullable=False,default=0)

    def __init__(self,quantity,total_price):
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self):
        return '<Cart %r>' % self.quantity
    
class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer,nullable=False,default=0)
    price = db.Column(db.Integer,nullable=False,default=0)
    datetime = db.Column(db.DateTime,nullable=False)

    def __init__(self,quantity,total_price):
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self):
        return '<Order %r>' % self.quantity

#create database if it doesn't exist
with app.app_context():
    db.create_all()
    

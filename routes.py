from flask import Flask,render_template,request,redirect,url_for,session,flash
from models import User,Product,Order,Category,Cart
from app import app,db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if username=='' or password=='':
        flash('Please enter all the fields')
        return redirect(url_for('login'))
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User not found')
        return redirect(url_for('login'))
    if not user.check_password(password):
        flash('Invalid password')
        return redirect(url_for('login'))
    #login successfull
    return redirect(url_for('index'))


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    name=request.form.get('name')
    if username=='' or password=='':
        flash('Please enter all the fields')
        return redirect(url_for('register'))
    if user.query.filter_by(username=username).first():
        flash ('User already exists')
        return redirect(url_for('register'))    
    user = User(username=username,password=password,name=name)
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

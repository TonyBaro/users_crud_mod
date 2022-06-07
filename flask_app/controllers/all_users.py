from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.retrieve()
    return render_template('index.html', all_users = users)

@app.route('/users/new')
def new():
    return render_template('newuser.html')

@app.route('/users/<idnum>/edit')
def edit_user(idnum):
    data ={'idnum':(idnum)}
    user = User.retrieve_user(data)
    return render_template("updateuser.html" , idnum = idnum, this_user = user)

@app.route('/add_user' , methods=["POST"])
def add():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/')

@app.route('/users/<idnum>/del')
def delete(idnum):
    data = {'id':(idnum)}
    print(data)
    User.del_user(data)
    return redirect('/')

@app.route('/users/<int:idnum>')
def one_user(idnum):
    data ={'idnum':(idnum)}
    user = User.retrieve_user(data)
    print(user)
    return render_template('user.html', this_user = user,)

@app.route('/users/<idnum>/update' , methods=["POST"])
def update_user(idnum):
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
        'id': request.form['idnum']
    }
    print(data)
    User.update_user(data)
    return redirect(f'/users/{idnum}')
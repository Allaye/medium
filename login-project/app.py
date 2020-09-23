from project_login import app, db
from flask import (Flask, request, render_template, redirect, url_for, flash, abort)
from flask_login import login_required, login_user, logout_user
from project_login.models import User
from project_login.forms import Login, Registeration

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome(): 
    return render_template('welcome.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logout')
    return redirect(url_for('home'))


@app.route('/login', methods=['POST', 'GET'])
def login():

    form = Login()
    if form.validate_on_submit():
         
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None:

            if user.check_password(form.password.data) and user is not None:
                login_user(user)
                flash('Login succesful')
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('welcome')
                return redirect(next)

    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    new_user = Registeration()
    if new_user.validate_on_submit():
        user = User(email=new_user.email.data, password= new_user.passwrd.data, username =new_user.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for your registration, navigate to the login page')
        return redirect(url_for('login'))

    return render_template('register.html', form = new_user)
 
 
if __name__ == "__main__":
    app.run(debug=True)

    
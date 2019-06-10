from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from ..user import user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            print("Hello")
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('user.homepage'))
            
        flash('Invalid Username or Password')




    return render_template('auth/login.html', title=title, login_form=login_form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    title =  'Sign Up'
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
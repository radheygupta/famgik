from . import auth
from flask import render_template, flash, redirect, request, url_for
from .forms import SignupForm, LoginForm
from flask_login import login_user, logout_user
from famgik.models import FamgikUser
from famgik import db


@auth.route('/signup', methods=['GET', 'POST'])
def user_signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = FamgikUser()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
    return render_template('auth/signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = FamgikUser.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.password == form.password.data:
                login_user(user)
                flash('Logged in successfully as {}'.format(user.first_name), 'success')
                return redirect(request.args.get('next') or url_for('index'))
            else:
                flash('User name or password is incorrect.', 'danger')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('index'))

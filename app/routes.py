from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html', title = 'TaskHero')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('/login.html', title = 'Sign In', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    return render_template('/register.html', title = 'Sign Up', form = form)
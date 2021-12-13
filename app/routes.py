from flask_login.utils import login_required
from app import app, db
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm, RegistrationForm, TaskForm, UpdateForm
from app.models import Task, User
from flask_login import current_user, login_user, logout_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(body=form.task.data, author=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Task added!')
        return redirect(url_for('index'))
    tasks = current_user.tasks
    return render_template('/index.html', title = 'TaskHero', form=form, tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Sign up was successful!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    task_to_update = Task.query.get_or_404(task_id)
    form = UpdateForm()
    if form.validate_on_submit():
        task_to_update.body = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form, title='Update task')     

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
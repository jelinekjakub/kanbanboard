from flask import render_template

from app import app


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/board')
def board():
    return render_template('board.html')


@app.route('/task')
def task_show():
    # id
    return render_template('task/show.html')


@app.route('/task/edit')
def task_edit():
    # id
    return render_template('task/edit.html')

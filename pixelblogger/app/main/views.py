from flask import render_template
from flask_login import login_required
from . import main

@main.route('/')
def index():
    return render_template('index.html')

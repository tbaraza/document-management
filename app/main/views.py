from . import main
from app import db
from flask import render_template


@main.route('/')
def index():
	return render_template('index.html')

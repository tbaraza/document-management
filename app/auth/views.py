from app import db
from ..models import User
from .forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user, login_required, current_user, logout_user
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', form=form)


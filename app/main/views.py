from . import main
from app import db
from flask import render_template, request, flash, redirect, url_for, abort
from .forms import DocForm
from ..models import Document
from flask.ext.login import current_user


@main.route('/', methods=['GET', 'POST'])
def index():
    form = DocForm()

    if request.method == 'GET':
        return render_template('index.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            # for field, errors in form.errors.itemsr():
            #     flash(u"Error in the %s field - %s" %
            #           (getattr(form, field).label.text, errors))
            post = Document(title=form.title.data,
                            link=form.link.data,
                            keywords=form.keywords.data,
                            department=form.department.data,
                            user=current_user._get_current_object())
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.index'))
        return render_template('index.html', form=form)


@main.route('/documents/<department>')
def documents(department):
    documents = Document.query.filter_by(department=department)
    if documents is None:
        abort(404)
    return render_template('docs.html', documents=documents)

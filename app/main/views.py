from flask import render_template, redirect,url_for
from . import main
from flask_login import login_required
from ..models import Blog
from .forms import NewblogForm
from .. import db

# Views
@main.route('/')
def index():

    title = 'Home - Fine Blog'
    return render_template('index.html',message = message)

@main.route('/newblog',methods = ["GET","POST"])
def newblog():
    form = NewblogForm()
    if form.validate_on_submit():
        blog = Blog (title = form.title.data, blog = form.blog.data,author = form.author.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('newblog.html',form = form,title=title)
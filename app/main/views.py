from flask import render_template, redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import Blog,Comment
from .forms import NewblogForm,CommentForm
from .. import db
from app.request import getQuotes

# Views
@main.route('/')
def index():
    quote = getQuotes()
    title = 'Home - Fine Blog'
    print(quote)
    blogs = Blog.query.all()
    return render_template('index.html',title = title,quote = quote,blogs=blogs)

@main.route('/newblog',methods = ["GET","POST"])
@login_required
def newblog():
    form = NewblogForm()
    if form.validate_on_submit():
        blog = Blog (title = form.title.data, blog = form.blog.data,author_id = current_user._get_current_object().id)
        blog.save()
        return redirect(url_for('main.index'))
    return render_template('newblog.html',form = form)

@main.route('/newcomment/<blog_id>',methods = ["GET","POST"])
@login_required
def newcomment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment = form.comment.data, blog_id = blog_id, user_id = current_user._get_current_object().id )
        new_comment.save()
        return redirect (url_for('main.index'))
    return render_template('comment.html', form = form )

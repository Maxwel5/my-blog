from flask import render_template, redirect,url_for
from . import main
from flask_login import login_required
from ..models import Blog
from .forms import NewblogForm
from .. import db
from app.request import getQuotes

# Views
@main.route('/')
def index():
    quote = getQuotes()
    title = 'Home - Fine Blog'
    print(quote)
    return render_template('index.html',title = title,quote = quote)

@main.route('/newblog',methods = ["GET","POST"])
def newblog():
    form = NewblogForm()
    if form.validate_on_submit():
        blog = Blog (title = form.title.data, blog = form.blog.data,author = form.author.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('newblog.html',form = form)

@main.route('/blog/<int:id>', methods = ['GET', 'POST'])
def blog(id):
    blog = Blog.get_post(id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.blog.data

        new_comment = Comment(comment = comment,user = current_user,blog_id = blog)

        new_comment.save_comment()


    comments = Comment.get_comments(blog)

    return render_template("blog.html", blog=blog, comment_form=comment_form, comments=comments)
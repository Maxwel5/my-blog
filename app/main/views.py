from flask import render_template
from . import main
# from flask_login import login_required
from ..models import User
from .forms import NewblogForm
from .. import db

# Views
@main.route('/')
def index():

    message = 'Fine Blog'
    return render_template('index.html',message = message)

@main.route('/newblog',methods = ["GET","POST"])
def register():
    form = NewblogForm()
    if form.validate_on_submit():
        user = User(title = form.title.data, blog = form.blog.data,author = form.author.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('main/newblog.html',newblog_form = form)
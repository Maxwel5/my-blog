from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255), nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String)
    post = db.relationship('Blog', backref='user', lazy='dynamic')
    

    @property
    def password(self):
        raise AttributeError('Password attribute cannot be read')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Blog(db.Model):
    __tablename__="blogs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    blog = db.Column(db.String(120))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    
    def __repr__(self):
        return f'User {self.title, blog, author}'



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    


    def __repr__(self):
        return f'User {self.name}'

class Quotes:
 def __init__ (self,author,quote,permalink):
   self.author = author
   self.quote = quote
   self.permalink = permalink
    
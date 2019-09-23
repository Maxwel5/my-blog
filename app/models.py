from . import db, login_manager

class Blog(db.Model):
    __tablename__="blogs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    blog = db.Column(db.String(120))
    author = db.Column(db.String(80))

    def __repr__(self):
        return f'User {self.title, blog, author}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'
    
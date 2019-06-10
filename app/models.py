from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String)
    password_hash = db.Column(db.String(255))   


    @property
    def password(self):
        raise AttributeError('You are not allowed to access password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "Writer {}".format(self.username)

class BlogPost(db.Model):
    """
    """
    __tablename__ ='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    post = db.Column(db.String)
    author = db.Column(db.String)
    postedAt = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    """
    """
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    comment = db.Column(db.String)
    postedAt = db.Column(db.DateTime, default=datetime.utcnow)
    comment_id = db.Column(db.Integer)

class Subscriber(db.Model):
    """
    """
    __tablename__="subscribers"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String)


    
class Quote:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author 
        
    
           

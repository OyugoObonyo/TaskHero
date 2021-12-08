from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """
    A class representing users of the application
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True) 
    email= db.Column(db.String(40), index=True, unique=True)
    password_hash = db.Column(db.String(50))
    
    def set_password(self):
        """
        Create a hash for user's password
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self):
        """
        Confirm that the password hash is a match
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "User = {} ".format(self.username)


class Task(db.Model):
    """
    Tasks model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    body = db.Column(db.String(120))

    def __repr__(self):
        return "Task title = {}".format(self.title)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

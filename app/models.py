from app import db

class User(db.Model):
    """
    A class representing users of the application
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True) 
    email= db.Column(db.String(40), index=True, unique=True)
    password_hash = db.Column(db.String(50))

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
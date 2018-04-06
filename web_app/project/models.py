from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship('Message', backref="user", lazy="dynamic", cascade="all,delete")

    def __str__(self):
        return self.first_name

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Message(db.Model):
    __tablename__ = "messages"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __str__(self):
        return self.content

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
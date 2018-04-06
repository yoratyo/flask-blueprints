from flask import Flask, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from web_app.project.models import db, User, Message

app = Flask(__name__)
app.config.from_pyfile('config.py')
modus = Modus(app)

#import models here
db.init_app(app)

admin = Admin(app, name='Test-Flask-Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Message, db.session))

from web_app.project.users.views import users_blueprint
from web_app.project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return redirect(url_for('users.index'))




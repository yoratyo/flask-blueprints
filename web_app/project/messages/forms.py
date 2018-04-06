from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MessageForm(FlaskForm):
    content = StringField('Content', [validators.data_required()])

# To get csrf token for delete request
class DeleteForm(FlaskForm):
    pass


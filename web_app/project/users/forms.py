from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    first_name = StringField('First Name', [validators.data_required()])
    last_name = StringField('Last Name', [validators.data_required()])

# To get csrf token for delete request
class DeleteForm(FlaskForm):
    pass


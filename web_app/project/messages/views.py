from flask import redirect, render_template, request, url_for, flash, Blueprint
from web_app.project.messages.forms import MessageForm, DeleteForm
from web_app.project.models import User, Message
from web_app.project import db

messages_blueprint = Blueprint(
    'messages', #name
    __name__, #name file blueprint
    template_folder='templates' # templates folder
)

   # Nested messages inside of users (Shallow Routing)
    # /users/<int:user_id>/messages

    # get all and create messages to spesific user
@messages_blueprint.route('/', methods= ["GET", "POST"])
def index(user_id):
    delete_form = DeleteForm()
    if request.method == "POST":
        form = MessageForm(request.form)
        if form.validate():
            new_message = Message(form.content.data, user_id)
            db.session.add(new_message)
            db.session.commit()
            flash('Message Created!')
            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template('messages/new.html', user=User.query.get(user_id), form=form)
    return render_template('messages/index.html', user=User.query.get(user_id), delete_form=delete_form)

    # new form messages
@messages_blueprint.route('/new', methods=["GET", "POST"])
def new(user_id):
    form = MessageForm()
    return render_template('messages/new.html', user=User.query.get(user_id), form=form)

    # edit form messages to spesific user
@messages_blueprint.route('/<int:id>/edit')
def edit(user_id, id):
    found_message = Message.query.get(id)
    form = MessageForm(obj=found_message)
    return render_template('messages/edit.html', message=found_message, form=form)

    # delete and Update messages to spesific user
@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def     show(user_id, id):
    found_message = Message.query.get(id)
    delete_form = DeleteForm()
    if request.method == "PATCH":
        # Update
        form = MessageForm(request.form)
        if form.validate():
            found_message.content = form.content.data
            db.session.add(found_message)
            db.session.commit()
            flash('Message Updated!')
            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template('messages/edit.html', message=found_message, form=form)
    if request.method == "DELETE":
        # Delete
        db.session.delete(found_message)
        db.session.commit()
        flash('Message Deleted!')
        return redirect(url_for('messages.index', user_id=user_id))

    return redirect(url_for('messages.index', user_id=user_id))
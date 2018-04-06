from flask import redirect, render_template, request, url_for, flash, Blueprint
from web_app.project.users.forms import UserForm, DeleteForm
from web_app.project.models import User
from web_app.project import db

users_blueprint = Blueprint(
    'users', #name
    __name__, #name file blueprint
    template_folder='templates' # templates folder
)

@users_blueprint.route('/', methods=["GET", "POST"])
def index():
    delete_form = DeleteForm()
    if request.method == "POST":
        # create users
        form = UserForm(request.form)
        if form.validate():
            new_user = User(form.first_name.data, form.last_name.data)
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!')
            return redirect(url_for('users.index'))
        else:
            return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.all(), form=delete_form)


@users_blueprint.route('/new')
def new():
    user_form = UserForm()
    return render_template('users/new.html', form=user_form)


@users_blueprint.route('/<int:id>/edit')
def edit(id):
    found_user = User.query.get(id)
    user_form = UserForm(obj=found_user)
    return render_template('users/edit.html', user=found_user, form=user_form)


@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_user = User.query.get(id)
    delete_form = DeleteForm()
    if request.method == "PATCH":
        # Update
        form = UserForm(request.form)
        if form.validate():
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            db.session.add(found_user)
            db.session.commit()
            flash('User Updated!')
            return redirect(url_for('users.index'))
        else:
            return render_template('users/edit.html', user=found_user, form=form)
    if request.method == "DELETE":
        # Delete
        db.session.delete(found_user)
        db.session.commit()
        flash('User Deleted!')
        return redirect(url_for('users.index'))

    return render_template('users/show.html', user=found_user, form=delete_form)

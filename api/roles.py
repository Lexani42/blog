from flask import request, session
from db.models import *
from .decorators import *


@is_logged
def create_role():
    user = Users.get(username=session['username'])
    if not user.role.roles:
        return 'Forbidden', 403
    try:
        data = request.form
        name = data['name']
    except KeyError:
        return 'Invalid data', 400
    try:
        Roles.create(name=name)
    except IntegrityError:
        return 'This role is already exists', 409
    return 'Ok', 200


@is_logged
def edit_role(role_id):
    user = Users.get(username=session['username'])
    if not user.role.roles:
        return 'Forbidden', 403
    try:
        role = Roles.get(id=role_id)
    except Roles.DoesNotExist:
        return 'Role not found', 404
    try:
        data = request.form
        role.comment = data['comment']
        role.like = data['like']
        role.create_topic = data['create_topic']
        role.edit_topic = data['edit_topic']
        role.edit_not_own_topic = data['edit_not_own_topic']
        role.delete_comments_and_topics = data['delete_comments_and_topics']
        role.ban_user = data['ban_user']
        role.delete_user = data['delete_user']
        role.roles = data['roles']
        role.save()
        return 'Ok', 200
    except KeyError:
        return 'Invalid data', 400


@is_logged
def delete_role(role_id):
    user = Users.get(username=session['username'])
    if not user.role.roles:
        return 'Forbidden', 403
    Roles.delete().where(Roles.id == role_id).execute()
    return 'Ok', 200

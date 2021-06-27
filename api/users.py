from flask import request, session
from db.models import *
from .decorators import *


def register():
    data = request.form
    try:
        username = data['username']
        password = data['password']
        email = data['email']
    except KeyError:
        return 'Invalid data', 400
    session['username'] = username
    session['password'] = password
    session['email'] = email
    try:
        Users.create(username=username, password=password, email=email)
    except IntegrityError:
        return 'User is already exists', 409
    return 'Registered', 200


@is_logged
def logout():
    session.clear()
    return 'Ok', 200


def login():
    try:
        data = request.form
        username = data['username']
        password = data['password']
    except KeyError:
        return 'Invalid data', 400
    try:
        user = Users.get(username=username)
    except Users.DoesNotExist:
        return 'Invalid username or password', 403
    if password == user.password:
        session['username'] = user.username
        session['password'] = user.password
        session['email'] = user.email
        return 'Ok', 200
    else:
        return 'Invalid username or password', 403


def get_all():
    result = {}
    for user in Users.select():
        result[user.id] = {'username': user.username, 'name': user.name, 'photo': user.photo}
    return result


def get(user_id):
    try:
        user = Users.get(id=user_id)
    except Users.DoesNotExist:
        return 'User does not exist', 404
    res = {'username': user.username, 'name': user.name, 'phone': user.phone, 'photo': user.photo, 'about': user.about,
           'count_of_articles': user.articles.count(), 'rating': 0, 'role': user.role.name}
    for article in user.articles:
        res['rating'] += article.likes.count() - article.dislikes.count()
    return res


def get_by_username(username):
    try:
        user = Users.get(username=username)
    except Users.DoesNotExist:
        return 'User does not exist', 404
    res = {'username': user.username, 'name': user.name, 'phone': user.phone, 'photo': user.photo, 'about': user.about,
           'count_of_articles': user.articles.count(), 'rating': 0, 'role': user.role.name}
    for article in user.articles:
        res['rating'] += article.likes.count() - article.dislikes.count()
    return res


@is_logged
def edit(user_id):
    try:
        user = Users.get(id=user_id)
    except Users.DoesNotExist:
        return 'User does not exist', 404
    if session['username'] != user.username:
        return 'Forbidden', 403
    else:
        try:
            data = request.json
            name = data['name']
            email = data['email']
            phone = data['phone']
            photo = data['photo']
            about = data['about']
            tg_notifications = data['tg_notifications']
        except KeyError:
            return 'Invalid data', 400
        user.name = name
        user.email = email
        user.phone = phone
        user.photo = photo
        user.about = about
        user.tg_notifications = tg_notifications
        user.save()
        return 'Ok', 200


@is_logged
def change_password():
    user = Users.get(username=session['username'])
    try:
        data = request.form
        password = data['password']
    except KeyError:
        return 'Invalid data', 400
    user.password = password
    session['password'] = password
    user.save()
    return 'Ok', 200


@is_logged
def delete(user_id):
    requesting = Users.get(username=session['username'])
    if not requesting.role.delete_user:
        return 'Forbidden', 403
    Users.delete().where(Users.id == user_id).execute()
    return 'OK', 200


@is_logged
def change_role(user_id):
    requesting = Users.get(username=session['username'])
    if not requesting.role.change_user_role:
        return 'Forbidden', 403
    try:
        data = request.form
        new_role_id = data['new_role_id']
    except KeyError:
        return 'Invalid data', 400
    try:
        role = Roles.get(id=new_role_id)
    except Roles.DoesNotExist:
        return 'Role not found', 404
    try:
        user = Users.get(id=user_id)
    except Users.DoesNotExist:
        return 'User not found', 404
    user.role = role
    user.save()
    return 'Ok', 200


@is_logged
def ban(user_id):
    requesting = Users.get(username=session['username'])
    if not requesting.role.change_user_role:
        return 'Forbidden', 403
    try:
        user = Users.get(id=user_id)
    except Users.DoesNotExist:
        return 'User not found', 404
    role = Roles.get(id=3)
    user.role = role
    user.save()
    return 'Ok', 200

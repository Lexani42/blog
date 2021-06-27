from flask import request, session
from db.models import *
from .decorators import *


@is_logged
def add_comment(article_id):
    user = Users.get(username=session['username'])
    if not user.role.comment:
        return 'Forbidden', 403
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    try:
        data = request.form
        Comments.create(user=user, article=article, content=data['content'])
        return 'Ok', 200
    except KeyError:
        return 'Invalid data', 400


@is_logged
def edit_comment(comment_id):
    user = Users.get(username=session['username'])
    if not user.role.comment:
        return 'Forbidden', 403
    try:
        comment = Comments.get(id=comment_id)
    except Comments.DoesNotExist:
        return 'Comment not found', 404
    if user != comment.user:
        return 'Forbidden', 403
    try:
        data = request.form
        comment.content = data['content']
        comment.save()
        return 'Ok', 200
    except KeyError:
        return 'Invalid data', 400


@is_logged
def delete_comment(comment_id):
    user = Users.get(username=session['username'])
    if not user.role.comment:
        return 'Forbidden', 403
    try:
        comment = Comments.get(id=comment_id)
    except Comments.DoesNotExist:
        return 'Ok', 200
    if comment.user == user or user.role.delete_comments_and_topics:
        Comments.delete().where(Comments.id == comment_id).execute()
        return 'Ok', 200
    return 'Forbidden', 403

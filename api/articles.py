from flask import request, session
from db.models import *
from .decorators import *


@is_logged
def create_article():
    user = Users.get(username=session['username'])
    if not user.role.create_topic:
        return 'Forbidden', 403
    try:
        data = request.form
        Articles.create(
            title=data['title'],
            content=data['content'],
            author=user
        )
        return 'Ok', 200
    except KeyError:
        return 'Invalid data', 400


def get_articles():
    res = {}
    for article in Articles.select():
        res[article.id] = {
            'title': article.title,
            'author': article.author.username
        }
    return res, 200


def get_article(article_id):
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    res = {'title': article.title, 'content': article.content, 'author': article.author.id, 'comments': {}}
    for comment in article.comments:
        res['comments'][comment.id] = {'author': comment.author.id, 'content': comment.content}



@is_logged
def update_article(article_id):
    user = Users.get(username=session['username'])
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    if (user != article.author) and (not user.role.edit_not_own_topic):
        return 'Forbidden', 403
    try:
        data = request.form
        article.title = data['title']
        article.content = data['content']
        article.save()
        return 'Ok', 200
    except KeyError:
        return 'Invalid data', 400


@is_logged
def delete_article(article_id):
    user = Users.get(username=session['username'])
    if not user.role.delete_comments_and_topics:
        return 'Forbidden', 403
    Articles.delete().where(Articles.id == article_id).execute()
    return 'Ok', 200


@is_logged
def like(article_id):
    user = Users.get(username=session['username'])
    if not user.role.like:
        return 'Forbidden', 403
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    try:
        Likes.get(user=user, article=article)
        return 'Liked already', 409
    except Likes.DoesNotExist:
        Dislikes.delete().where((Dislikes.user == user) & (Dislikes.article == article)).execute()
        Likes.create(user=user, article=article)
        return 'Ok', 200


@is_logged
def del_like(article_id):
    user = Users.get(username=session['username'])
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    Likes.delete().where((Likes.user == user) & (Likes.article == article)).execute()
    return 'Ok', 200


@is_logged
def dislike(article_id):
    user = Users.get(username=session['username'])
    if not user.role.like:
        return 'Forbidden', 403
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    try:
        Dislikes.get(user=user, article=article)
        return 'Disliked already', 409
    except Dislikes.DoesNotExist:
        Likes.delete().where((Likes.user == user) & (Likes.article == article)).execute()
        Dislikes.create(user=user, article=article)
        return 'Ok', 200


@is_logged
def del_dislike(article_id):
    user = Users.get(useranme=session['username'])
    try:
        article = Articles.get(id=article_id)
    except Articles.DoesNotExist:
        return 'Article not found', 404
    Dislikes.delete().where((Dislikes.user == user) & (Dislikes.article == article)).execute()
    return 'Ok', 200

from flask import session
from db.models import *


def is_logged(f):
    def wrapper(*args, **kwargs):
        try:
            username = session['username']
        except KeyError:
            return 'Unauth', 403
        user = Users.get(username=username)
        if user.password == session['password']:
            return f(*args, **kwargs)
        else:
            return 'Invalid credentials', 403
    wrapper.__name__ = f.__name__
    return wrapper

from flask import Flask
from api import users, roles, articles, comments
app = Flask(__name__)
app.secret_key = 'SDjkgshdfjghsdjfghKJSDfhgkjdsfg'

# users
app.add_url_rule(
    '/api/users/login',
    'login',
    users.login,
    methods=['POST']
)
app.add_url_rule(
    '/api/users/register',
    'register',
    users.register,
    methods=['POST']
)
app.add_url_rule(
    '/api/users/logout',
    'logout',
    users.logout,
    methods=['POST']
)
app.add_url_rule(
    '/api/users',
    'get_all',
    users.get_all,
    methods=['GET']
)
app.add_url_rule(
    '/api/users/<user_id>',
    'get',
    users.get,
    methods=['GET']
)
app.add_url_rule(
    '/api/users/<user_id>',
    'edit',
    users.edit,
    methods=['PUT']
)
app.add_url_rule(
    '/api/users/change_password',
    'change_password',
    users.change_password,
    methods=['POST']
)
app.add_url_rule(
    '/api/users/<user_id>/change_role',
    'change_role',
    users.change_role,
    methods=['PUT']
)
app.add_url_rule(
    '/api/users/<user_id>/ban',
    'ban',
    users.ban,
    methods=['POST']
)
app.add_url_rule(
    '/api/users/<user_id>',
    'delete',
    users.delete,
    methods=['DELETE']
)

# roles
app.add_url_rule(
    '/api/roles/',
    'create_role',
    roles.create_role,
    methods=['POST']
)
app.add_url_rule(
    '/api/roles/<role_id>',
    'edit_role',
    roles.edit_role,
    methods=['PUT']
)
app.add_url_rule(
    '/api/roles/<role_id>',
    'delete_role',
    roles.delete_role,
    methods=['DELETE']
)

# articles
app.add_url_rule(
    '/api/articles/',
    'create_article',
    articles.create_article,
    methods=['POST']
)
app.add_url_rule(
    '/api/articles',
    'get_articles',
    articles.get_articles,
    methods=['GET']
)
app.add_url_rule(
    '/api/articles/<article_id>',
    'get_article',
    articles.get_article,
    methods=['GET']
)
app.add_url_rule(
    '/api/articles/<article_id>/',
    'update_article',
    articles.update_article,
    methods=['PUT']
)
app.add_url_rule(
    '/api/articles/<article_id>/',
    'delete_article',
    articles.delete_article,
    methods=['DELETE']
)
app.add_url_rule(
    '/api/articles/<article_id>/',
    'delete_article',
    articles.delete_article,
    methods=['DELETE']
)

# likes
app.add_url_rule(
    '/api/articles/<article_id>/like/',
    'like',
    articles.like,
    methods=['POST']
)
app.add_url_rule(
    '/api/articles/<article_id>/del_like/',
    'del_like',
    articles.del_like,
    methods=['POST']
)
app.add_url_rule(
    '/api/articles/<article_id>/dislike/',
    'dislike',
    articles.dislike,
    methods=['POST']
)
app.add_url_rule(
    '/api/articles/<article_id>/del_dislike/',
    'del_dislike',
    articles.del_dislike,
    methods=['POST']
)

# comments
app.add_url_rule(
    '/api/articles/<article_id>/add_comment/',
    'add_comment',
    comments.add_comment,
    methods=['POST']
)
app.add_url_rule(
    '/api/comments/<comment_id>/',
    'edit_comment',
    comments.edit_comment,
    methods=['PUT']
)
app.add_url_rule(
    '/api/articles/<comment_id>/',
    'delete_comment',
    comments.delete_comment,
    methods=['DELETE']
)

# follows
app.add_url_rule(
    '/api/users/<user_id>/follow/',
    'follow',
    users.follow,
    methods=['POST']
)
app.add_url_rule(
    '/api/users/<user_id>/unfollow/',
    'unfollow',
    users.unfollow,
    methods=['POST']
)


if __name__ == '__main__':
    app.run()

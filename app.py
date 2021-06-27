from flask import Flask
from api import users, roles
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

#roles
app.add_url_rule(
    '/api/roles/',
    'create_role',
    roles.create_role,
    methods=['POST']
)
app.add_url_rule(
    '/api/roles/<role_id>/',
    'edit_role',
    roles.edit_role,
    methods=['PUT']
)
app.add_url_rule(
    '/api/roles/',
    'create_role',
    roles.create_role,
    methods=['DELETE']
)

if __name__ == '__main__':
    app.run()

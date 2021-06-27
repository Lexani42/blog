from models import *

db.create_tables([Users, Articles, Likes, Dislikes, Follows, Comments, Roles])


Roles.create(name='Администратор', edit_not_own_topic=True, delete_comments_and_topics=True, ban_user=True, delete_user=True, roles=True)
Roles.create(name='Пользователь')
Roles.create(name='Забанен', comment=False, like=False, create_topic=False, edit_topic=False)

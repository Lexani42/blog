from peewee import *

db = PostgresqlDatabase('blog_db', user='postgres', password='lexani42', host='127.0.0.1', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Roles(BaseModel):
    name = TextField(null=False, unique=True)
    comment = BooleanField(null=False, default=True)
    like = BooleanField(null=False, default=True)
    create_topic = BooleanField(null=False, default=True)
    edit_topic = BooleanField(null=False, default=True)
    edit_not_own_topic = BooleanField(null=False, default=False)
    delete_comments_and_topics = BooleanField(null=False, default=False)
    ban_user = BooleanField(null=False, default=False)
    delete_user = BooleanField(null=False, default=False)
    change_user_role = BooleanField(null=False, default=False)


class Users(BaseModel):
    username = TextField(unique=True, null=False)
    name = TextField(null=False, default='Аноним')
    password = TextField(null=False)
    email = TextField(null=False)
    phone = TextField(null=True)
    photo = TextField(null=False, default='https://xn----7sbfpkp2apbuh.xn--p1ai/wp-content/uploads/2019/06/noavatar.png')
    about = TextField(null=True)
    tg_notifications = BooleanField(null=False, default=False)
    role = ForeignKeyField(Roles, backref='users', on_delete='CASCADE', default=2)


class Articles(BaseModel):
    title = TextField(null=False)
    content = TextField(null=False)
    author = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='articles')


class Likes(BaseModel):
    user = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='likes_sent')
    article = ForeignKeyField(Articles, null=False, on_delete='CASCADE', backref='likes_received')


class Dislikes(BaseModel):
    user = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='dislikes_sent')
    article = ForeignKeyField(Articles, null=False, on_delete='CASCADE', backref='dislikes_received')


class Follows(BaseModel):
    from_user = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='following')
    to_user = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='followers')


class Comments(BaseModel):
    user = ForeignKeyField(Users, null=False, on_delete='CASCADE', backref='comments')
    article = ForeignKeyField(Articles, null=False, on_delete='CASCADE', backref='comments')
    content = TextField(null=False)

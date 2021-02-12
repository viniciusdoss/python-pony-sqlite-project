from pony import orm
from users import def_users_entity
from posts import def_posts_entity
from faking_users import fake_users, get_users_posts, del_user, delete_users_bulk, update_user


db = orm.Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
users_class = def_users_entity(db, orm)
posts_class = def_posts_entity(db, orm, users_class)

db.generate_mapping(create_tables=True)

#fake_users(users_class, posts_class)
#get_users_posts(posts_class)
#del_user(users_class, 5)
#delete_users_bulk(users_class)
update_user(users_class, 10, 'Vinicius')
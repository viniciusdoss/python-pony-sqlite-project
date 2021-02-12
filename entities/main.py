from pony import orm
from users import def_users_entity
from posts import def_posts_entity

db = orm.Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
users_class = def_users_entity(db, orm)
def_posts_entity(db, orm, users_class)

db.generate_mapping(create_tables=True)

def def_users_entity(db, orm):
    class Users(db.Entity):
        __table__ = 'users'
        id = orm.PrimaryKey(int, auto=True)
        first_name = orm.Required(str, 40)
        second_name = orm.Required(str, 40)
        age = orm.Required(int)
        about = orm.Optional(str, nullable=False)
        email = orm.Required(str, unique=True)
        posts = orm.Set('Posts')
    return Users


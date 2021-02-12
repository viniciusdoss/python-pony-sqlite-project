def def_posts_entity(db, orm, Users):
    class Posts(db.Entity):
        __table__ = 'posts'
        id = orm.PrimaryKey(int, auto=True)
        title = orm.Required(str, 40)
        body = orm.Required(str) # text
        user = orm.Required(Users, column='user_id') # user (int)
    return Posts
from pony.orm import db_session
import json
from faker import Faker

fake = Faker()

@db_session()
def fake_users(Users, Posts, amount=10):
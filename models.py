import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase("taco.db")

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    
    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        """Create a new user"""
        try:
            with DATABASE.transaction():
                cls.create(
                 email=email,
                 password=generate_password_hash(password)
                )
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    protein = CharField(max_length=25)
    shell = CharField(max_length=25)
    cheese = BooleanField()
    extras = CharField(max_length=250)
    user = ForeignKeyField(
        User,
        related_name='tacos'
    )
    
    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco])
    DATABASE.close()
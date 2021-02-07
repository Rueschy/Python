from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pwmdb.sqlite', echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    # users table
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    email = Column(String(30), nullable=True)
    password = Column(String(128))

    # constructor
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # getters and setters
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_username(self, value):
        self.username = value

    def set_email(self, value):
        self.email = value

    def set_password(self, value):
        self.password = value


session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine, checkfirst=True)


def add_user(username, email, password):
    s = session()
    user = User(username, email, password)
    s.add(user)
    s.commit()


def get_user(username):
    s = session()
    for user in s.query(User):
        if user.username == username:
            return user
    return False


def get_all_users():
    s = session()
    users = s.query.all()
    return users

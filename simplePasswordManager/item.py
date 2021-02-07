from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pwmdb.sqlite', echo=True)
Base = declarative_base(bind=engine)


class Item(Base):
    # items table
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    username = Column(String(30))
    password = Column(String(128))

    # constructor
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine, checkfirst=True)


def add_item(name, username, password):
    s = session()
    item = Item(name, username, password)
    s.add(item)
    s.commit()


def get_item(name):
    s = session()
    for item in s.query(Item):
        if item.name == name:
            return item
    return False


def get_all_items():
    s = session()
    items = s.query.all()
    return items

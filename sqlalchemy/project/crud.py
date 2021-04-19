# Session and engine will usually be defined at the top of db.py or crud.py
#
# Import Session and make a new s whenever we wish to interact with the
# database.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from datetime import datetime
# import yaml

from secrets import DATABASE_URI
# DATABASE_URI = "postgresql+psycopg2://<user>:<password>@<URL>:<port>/<table>"

from models import Book

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_database():
    Book.metadata.create_all(engine)


def reset_database():
    Book.metadata.drop_all(engine)
    Book.metadata.create_all(engine)


def rm_database():
    Book.metadata.drop_all(engine)


# reset_database()

s = Session()

# book = Book(
#     title='Deep Learning',
#     author='Ian Goodfellow',
#     pages=775,
#     published=datetime(2016, 11, 18)
# )
# s.add(book)
# s.commit()


# for data in yaml.load_all(open('books.yaml')):
#     book = Book(**data)
#     s.add(book)
# s.commit()
# s.close()

# s.close_all_sessions()

# result = s.query(Book).first()
# print(result)

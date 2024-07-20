from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.testing import db

from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String
from sqlalchemy.types import Integer


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    image = Column(String)
    about = Column(String)

    text = Column(String)
    image2 = Column(String)
    about2 = Column(String)
    articles = relationship('Article',back_populates="user")


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



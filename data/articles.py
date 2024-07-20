from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer

from .db_session import SqlAlchemyBase


class Article(SqlAlchemyBase):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(ForeignKey("users.id"))
    user = relationship('User', back_populates="articles")
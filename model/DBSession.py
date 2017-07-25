#coding=utf8
from sqlalchemy import Column, String, create_engine, Integer,ForeignKey,Text,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BlogUser(Base):
    #table name
    __tablename__ = 'blog_name'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(100))
    description = Column(String(100))


class BlogCategory(Base):

    #table name
    __tablename__ = 'blog_category'
    id = Column(Integer, primary_key=True,autoincrement=True)
    href = Column(String(100))
    tag_name = Column(String(100))


class Article(Base):

    #table name
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True,autoincrement=True)
    tag_id = Column(Integer, ForeignKey('blog_category.id'))
    link = Column(String(500))
    title = Column(String(500))
    content = Column(Text)
    update_time = Column(DateTime)



engine = create_engine('mysql://root:admin@localhost:3306/peak',connect_args={"charset": "utf8"})


DBSession = sessionmaker(bind=engine)
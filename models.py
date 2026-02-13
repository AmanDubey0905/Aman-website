from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    owner_id = Column(String)
    content = Column(Text)
    status = Column(String, default="uploaded")

class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(String)

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    owner_id = Column(String)

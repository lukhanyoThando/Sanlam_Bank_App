from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    balance = Column(Numeric(precision=12, scale=2))

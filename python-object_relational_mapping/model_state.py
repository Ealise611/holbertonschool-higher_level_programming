#!/usr/bin/python3
"""
This module contains the definition of the State class
and in instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """
    State class:
    inherits from Base
    links to the MySQL table states
    Class attributes: id represent a colunm of an auto-generated,
    unique integer, can't be NULL and is a primary key
    Class attributes: name represent a column of a string with maximum
    length of 128, can't be NULL
    Must use the module sqlalchemy (import sqlalchemy)
    This script should connect to a MYSQL server running on
    localhost at port 3306
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

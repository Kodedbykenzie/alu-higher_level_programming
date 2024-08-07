#!/usr/bin/python3
"""Defines the State class linked to the cities relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship with the City class
    cities = relationship("City", backref="state", cascade="all, delete-orphan")



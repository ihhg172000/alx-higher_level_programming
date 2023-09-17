#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List


class Base(DeclarativeBase):
    pass


class State(Base):
    """
    The definition os State class.
    """
    __tablename__ = 'states'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped[List['City']] = relationship(
        cascade="all, delete",
        back_populates='state'
    )

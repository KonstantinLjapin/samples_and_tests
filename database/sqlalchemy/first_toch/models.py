from __future__ import annotations
from sqlalchemy import MetaData, Table, Column, Integer, String
import asyncio
import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class B(Base):
    __tablename__ = "b"
    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]


class A(Base):
    __tablename__ = "a"
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]
    create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    bs: Mapped[List[B]] = relationship()


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(index=True)
    password: Mapped[str] = mapped_column(index=True)
    books: Mapped[List[Book]] = relationship()


meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


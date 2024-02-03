from app.db import Base
from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from datetime import date, datetime

class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=False) 
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    birthday: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    additional_data: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    emails: Mapped[List['Email']] = relationship()
    phones: Mapped[List['Phone']] = relationship()

class Email(Base):
    __tablename__ = 'emails'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    contact_id: Mapped[int] = mapped_column(Integer, ForeignKey('contacts.id'))

class Phone(Base):
    __tablename__ = 'phones'
    id: Mapped[int] = mapped_column(Integer,  primary_key=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=False)
    contact_id: Mapped[int] = mapped_column(Integer, ForeignKey('contacts.id'))
# coding=utf-8

import datetime as dt

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Enum

from .base import Base
from .transaction_type import TransactionType


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Numeric)
    created_at = Column(DateTime)
    type = Column(Enum(TransactionType))

    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()

# coding=utf-8

import datetime as dt

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .transaction_type import TransactionType
from .tag import TagSerializer

transactions_tags_association = Table(
    'transactions_tags', Base.metadata,
    Column('transaction_id', Integer, ForeignKey('transaction.id')),
    Column('tag_name', String, ForeignKey('tag.name'))
)


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Numeric)
    created_at = Column(DateTime)
    transaction_type = Column(Enum(TransactionType))
    tags = relationship("Tag", secondary=transactions_tags_association)

    def __init__(self, description, amount, transaction_type, tags):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.transaction_type = transaction_type
        self.tags = tags

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    transaction_type = fields.Str()
    tags = TagSerializer()

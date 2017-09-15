# coding=utf-8

import datetime as dt
from marshmallow import Schema, fields, post_load


class Expense(object):
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Expense(name={self.description!r})>'.format(self=self)


class ExpenseSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    release_date = fields.Date()

    @post_load
    def make_expense(self, data):
        return Expense(**data)

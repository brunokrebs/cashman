# coding=utf-8

from marshmallow import fields
from sqlalchemy import Column, String

from .base import Base


class Tag(Base):
    __tablename__ = 'tag'
    name = Column(String, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag(name={self.name!r})>'.format(self=self)


class TagSerializer(fields.Field):
    def _serialize(self, values, attr, obj):
        if values is None or len(values) == 0:
            return
        tags = []
        for value in values:
            tags.append(value.name)
        return tags

    def _deserialize(self, values, attr, data):
        tags = []
        for value in values:
            tags.append(Tag(value))
        return tags

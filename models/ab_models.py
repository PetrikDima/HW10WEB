from mongoengine import Document, StringField, connect, DateField

from database.db import URL
conn = connect(host=URL)


class Addressbook(Document):
    name = StringField(max_length=100, min_length=1, required=True)
    phone = StringField(max_length=100, default='')
    birthday = DateField(max_length=100, default='', null=True)
    email = StringField(max_length=100, default='')
    address = StringField(max_length=120, default='')

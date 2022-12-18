from datetime import datetime

import redis
from mongoengine import connect, IntField, Document, StringField, ListField, BooleanField, DateTimeField, ReferenceField, CASCADE
from redis_lru import RedisLRU

from database.db import URL

conn = connect(host=URL)
client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


class Tag(Document):
    id_count = IntField()
    tags = ListField(StringField(max_length=80))


class Note(Document):
    id_count = IntField()
    text = StringField(max_length=1000)
    done = BooleanField(default=False)
    created = DateTimeField(default=datetime.now())
    tags = ReferenceField(Tag, reverse_delete_rule=CASCADE, dbref=True)


class Archive(Document):
    id_count = IntField()
    text = StringField(max_length=1000)
    transferred = DateTimeField(default=datetime.now())
    tags = ReferenceField(Tag, reverse_delete_rule=CASCADE, dbref=True)

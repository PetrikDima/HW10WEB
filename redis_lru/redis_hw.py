import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


@cache
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


print(factorial(5))
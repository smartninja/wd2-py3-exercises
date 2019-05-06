import os
import uuid
import smartninja_redis

redis = smartninja_redis.from_url(os.environ.get("REDIS_URL"))


def create_csrf_token(username):
    csrf_token = str(uuid.uuid4())
    redis.set(name=csrf_token, value=username)

    return csrf_token


def validate_csrf(csrf, username):
    redis_csrf_username = redis.get(name=csrf).decode()  # csrf from Redis (needs to be decoded from byte string)

    # if CSRF token is found in cache and usernames match, allow user to create a comment
    if redis_csrf_username and username == redis_csrf_username:
        return True
    else:
        return False

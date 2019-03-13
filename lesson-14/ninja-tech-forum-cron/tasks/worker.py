import os
from huey import RedisHuey

# worker
huey = RedisHuey(url=os.getenv('REDIS_URL'))

import os
import random
from huey import RedisHuey

# worker
huey = RedisHuey(url=os.getenv('REDIS_URL'))


# task
@huey.task(retries=5, retry_delay=5)
def get_random_num():
    print("This is a task to get a random number")
    num = random.randint(1, 3)
    print("Random number is {}".format(num))

    if num == 1:  # if number is 1, the task was successful
        return True
    else:  # if number is not 1, raise an error (so that we see how a failed task looks like and what happens next)
        raise Exception("Error in the worker... :(")

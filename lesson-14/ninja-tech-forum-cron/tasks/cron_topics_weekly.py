from .worker import huey
from huey import crontab


@huey.periodic_task(crontab(day_of_week='1', hour='8', minute='0'))  # 1 is Monday
def new_topics_weekly():
    # code for sending a weekly email
    return

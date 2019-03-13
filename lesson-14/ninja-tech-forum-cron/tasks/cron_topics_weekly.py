import datetime

from .worker import huey
from huey import crontab
from models.user import User
from models.topic import Topic
from utils.email_helper import send_email_to_one_recipient


@huey.periodic_task(crontab(day_of_week='1', hour='8', minute='0'))  # 1 is Monday
def new_topics_weekly():
    # get topics from the previous week
    topics = Topic.get_topics_date_range(lt=datetime.datetime.now(),  # between today
                                         gt=(datetime.datetime.now() - datetime.timedelta(days=7)))  # and 7 days ago

    # if no topics, finish the task without sending the email
    if not topics:
        print("No new topics created last week, so no email will be sent.")
    else:
        # create an email message
        message = "Topics created in the previous week:\n"

        for topic in topics:
            message += "- {0}\n".format(topic.title)

        # get all Ninja Tech Forum users
        users = User.get_all_users()

        for user in users:
            if user.email_address:
                send_email_to_one_recipient(recipient_email=user.email_address,
                                            subject="See topics from the last week", message=message)

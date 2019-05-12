import datetime
from models.user import User
from models.topic import Topic
from utils.email_helper import send_email_to_one_recipient


def new_topics_email():
    # get topics from yesterday
    topics = Topic.get_topics_date_range(lt=datetime.datetime.now(),  # between today
                                         gt=(datetime.datetime.now() - datetime.timedelta(days=1)))  # and 1 day ago

    # if no topics, finish the task without sending the email
    if not topics:
        print("No new topics created yesterday, so no email will be sent.")
    else:
        # create an email message
        message = "Topics created yesterday:\n"

        for topic in topics:
            message += "- {0}\n".format(topic.title)

        # get all Ninja Tech Forum users
        users = User.get_all_users()

        for user in users:
            if user.email_address:
                send_email_to_one_recipient(recipient_email=user.email_address,
                                            subject="See new topics at Ninja Tech Forum", message=message)


if __name__ == '__main__':
    new_topics_email()

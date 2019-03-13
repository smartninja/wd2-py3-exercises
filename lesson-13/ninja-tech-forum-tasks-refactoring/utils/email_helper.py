import os


def send_email_to_one_recipient(recipient_email, subject, message):
    if os.getenv('REDIS_URL'):
        from tasks import send_email
        send_email(recipient_email, subject, message)
    else:
        print("You are on localhost, so the email will not be really sent.")
        print("---------------EMAIL MESSAGE----------------")
        print("Email recipient: {}".format(recipient_email))
        print("Subject: {}".format(subject))
        print(message)
        print("---------------EMAIL MESSAGE----------------")

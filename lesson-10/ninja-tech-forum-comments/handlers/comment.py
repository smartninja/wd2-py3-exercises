from flask import render_template, request, redirect, url_for, Blueprint
from models.user import User
from models.comment import Comment
from models.database import redis


comment_handlers = Blueprint("comment", __name__)


@comment_handlers.route("/topic/<topic_id>/create-comment", methods=["POST"])
def comment_create(topic_id):
    # get current user (comment author)
    session_token = request.cookies.get("session_token")
    user = User.get_by_session_token(session_token=session_token)

    # only logged in users can create a comment
    if not user:
        return redirect(url_for('auth.login'))

    csrf = request.form.get("csrf")  # csrf from HTML
    redis_csrf = redis.get(name=user.username).decode()  # csrf from Redis (needs to be decoded from byte string)

    # if they match, allow user to create a comment
    if csrf and csrf == redis_csrf:
        text = request.form.get("text")

        # create a Comment object
        comment = Comment(topic_id=topic_id, text=text, author_id=user._id, author_username=user.username)
        comment.insert()

        return redirect(url_for('topic.topic_details', topic_id=topic_id))
    else:
        return "CSRF token is not valid!"

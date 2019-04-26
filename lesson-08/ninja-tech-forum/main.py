import hashlib

from flask import Flask, render_template, request, redirect, url_for, make_response
from models.user import User
from models.topic import Topic

app = Flask(__name__)


@app.route("/")
def index():
    # check if user is authenticated based on session_token
    session_token = request.cookies.get("session_token")
    user = User.get_by_session_token(session_token=session_token)

    # get all topics from db
    topics = Topic.get_all_topics()

    return render_template("index.html", user=user, topics=topics)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        user = User.get_by_username(username=username)

        if not user:
            return "This user does not exist"
        else:
            # if user exists, check if password hashes match
            if password_hash == user.password_hash:
                user.set_new_session_token()

                # save user's session token into a cookie
                response = make_response(redirect(url_for('index')))
                response.set_cookie("session_token", user.session_token, httponly=True, samesite='Strict')

                return response
            else:
                return "Your password is incorrect!"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repeat = request.form.get("repeat")

        if password != repeat:
            return "Passwords do not match! Go back and try again."

        # check if username already exists
        user_exists = User.get_by_username(username=username)
        if user_exists:
            return "A user with this username already exists. Try a more unique username."

        user = User(username=username, password_hash=hashlib.sha256(password.encode()).hexdigest())
        user.insert()

        # save user's session token into a cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie("session_token", user.session_token, httponly=True, samesite='Strict')

        return response


@app.route("/create-topic", methods=["GET", "POST"])
def topic_create():
    if request.method == "GET":
        return render_template("topic_create.html")

    elif request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")

        # get current user (author)
        session_token = request.cookies.get("session_token")
        user = User.get_by_session_token(session_token=session_token)

        # only logged in users can create a topic
        if not user:
            return redirect(url_for('login'))

        # create a Topic object
        topic = Topic(title=title, text=text, author_id=user._id, author_username=user.username)
        topic.insert()

        return redirect(url_for('index'))


@app.route("/topic/<topic_id>", methods=["GET"])
def topic_details(topic_id):
    topic = Topic.get_by_id(topic_id=topic_id)

    # get current user
    session_token = request.cookies.get("session_token")
    user = User.get_by_session_token(session_token=session_token)

    return render_template("topic_details.html", topic=topic, user=user)


@app.route("/topic/<topic_id>/edit", methods=["GET", "POST"])
def topic_edit(topic_id):
    topic = Topic.get_by_id(topic_id=topic_id)

    if request.method == "GET":
        return render_template("topic_edit.html", topic=topic)

    elif request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")

        # get current user (author)
        session_token = request.cookies.get("session_token")
        user = User.get_by_session_token(session_token=session_token)

        # check if user is logged in and user is author
        if not user:
            return redirect(url_for('login'))
        elif topic.author_id != user._id:
            return "You are not the author!"
        else:  # if user IS logged in and current user IS author
            Topic.edit_topic(topic_id=topic_id, updates_dict={"title": title, "text": text})
            return redirect(url_for('topic_details', topic_id=topic_id))


if __name__ == '__main__':
    app.run(debug=True)

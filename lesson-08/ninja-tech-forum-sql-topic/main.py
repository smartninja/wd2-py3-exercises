import hashlib
import uuid
from flask import Flask, render_template, request, redirect, url_for, make_response

from models.topic import Topic
from models.user import User
from models.settings import db

app = Flask(__name__)

# create tables in a database (important: this does not update tables, only creates new ones)
db.create_all()


@app.route("/")
def index():
    # check if user is authenticated based on session_token
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()

    # get topics
    topics = db.query(Topic).all()

    return render_template("index.html", user=user, topics=topics)


@app.route("/create-topic", methods=["GET", "POST"])
def topic_create():
    if request.method == "GET":
        return render_template("topic_create.html")

    elif request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")

        # get current user (author)
        session_token = request.cookies.get("session_token")
        user = db.query(User).filter_by(session_token=session_token).first()

        # only logged in users can create a topic
        if not user:
            return redirect(url_for('login'))

        # create a Topic object
        topic = Topic.create(title=title, text=text, author=user)

        return redirect(url_for('index'))


@app.route("/topic/<topic_id>", methods=["GET"])
def topic_details(topic_id):
    topic = db.query(Topic).get(int(topic_id))

    # get current user (author)
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()

    return render_template("topic_details.html", topic=topic, user=user)


@app.route("/topic/<topic_id>/edit", methods=["GET", "POST"])
def topic_edit(topic_id):
    topic = db.query(Topic).get(int(topic_id))

    if request.method == "GET":
        return render_template("topic_edit.html", topic=topic)

    elif request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")

        # get current user (author)
        session_token = request.cookies.get("session_token")
        user = db.query(User).filter_by(session_token=session_token).first()

        # check if user is logged in and user is author
        if not user:
            return redirect(url_for('login'))
        elif topic.author.id != user.id:
            return "You are not the author!"
        else:
            # update the topic fields
            topic.title = title
            topic.text = text
            db.add(topic)
            db.commit()

            return redirect(url_for('topic_details', topic_id=topic_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # get password hash out of password
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # get user from database by her/his username and password
        user = db.query(User).filter_by(username=username).first()

        if not user:
            return "This user does not exist"
        else:
            # if user exists, check if password hashes match
            if password_hash == user.password_hash:
                user.session_token = str(uuid.uuid4())  # if password hashes match, create a session token
                db.add(user)
                db.commit()

                # save user's session token into a cookie
                response = make_response(redirect(url_for('index')))
                response.set_cookie("session_token", user.session_token)  # you might want to set httponly=True on production

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

        user = User(username=username, password_hash=hashlib.sha256(password.encode()).hexdigest(),
                    session_token=str(uuid.uuid4()))
        db.add(user)  # add to the transaction (user is not yet in a database)
        db.commit()  # commit the transaction into the database (user is now added in the database)

        # save user's session token into a cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie("session_token", user.session_token)  # you might want to set httponly=True on production

        return response


if __name__ == '__main__':
    app.run()

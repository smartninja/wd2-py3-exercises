import hashlib

from flask import Flask, render_template, request, redirect, url_for, make_response
from models.user import User

app = Flask(__name__)


@app.route("/")
def index():
    # check if user is authenticated based on session_token
    session_token = request.cookies.get("session_token")
    user = User.get_by_session_token(session_token=session_token)

    return render_template("index.html", user=user)


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
                response.set_cookie("session_token", user.session_token)

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
        response.set_cookie("session_token", user.session_token)

        return response


if __name__ == '__main__':
    app.run()

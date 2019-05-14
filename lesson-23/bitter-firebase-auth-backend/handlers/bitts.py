import json

from flask import Blueprint, request, render_template, jsonify
from models.bitt import Bitt

import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)

bitt_handlers = Blueprint("topic", __name__)


@bitt_handlers.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bitt_handlers.route("/get-all-bitts", methods=["GET"])
def bitts_get_all():
    # check if browser sent a last bitt id as URL parameter
    browser_last_bitt_id = request.args.get("lastid", default="Nothing", type=str)

    # if browser last Bitt id is the same as backend last Bitt ID, don't make a DB query
    if browser_last_bitt_id == Bitt.get_last_bitt_id():
        return jsonify({"success": True, "synced": True})
    else:
        # get all bitts from db
        bitts = Bitt.get_all_bitts()

        if not bitts:
            print("No bitts yet")

        return jsonify([bitt.to_dict for bitt in bitts])


@bitt_handlers.route("/create-bitt", methods=["POST"])
def bitt_create():
    username = request.json.get("username")
    text = request.json.get("text")
    id_token = request.json.get("idtoken")

    # verify the id_token
    decoded_token = auth.verify_id_token(id_token)
    email = decoded_token['email']

    # check if the email sent by user inside the username field is the same as email from the encrypted id token
    if username == email and text:
        bitt = Bitt(text=text, username=username)
        bitt.insert()

        return jsonify(bitt.to_dict)  # needs to be converted to a dictionary before turned into json
    else:
        return jsonify({"success": False, "message": "Username and/or text is missing."})


def get_service_account():
    return json.dumps({
        "type": "service_account",
        "project_id": "bitter-web-app",
        "private_key_id": "d2bef07bb7bcc6179aef30d1a8edc6ba91a0b5d1",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZIoxSI8i78x67\n6fRgZLQ952i5NtDCxRembwbII5R8Xg4M/jsTfIplKtRGpeuKWkIPeFWzpSzg9/Qr\nOVrG41IEGr/1dMT0w4LkTMQl2Jr8Ban7KYUKcikXb0RTtfO3fbz1DMspoVB2VgdA\nrGwXDwW8eqGCS5YUQaT9m5cSu9BNPlahs24sZYpOniPp7RoZIH9N/YCB6+uVOq31\nuMk18v4ZwnMqHlEtzuZkYPfdYWRjgaflINUG82W5nUYIqJQLxfQYrOz132J3hDOP\nc9Xn28T32GpeUS53AacCd+aDS6uXZ8fPJ0kgJMuDWNUDoNN85Bovz+EJv8Q11PIe\n2khDpFZzAgMBAAECggEAZk/tn4yl+s3RhwjzsfHxrhOamF84WfYlsTIyl16QilOF\nOmEWtBVkXswiDxICXQQviXuRol7ruSuMvUs+t2WIkU+LcNyvK4fuZqW3bP/V83e1\nwxeqzSPCsfynTOx45NaWET+QgVK2B7R8oWA9ZFYbRVbhQHReSLgvxqIoOtcNjT86\ngnaptYl2kxJhVD8Xrpuyku9TBCJD9hGyvIktc5uLXNTN8VnKJybU9zGCbL3Jy5vB\n38vPHybplVBw/4rB/qAn8so5XNrrWYmUbCN7nGwYvknyA+XcH0YqfDC/dunAPU6e\nEFIcvymp4MDMbgF8etEbEjRkZpZYildg0aEL8S3ZWQKBgQD3LApruFY7ZmkkajhP\nyk90/8C6ESA/QqA3asEEk/LXbaMVPW4HLbwwPUobolKksoQBprE5+nmSPeyloLb2\n6PLrZlpaC3nN2pbb42ACzSnuGTiYBp/55svMIFphNcupM1BDMjXyR0d9k5FuuXDE\nh3Qp4co4RgRBI9Hhm3l5Rl8ZSwKBgQDg497V05ajRBovTm1EyYF3i9h1QKyAemX2\nxmyx3sEJBR1RJfqiShyEhSb4kFwzwKVl6sJVHDwkarDo9d75MHwstohO/IyzDedz\n5uu5Rfqz/pStZjzzNkPxFtrAaMStr+0PzqLED82dgDTI7iPieNM5nXDZLKDSOu+z\nq0ZmbOjmeQKBgQDucd8PsgIGRbKSvaHbX4ktjnhnR5Q7UtPrAiJ4fx2bM5pLKDrX\n1Agi5U1zwTFGzyxHx35bN0ZGjVSZJ6S6J1oJO3FYQo/bxc8ZC42YxkF3/364MlPs\nKflaz69A7jut2+HHIU4njxnpjA2VqnGeNiobKUYC6ZC7Ioobwff6xaeCZwKBgDqA\n7SJhNenpOIqf82sWpLiNx9TQ609NCCOHgRVQppULIJJQt//qGbsbzISTQXkxH5YA\n2Wc8viSXIMip1cSrqVIUdideKdgWwOR06VO8cbjLfLATTb3Tmx8n2+Z8GtY4Uwpu\nrgclOU9E3/Z5hRpQZlqxq37Dzl6CeIMcBmd04625AoGBAKHP5UWH18bUhyzafYtW\n6SBe4mwbfdW+9qWKFgeMY5mZ9cOBw/9r/jlmjMi+B7O0aj5WUyuTgv7W2UxQ1hmK\nv0scHE5J4DucWx63xaqRPw2dsMcK9m/nHtruZAp686+iswRZFTAL09+G0YBJwfJz\nkdEqGHk6O/YAiA667fQdoTwr\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-0opoj@bitter-web-app.iam.gserviceaccount.com",
        "client_id": "100188799446942711736",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-0opoj%40bitter-web-app.iam.gserviceaccount.com"
    })

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

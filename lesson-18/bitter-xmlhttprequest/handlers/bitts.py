from flask import Blueprint, request, render_template
from models.bitt import Bitt
from bson.json_util import dumps

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
        return dumps({"success": True, "synced": True})
    else:
        # get all bitts from db
        bitts = Bitt.get_all_bitts()

        if not bitts:
            print("No bitts yet")

        return dumps(bitts)


@bitt_handlers.route("/create-bitt", methods=["POST"])
def bitt_create():
    username = request.json.get("username")
    text = request.json.get("text")

    if username and text:
        bitt = Bitt(text=text, username=username)
        bitt.insert()

        return dumps(bitt.__dict__)  # needs to be converted to a dictionary before turned into json
    else:
        return dumps({"success": False, "message": "Username and/or text is missing."})

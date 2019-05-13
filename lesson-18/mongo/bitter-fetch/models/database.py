import os
from smartninja_mongo.connection import MongoClient


# get DB client
mongo_uri = os.getenv("MONGODB_URI", "localhost")  # Find MONGODB_URI env var (Heroku). If not found, use "localhost"
client = MongoClient(mongo_uri)

# get DB name
if mongo_uri != "localhost":  # if app is on Heroku, get db name from MONGODB_URI
    uri_parts = mongo_uri.split(":")
    db_name = uri_parts[1].replace("//", "")
else:
    db_name = "localdb"

mongo_db = client[db_name]

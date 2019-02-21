import os
from smartninja_mongo.connection import MongoClient


def get_db():
    client = MongoClient(os.getenv("MONGODB_URI", "localhost"))  # Find MONGODB_URI env var (Heroku). If not found, use "localhost"
    db = client.my_database  # change the database name when you deploy on Heroku

    return db

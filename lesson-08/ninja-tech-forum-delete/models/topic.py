import datetime
import os
from smartninja_mongo.connection import MongoClient
from smartninja_mongo.odm import Model

client = MongoClient(os.getenv("MONGODB_URI", "localhost"))  # Find MONGODB_URI env var (Heroku). If not found, use "localhost"
db = client.my_database  # change the database name when you deploy on Heroku
collection = db.topics


class Topic(Model):
    def __init__(self, title, author_id, text, author_username, **kwargs):
        self.title = title
        self.author_id = author_id
        self.author_username = author_username
        self.text = text
        self.created = datetime.datetime.now()

        # data validation
        if type(self.title) is not str:
            raise TypeError("Topic title must be a string!")

        if type(self.text) is not str:
            raise TypeError("Topic text must be a string!")

        super().__init__(**kwargs)

    def insert(self):
        topic_id = collection.insert_one(self.__dict__).inserted_id
        self._id = topic_id  # save id from MongoDB into the Topic object

        return topic_id

    @classmethod
    def get_all_topics(cls):
        topics = collection.find()

        # IMPORTANT: this returns a list of topic dictionaries, not objects
        # If you want to have a list of objects, you'll need to convert dicts into objects:
        # topic_objects = []
        # for topic in topics:
        #     topic_objects.append(cls.convert_dict_to_object(data_dict=topic))
        # return topic_objects

        return topics

    @classmethod
    def get_by_id(cls, topic_id):
        topic_dict = collection.find_one({"_id": topic_id})

        # convert topic dictionary into topic object
        topic_obj = cls.convert_dict_to_object(data_dict=topic_dict)

        return topic_obj

    @classmethod
    def edit_topic(cls, topic_id, updates_dict):
        result = collection.update_one({"_id": topic_id}, {"$set": updates_dict})

        return result

    @classmethod
    def delete_topic(cls, topic_id):
        result = collection.delete_one({"_id": topic_id})

        return result

import datetime
from smartninja_mongo.odm import Model
from smartninja_mongo.bson import ObjectId
from models.database import mongo_db


collection = mongo_db.comments


class Comment(Model):
    def __init__(self, topic_id, author_id, text, author_username, **kwargs):
        self.topic_id = topic_id
        self.author_id = author_id
        self.author_username = author_username
        self.text = text
        self.created = datetime.datetime.now()

        super().__init__(**kwargs)

    def insert(self):
        comment_id = collection.insert_one(self.__dict__).inserted_id
        self._id = comment_id  # save id from MongoDB into the Topic object

        return comment_id

    @classmethod
    def get_comments(cls, topic_id):
        comment_dicts = collection.find({"topic_id": topic_id})  # we don't use ObjectId() because we didn't save topic_id like this

        """
        # Uncomment this if you want to convert dicts into objects
        comments = []
        for comm_dict in comment_dicts:
            comments.append(cls.convert_dict_to_object(data_dict=comm_dict))
        """

        return comment_dicts

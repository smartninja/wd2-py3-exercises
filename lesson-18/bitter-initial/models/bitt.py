import datetime
from smartninja_mongo.odm import Model
from models.database import mongo_db


collection = mongo_db.bitts


class Bitt(Model):
    def __init__(self, text, author_username, **kwargs):
        self.author_username = author_username
        self.text = text
        self.created = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        if type(self.text) is not str:
            raise TypeError("Bitt text must be a string!")

        super().__init__(**kwargs)

    def insert(self):
        bitt_id = collection.insert_one(self.__dict__).inserted_id
        self._id = bitt_id  # save id from MongoDB into the Bitt object

        return bitt_id

    @classmethod
    def get_all_bitts(cls):
        bitts = collection.find()

        # some pre-made bitts (you can delete them)
        bitts_dicts = [
            {
                "_id": "1e4eabc8654211e99e4eacbc329afba7",
                "author_username": "Bittman",
                "created": "2019-04-19T07:32:09",
                "text": "I'm fine. Thanks for not asking."
            },
            {
                "_id": "9125e4ea654211e99e4eacbc329afba7",
                "author_username": "bossbabe",
                "created": "2019-04-21T22:05:12",
                "text": "Sometimes you have to unfollow people in real life."
            },
            {
                "_id": "6e38adc2654311e99e4eacbc329afba7",
                "author_username": "karmalicious",
                "created": "2019-04-22T18:40:45",
                "text": "I hope karma slaps you in the face before I do."
            },
        ]

        for bitt in bitts:
            bitts_dicts.append(dict(bitt))  # convert bitts from a document type into a dictionary

        return bitts_dicts

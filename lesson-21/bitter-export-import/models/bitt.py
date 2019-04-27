import datetime
import os

from smartninja_mongo.odm import Model
from models.database import mongo_db
import smartninja_redis


collection = mongo_db.bitts
redis = smartninja_redis.from_url(os.environ.get("REDIS_URL"))


class Bitt(Model):
    def __init__(self, text, username, **kwargs):
        self.username = username
        self.text = text
        self.created = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        if type(self.text) is not str:
            raise TypeError("Bitt text must be a string!")

        super().__init__(**kwargs)

    def insert(self):
        bitt_id = collection.insert_one(self.__dict__).inserted_id
        self._id = bitt_id  # save id from MongoDB into the Bitt object
        self.id = str(bitt_id)  # convert Mongo's ObjectId to string

        # save ID into Redis (last Bitt ID)
        redis.set(name="last-bitt-id", value=str(bitt_id))

        return bitt_id

    @classmethod
    def get_all_bitts(cls):
        bitts = collection.find()

        # some pre-made bitts (you can delete them)
        bitts_dicts = [
            {
                "id": "1e4eabc8654211e99e4eacbc329afba7",
                "username": "Bittman",
                "created": "2019-04-19T07:32:09",
                "text": "I'm fine. Thanks for not asking."
            },
            {
                "id": "9125e4ea654211e99e4eacbc329afba7",
                "username": "bossbabe",
                "created": "2019-04-21T22:05:12",
                "text": "Sometimes you have to unfollow people in real life."
            },
            {
                "id": "6e38adc2654311e99e4eacbc329afba7",
                "username": "karmalicious",
                "created": "2019-04-22T18:40:45",
                "text": "I hope karma slaps you in the face before I do."
            },
        ]

        for bitt in bitts:
            bitt_dict = dict(bitt)

            try:
                bitt_dict["id"] = str(bitt["_id"])  # convert Mongo's ObjectId to string
            except Exception as e:
                print("Error _id to id: {}".format(e))

            bitts_dicts.append(dict(bitt_dict))  # convert bitts from a document type into a dictionary

        # sort by date created (reverse order)
        bitts_dicts.sort(key=lambda x: datetime.datetime.strptime(x['created'], '%Y-%m-%dT%H:%M:%S'), reverse=True)

        return bitts_dicts

    @classmethod
    def get_last_bitt_id(cls):
        last_bitt_id = redis.get(name="last-bitt-id")

        if last_bitt_id:
            last_bitt_id = last_bitt_id.decode()
        else:
            last_bitt = cls.get_all_bitts()[0]
            last_bitt_id = last_bitt["id"]
            redis.set(name="last-bitt-id", value=last_bitt_id)

        return last_bitt_id

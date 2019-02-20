from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(host="mongo", username="root", password="example")

# create a database (or find an existing one)
db = client.my_first_database

# create a collection (or find an existing one)
collection = db.users

# insert new document
user_id = collection.insert_one({"first_name": "Matej", "last_name": "Ramuta", "year_born": 1987}).inserted_id

print(user_id)
print(type(user_id))  # user_id is not a string, but an ObjectId

# find a document (using user_id as an ObjectId)
print("Using ID as ObjectId")
user_info = collection.find_one({"_id": user_id})
print(user_info)

# find a document (using user_id_str as a string)
print("Using ID as string")
user_id_str = str(user_id)
user_info_2 = collection.find_one({"_id": user_id_str})  # result is None
print(user_info_2)  # None, because id string needs to be an ObjectId

# user_id_str string needs to be converted to ObjectId
print("converting ID string to ObjectId")
user_id_obj = ObjectId(user_id_str)
user_info_3 = collection.find_one({"_id": user_id_obj})
print(user_info_3)

# find many documents
print("Many users:")
many_users = collection.find({"first_name": "Matej"})

for user in many_users:
    print(user)

# update a document
collection.update_one({"_id": user_id}, {"$set": {"first_name": "Miha"}})
user_info = collection.find_one({"_id": user_id})
print("Updated user: ")
print(user_info)

# delete a document
collection.delete_one({"_id": user_id})

# let's try to find the deleted object:
user_info = collection.find_one({"_id": user_id})

print("Deleted user: ")
print(user_info)  # should return None

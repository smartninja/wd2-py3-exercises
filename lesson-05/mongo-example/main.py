from smartninja_mongo.connection import MongoClient

# connect client
client = MongoClient(host="localhost")

# create a database (or find an existing one)
db = client.my_first_database

# create a collection (or find an existing one)
collection = db.users

# insert new document
user_id = collection.insert_one({"first_name": "Matej", "last_name": "Ramuta", "year_born": 1987}).inserted_id

print(user_id)

# find a document
user_info = collection.find_one({"_id": user_id})

print(user_info)

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

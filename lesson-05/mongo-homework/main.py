from smartninja_mongo.connection import MongoClient

# connect client
client = MongoClient(host="localhost")

# create a database (or find an existing one)
db = client.my_first_database

# create a collection (or find an existing one)
collection = db.users

# insert new documents
user_id_1 = collection.insert_one({"first_name": "Matt", "last_name": "Ramuta", "year_born": 1987}).inserted_id
user_id_2 = collection.insert_one({"first_name": "Alina", "last_name": "Toppler", "year_born": 1991}).inserted_id
user_id_3 = collection.insert_one({"first_name": "Bob", "last_name": "Marley", "year_born": 1945}).inserted_id

print(user_id_1)
print(type(user_id_1))  # user ids are not a string, but an ObjectId

many_users = collection.find()

print("Unsorted users:")
for user in many_users:
    print(user)

# sort results based on the first_name
sorted_users = collection.find(sort=[("first_name", "1")])

print("Sorted users by first name:")
for user in sorted_users:
    print(user)

# limit number of results to 2
sorted_users = collection.find(sort=[("first_name", "1")], limit=2)

print("Limited number of users:")
for user in sorted_users:
    print(user)

# find all users with year_born older than 1990
sorted_users = collection.find({"year_born": {"$lt": 1990}}, sort=[("first_name", "1")])

print("Users born before 1990:")
for user in sorted_users:
    print(user)

# add a new field to every user
collection.update({}, {"$set": {"active": True}})

print("Updated users with a new field:")
many_users = collection.find()
for user in many_users:
    print(user)

# count the number of all users in the collection
print(collection.find().count())

# final cleanup
collection.delete_many({})

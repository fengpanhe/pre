import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client.pre

collection = db['user_installedapps']

for user in collection.find({"userId":1}):
    print(user)

import pymongo

client = pymongo.MongoClient('120.24.223.44', 27017)

db = client['pre']

collection = db['user_installedapps']

for user in collection.find({"userId":'1'}):
    print(user)

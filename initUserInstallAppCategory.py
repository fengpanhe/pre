import pymongo
from preDb import preDb

pre_db = preDb()
train_size = pre_db.db.train.count()
for i in range(train_size):
    instance = pre_db.db.train.find().limit(1).skip(i)[0]
    user_id = instance["userID"]
    pre_db.get_user_installedappsCategory(user_id)

test_size = pre_db.db.test.count()
for i in range(test_size):
    instance = pre_db.db.test.find().limit(1).skip(i)[0]
    user_id = instance["userID"]
    pre_db.get_user_installedappsCategory(user_id)
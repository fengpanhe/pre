import pymongo
from preDb import preDb

pre_db = preDb()
train_size = pre_db.db.train.count()
for i in range(train_size):
    instance = pre_db.db.train.find().limit(1).skip(i)[0]
    user_id = instance["userID"]
    category = pre_db.get_user_installedappsCategory(user_id)
    print(category)
    print("userID: " + str(user_id) + '  rate_sum: ' + str(sum(category)))
    print("train: " + str(train_size) + ' | ' + str(i))

test_size = pre_db.db.test.count()
for i in range(test_size):
    instance = pre_db.db.test.find().limit(1).skip(i)[0]
    user_id = instance["userID"]
    category = pre_db.get_user_installedappsCategory(user_id)
    print(category)
    print("userID: " + str(user_id) + '  rate_sum: ' + str(sum(category)))
    print("test: " + str(test_size) + ' | ' + str(i))

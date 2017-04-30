import pymongo

class preDb(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client.pre

        # self.ad_collection = db.ad
        # self.user_installed_app_collection = db.user_installedapps
        # self.position_collection = db.position
        # self.app_categories_collection = db.app_categories
        # self.user_collection = db.user
        # self.user_app_actions_collection = db.user_app_actions
        # self.test_collection = db.test
        # self.train_collection = db.train

        self.app_categories = []
    
    def app_categories(self):
        app_categories = []
        for line in self.db.app_categories.find():
            if not line["appCategory"] in app_categories:
                app_categories.append(line["appCategory"])
        self.app_categories = app_categories.copy()

    def get_a_train_instance(self,index):
        
        instance = self.db.train.find().limit(1).skip(index)

        ad = self.db.ad.find({"creativeID":instance['creativeID']})
        instance["adID"] = ad["adID"]
        instance["camgaignID"] = ad["camgaignID"]
        instance["advertiserID"] = ad["advertiserID"]
        instance["appID"] = ad["appID"]
        instance["appPlatform"] = ad["appPlatform"]

        user = self.db.user.find({"userID":instance['userID']})
        instance["age"] = user["age"] 
        instance["gender"] = user["gender"] 
        instance["education"] = user["education"] 
        instance["marriageStatus"] = user["marriageStatus"] 
        instance["haveBaby"] = user["haveBaby"] 
        instance["hometown"] = user["hometown"] 
        instance["residence"] = user["residence"]
        
        position = self.db.position.find({"positionID":instance['positionID']})
        instance["positionID"] = position["positionID"] 
        instance["sitesetID"] = position["sitesetID"] 
        instance["positionType"] = position["positionType"]

        installed_app_list = []
        for line in self.db.user_installedapps.find({"userID":user_id}):
            installed_app_list.append(line('appID'))

        for app_id in installed_app_list:
            app_categories_id = 'installedAppCategories' + str(self.db.app_categories.find({"appID":app_id}))
            if app_categories_id in instance:
                instance[app_categories_id] += 1
            else:
                instance[app_categories_id] = 1
        
        for categories in self.app_categories:
            categories_id = 'installedAppCategories' + str(categories)
            if categories_id in instance:
                instance[categories_id] /= len(installed_app_list)
            else:
                instance[categories_id] = 0
        
        return instance

pre_db = pre_db()
pre_db.app_categories()
print(pre_db.get_a_train_instance(0))

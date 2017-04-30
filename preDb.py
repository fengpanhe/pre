import pymongo

class preDb(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client.pre
        
        self.app_categories = [2, 203, 104, 402, 301, 407, 101, 408, 106, 0, 201, 409, 503, 210, 108, 211, 1, 110, 405, 401, 109, 103, 209, 406, 303, 403, 105, 204]
        self.calc_app_categories()
    
    def calc_app_categories(self):
        app_categories = []
        for line in self.db.app_categories.find():
            if not line["appCategory"] in app_categories:
                app_categories.append(line["appCategory"])
        self.app_categories = app_categories.copy()
        print(self.app_categories)

    def get_user_installedappsCategory(self,user_id):
        find_result = self.db.user_installedappsCategory.find({"userID":user_id})
        if not find_result.count() == 0:
            return find_result[0]["appsCategory"]
        
        installed_app_list = []
        for line in self.db.user_installedapps.find({"userID":user_id}):
            installed_app_list.append(line['appID'])

        app_category_id_dict = {}
        for app_id in installed_app_list:
            app_category_id = self.db.app_categories.find({"appID":app_id})[0]['appCategory']
            if app_category_id in app_category_id_dict:
                app_category_id_dict[app_category_id] += 1
            else:
                app_category_id_dict[app_category_id] = 1
        
        installedappsCategory_rate = []
        for category_id in self.app_categories:
            if category_id in app_category_id_dict:
                installedappsCategory_rate.append(app_category_id_dict[category_id] / len(installed_app_list))
            else:
                installedappsCategory_rate.append(0)
        
        self.db.user_installedappsCategory.insert(
            {
                "userID":user_id,
                "appsCategory":installedappsCategory_rate
            }
        )
        return installedappsCategory_rate



    def get_a_train_instance(self,index):
        
        instance = self.db.train.find().limit(1).skip(index)[0]
        print(str(instance))
        ad = self.db.ad.find({"creativeID":instance["creativeID"]})[0]
        instance["adID"] = ad["adID"]
        instance["camgaignID"] = ad["camgaignID"]
        instance["advertiserID"] = ad["advertiserID"]
        instance["appID"] = ad["appID"]
        instance["appPlatform"] = ad["appPlatform"]

        user = self.db.user.find({"userID":instance['userID']})[0]
        instance["age"] = user["age"] 
        instance["gender"] = user["gender"] 
        instance["education"] = user["education"] 
        instance["marriageStatus"] = user["marriageStatus"] 
        instance["haveBaby"] = user["haveBaby"] 
        instance["hometown"] = user["hometown"] 
        instance["residence"] = user["residence"]
        
        position = self.db.position.find({"positionID":instance['positionID']})[0]
        instance["positionID"] = position["positionID"] 
        instance["sitesetID"] = position["sitesetID"] 
        instance["positionType"] = position["positionType"]

        installedappsCategory_rate = self.get_user_installedappsCategory(instance['userID'])
        instance["appsCategory"] = installedappsCategory_rate
        installed_app_list = []
        
        return instance

pre_db = preDb()
print(pre_db.get_user_installedappsCategory(2798058))
# print(pre_db.get_a_train_instance(0)

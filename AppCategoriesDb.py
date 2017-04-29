import pymongo

class AppCategoriesDb(object):

    def __init__(self,db):
        self.collection = db.app_categories

    def get_app_categories(self,app_id):
        return self.collection.find_one({"appID":app_id})['appCategory']
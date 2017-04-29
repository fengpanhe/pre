import pymongo


class UserInstalledappsDb(object):

    def __init__(self,db):
        self.collection = db.user_installedapps

    def get_install_app_list(self,user_id):
        app_list = []
        for line in self.collection.find({"userID":user_id}):
            app_list.append(line['appID'])
        return app_list

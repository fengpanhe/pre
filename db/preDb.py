import pymongo
import numpy as np


class preDb(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017, connect=False)
        self.db = client.pre

        self.app_categories = [
            2, 203, 104, 402, 301, 407, 101, 408, 106, 0, 201, 409, 503, 210,
            108, 211, 1, 110, 405, 401, 109, 103, 209, 406, 303, 403, 105, 204
        ]
        # self.calc_app_categories()

    def calc_app_categories(self):
        app_categories = []
        for line in self.db.app_categories.find():
            if not line["appCategory"] in app_categories:
                app_categories.append(line["appCategory"])
        self.app_categories = app_categories.copy()
        print(self.app_categories)

    def get_user_installedappsCategory(self, user_id):
        '''
        得到用户的 app 安装列表的 app 分类占比和安装的app数量，app类别28类
        '''
        find_result = self.db.user_installedappsCategory.find_one({
            "userID": user_id
        })
        if find_result is not None:
            return {
                "appsCategory": find_result["appsCategory"],
                "appNum": find_result['InstalledAppNum']
            }

        installed_app_list = []
        for line in self.db.user_installedapps.find({"userID": user_id}):
            installed_app_list.append(line['appID'])

        app_category_id_dict = {}
        for app_id in installed_app_list:
            app_category_id = self.db.app_categories.find({
                "appID": app_id
            })[0]['appCategory']
            if app_category_id in app_category_id_dict:
                app_category_id_dict[app_category_id] += 1
            else:
                app_category_id_dict[app_category_id] = 1

        installedappsCategory_rate = []
        for category_id in self.app_categories:
            if category_id in app_category_id_dict:
                installedappsCategory_rate.append(
                    app_category_id_dict[category_id] /
                    len(installed_app_list))
            else:
                installedappsCategory_rate.append(0)

        installed_app_num = len(installed_app_list)

        self.db.user_installedappsCategory.insert({
            "userID":
            user_id,
            "appsCategory":
            installedappsCategory_rate,
            "InstalledAppNum":
            installed_app_num
        })
        return {
            "appsCategory": installedappsCategory_rate,
            "appNum": installed_app_num
        }

    def get_user_app_actions(self, user_id):
        '''
        得到用户的 app 操作行为的 app 分类次数，app类别28类
        '''

    def get_a_train_instance(self, index):
        '''
        得到一条训练条目的输入数据和结果
        '''

        # 先在train_instance查找，有则直接返回
        find_result = self.db.train_instance.find_one({"index": index})
        if find_result is not None:
            return {
                'input_val': find_result["input_val"],
                'correct_result': find_result["correct_result"]
            }

        instance = self.db.train.find().limit(1).skip(index)[0]
        print(str(instance))

        input_val = []

        input_val.append(instance["connectionType"])
        input_val.append(instance["telecomsOperator"])

        ad = self.db.ad.find_one({"creativeID": instance["creativeID"]})
        if ad is not None:
            input_val.append(ad["adID"])
            input_val.append(ad["camgaignID"])
            input_val.append(ad["advertiserID"])
            input_val.append(ad["appID"])
            app_category = self.db.app_categories.find_one({
                "appID": ad["appID"]
            })
            if app_category is not None:
                input_val.append(app_category['appCategory'])
            else:
                input_val.append(0)
            input_val.append(ad["appPlatform"])
        else:
            for i in range(6):
                input_val.append(0)
        # instance["adID"] = ad["adID"]
        # instance["camgaignID"] = ad["camgaignID"]
        # instance["advertiserID"] = ad["advertiserID"]
        # instance["appID"] = ad["appID"]
        # instance["appPlatform"] = ad["appPlatform"]

        user = self.db.user.find_one({"userID": instance['userID']})
        if user is not None:
            input_val.append(user["age"])
            input_val.append(user["gender"])
            input_val.append(user["education"])
            input_val.append(user["marriageStatus"])
            input_val.append(user["haveBaby"])
            input_val.append(user["hometown"])
            input_val.append(user["residence"])
        else:
            for i in range(7):
                input_val.append(0)
        # instance["age"] = user["age"]
        # instance["gender"] = user["gender"]
        # instance["education"] = user["education"]
        # instance["marriageStatus"] = user["marriageStatus"]
        # instance["haveBaby"] = user["haveBaby"]
        # instance["hometown"] = user["hometown"]
        # instance["residence"] = user["residence"]

        position = self.db.position.find_one({
            "positionID": instance['positionID']
        })
        if position is not None:
            input_val.append(position["positionID"])
            input_val.append(position["sitesetID"])
            input_val.append(position["positionType"])
        else:
            for i in range(3):
                input_val.append(0)
        # instance["positionID"] = position["positionID"]
        # instance["sitesetID"] = position["sitesetID"]
        # instance["positionType"] = position["positionType"]

        # TODO：安装列表时间的处理。

        installedappsCategory = self.get_user_installedappsCategory(
            instance['userID'])
        for category_rate in installedappsCategory["appsCategory"]:
            input_val.append(category_rate)

        correct_result = 0.1
        if instance["label"] == 1 and instance["conversionTime"] / 10000 == instance["clickTime"] / 10000:
            correct_result = 0.9

        self.db.train_instance.insert({
            "index": index,
            'input_val': input_val,
            'correct_result': correct_result
        })
        return {
            'input_val': input_val,
            'correct_result': correct_result
        }

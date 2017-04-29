import pymongo

class AdDb(object):
    def __init__(self,db):
        self.collection = db.ad

    def get_creative_list(self,creative_id):
        creative_list = []
        for line in self.collection.find({"creativeID":creative_id}):
            creative_list.append(line)
        return creative_list
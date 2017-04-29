import pymongo

class PositionDb(object):

    def __init__(self,db):
        self.collection = db.position
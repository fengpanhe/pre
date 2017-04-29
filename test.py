import pymongo

from AdDb import AdDb
from UserInstalledappsDb import UserInstalledappsDb

client = pymongo.MongoClient('localhost', 27017)

db = client.pre

user_installed_app_db = UserInstalledappsDb(db)

print(user_installed_app_db.get_install_app_list(1))
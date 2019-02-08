import pprint

from pymongo import MongoClient
client = MongoClient()

db = client.OpdrachtSP

products = db.products
profiles = db.profiles
sessions = db.sessions


pprint.pprint(products.find_one())


for x in products.find({},{"name": "R%"}):
    print(x)

for x in products.find({},{"price": 1}):
    print(x)
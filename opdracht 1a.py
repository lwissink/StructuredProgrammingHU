import pprint

import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.OpdrachtSP

products = db.products
profiles = db.profiles
sessions = db.sessions

def nameandprice():
    for product in products.find():
        print(product['name'], (product['price']['selling_price'])/100, 'euro')
        break

def r_as_first_letter():
    for product in products.find():
        if 'R' == product['name'][0]:
            print(product['name'])
            break

def averageprice():
    prijzen = []
    for product in products.find():
        prijzen.append(int(product['price']['selling_price']))
    print(sum(prijzen)/len(prijzen))

nameandprice()
r_as_first_letter()
averageprice()

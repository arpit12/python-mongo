# use the following command step by step in terminal
import pymongo
 
#get Client
client = pymongo.MongoClient("localhost", 27017)
 
#show all mongo document databases
print client.database_names()

connection = pymongo.Connection()

db = connection["tutorial"]
employees = db["employees"]

cursor = db.employees.find()
for employee in db.employees.find():
        print employee

#remove all documents in current collection 
employees.remove()
# print all item in test collection 
for item in employees.find():
        print item

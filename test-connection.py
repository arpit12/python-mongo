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


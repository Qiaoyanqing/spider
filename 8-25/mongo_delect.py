import pymongo

client = pymongo.MongoClient(host="127.0.0.1",port=27017)

db = client["books"]
collection = db["books"]

res = collection.delete_many()

print(res)
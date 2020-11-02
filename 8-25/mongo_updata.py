import pymongo

client = pymongo.MongoClient(host="127.0.0.1",port=27017)

db = client["spider_practice"]
collection = db["students"]

student = collection.find_one({'ID':'1'})
student['Age'] = '32'
result = collection.update({'ID':'1'},student)
print(result)
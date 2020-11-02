import pymongo

# client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient(host="127.0.0.1",port=27017)
db = client["spider_practice"]
collection = db["students"]

result1 = collection.find_one({'ID':'2'})# 查找一个
# print(result1)

# 属性相同的时候，find_one只输出第一个
result2 = collection.find_one({'Age':'18'})
print(result2)
# 输出多个
result3 = collection.find({'Age':'18'})
for res in result3:
    # print(res)
    pass

# 计数
count = collection.count_documents({'Age':'18'})
print(count)

# 排序 pymongo.ASCENDING升序    pymongo.DESCENDING 降序
paixu = collection.find().sort('ID',pymongo.DESCENDING)

print([res_paixu['ID'] for res_paixu in paixu])

# 偏移
pianyi = collection.find().sort('ID',pymongo.DESCENDING).skip(2)
print(print([res_pianyi['ID'] for res_pianyi in pianyi]))
# 数据量大的时候，不要使用大数据偏移量，很容易导致内存溢出,这个时候要查询时尽量使用条件查询
from bson.objectid import  ObjectId
res03 = collection.find({"_id":{"$gt":ObjectId("5f4475c1b78b94ae55df4f1a")}})
print([res["name"] for res in res03])
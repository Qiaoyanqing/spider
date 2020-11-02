'''
mongo数据库的链接
'''

import pymongo
# 创建链接对象
# 方法一
client = pymongo.MongoClient(host="127.0.0.1",port=27017)# host = "localhost" port端口号
# 方法二
# client = pymongo.MongoClient("mongodb://localhost:27017")

# 指定链接数据库
# db = client.spider_practice
db = client["spider_practice"]# 链接到数据库spider_practice
# collection = db.students
collection = db["students"]# 链接到数据库下的students表


# 插入数据
student = {
    'ID':'101010',
    'Name':'鳗鲡湖之王',
    'Age':'18',
    'Gender':'male'
}

result = collection.insert_one(student)# 插入一个
# 运行成功会返回数据库ID（object）
print(result)

student1 = {
    'ID':'1',
    'Name':'泰达米尔',
    'Age':'18',
    'Gender':'male'
}
student2 = {
    'ID':'2',
    'Name':'赵信',
    'Age':'18',
    'Gender':'male'
}
student3 = {
    'ID':'3',
    'Name':'易大师',
    'Age':'18',
    'Gender':'male'
}
student4 = {
    'ID':'4',
    'Name':'嘉文',
    'Age':'18',
    'Gender':'male'
}
student5 = {
    'ID':'5',
    'Name':'盖伦',
    'Age':'18',
    'Gender':'male'
}

results = collection.insert_many([student1,student2,student3,student4,student5])# 插入多个
print(results)
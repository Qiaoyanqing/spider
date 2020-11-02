from pyquery import PyQuery
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>demo</title>
</head>
<body>
	<div id="container">
		<ul class="list">
			<li class="item-0">first line</li>
			<li class="item-1">second line</li>
			<li class="item-0 active"><a href="http://httpbin.org">third line</a></li>
			<li class="item-1 active"><a href="http://www.baidu.com/"><span class="des">fourth line</span></a></li>
			<h1>demo</h1>
		</ul>
	</div>
</body>
</html>
'''

# 构造对象
doc = PyQuery(html)
print(doc)
print(type(doc))
print(doc("li"))
print(type(doc("li")))

# url初始化
doc2 = PyQuery(url="http://www.baidu.com/")
print(doc2("title"))

# 以上写法等价于
import requests

doc2 = PyQuery(requests.get(url="http://www.baidu.com/").text)
print(doc2("title"))

# 文件初始化
doc3 = PyQuery(filename="demo.html")
print(doc3)
print(doc3("li"))

doc4 = PyQuery(html)
# 通过container选中id属性为container的代码块   .list选中class属性值为list的代码块
print(doc4("#container .list li"))

li = PyQuery(html)
for i in doc4("#container .list li").items():
    print(li)
    print(type(li))
    print(li.text())

# 寻找子节点
doc = PyQuery(html)
items = doc(".list")
print(items)
print(type(items))
print('-'*50)
lis = items.find("li") # 在items中利用find方法找到所有的li标签
print(lis)
print(type(lis))
print('-'*50)
children = items.children(".item-0")# 携带过滤
print(children)

# 寻找父节点
doc = PyQuery(html)
items = doc(".list")
print(items)
parent = items.parent()
print(parent)

# 寻找祖父节点
html2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>demo</title>
</head>
<body>
	<div id="container">
		<ul class="list">
			<li class="item-0">first line</li>
			<li class="item-1">second line</li>
			<li class="item-0 active"><a href="http://httpbin.org">third line</a></li>
			<li class="item-1 active"><a href="http://www.baidu.com/"><span class="des">fourth line</span></a></li>
			<h1>demo</h1>
		</ul>
	</div>
	<div id="container2">
		<ul class="list2">
			<li class="item-20">first line</li>
			<li class="item-21">second line</li>
			<li class="item-20 active"><a href="http://httpbin.org">third line</a></li>
			<li class="item-21 active"><a href="http://www.baidu.com/"><span class="des">fourth line</span></a></li>
			<h1>demo</h1>
		</ul>
	</div>
</body>
</html>
'''

doc = PyQuery(html2)
items = doc(".list2")
parents = items.parents("#container2")# 获取祖父节点
# daye = parents.find("#container2")

print(parents)

li = doc(".item-0 .active")
brother = li.siblings()# 获取兄弟节点
print(brother)

# 遍历
lis = doc("li")
for li in lis.items():
    print(li.text())


# CSS属性获取 attr方法
doc = PyQuery(html2)

a = doc(".item-0.active a")
href = a.attr("href")#方法一
href2 = a.attr.href#方法二
print(a)
print(href)
print(href2)
print('--'*50)
items = doc("a")
for item in items.items():
    print(item.attr("href"))

# text拿文本
doc = PyQuery(html)

a = doc(".item-0.active a")
print(type(a.html()))
print(a.html())
print(type(a.text()))
print(a.text())
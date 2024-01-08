# 字典清單的混用

p0 = {
	'name': '鉛筆',
	'price': 10
}

p1 = {
	'name': '鋼筆',
	'price': 300
}

pens = [p0, p1] # 清單中裝著字典
print(pens[0]['name']) # 鉛筆
print(pens[1]['price']) # 300
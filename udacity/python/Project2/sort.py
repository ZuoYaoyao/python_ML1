import operator
x = {'china':2, 3:4, 4:3, 2:1, 0:0}
x['china'] += 1
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

print(sorted_x)


location = {'大陆': 0, '美国': 0, '香港': 0, '台湾': 0, '日本': 0, '韩国': 0,
            '英国': 0, '法国': 0, '德国': 0, '意大利': 0, '西班牙': 0,
            '印度': 0, '泰国': 0, '俄罗斯': 0, '伊朗': 0, '加拿大': 0,
            '澳大利亚': 0, '爱尔兰': 0, '瑞典': 0, '巴西': 0, '丹麦': 0}
three_type = [location, location, location]

three_type[0]['大陆'] += 1

for item in three_type:
    print(item)

sorted_x = sorted(location.items(), key=operator.itemgetter(1),reverse=True)
print (sorted_x[0])
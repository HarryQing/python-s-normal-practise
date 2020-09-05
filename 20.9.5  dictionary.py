#创建一个字典并输出字典中所以元素

information={
    'first_name':'wang',
    'last_name':'yong qing',
    'age':'19',
    'city':'nanchang',
    }
print(information)


#结果{'first_name': 'wang', 'last_name': 'yong qing', 'age': '19', 'city': 'nanchang'}

#添加键—值对

information['love']='flower'
print(information)

#结果{'first_name': 'wang', 'last_name': 'yong qing', 'age': '19', 'city': 'nanchang', 'love': 'flower'}

#删除键—值对

del information['love']
print(information)

#结果{'first_name': 'wang', 'last_name': 'yong qing', 'age': '19', 'city': 'nanchang'}

#修改键—值对

information['first_name']='harry'
print(information)

#结果{'first_name': 'harry', 'last_name': 'yong qing', 'age': '19', 'city': 'nanchang'}

#访问字典中的值

print(information['first_name'].title())

#结果Harry

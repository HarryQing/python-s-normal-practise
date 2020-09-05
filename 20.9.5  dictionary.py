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

#遍历所以键—值对
favorite_language={
    'jen':'python',
    'sarah':'c',
    'tom':'ruby',
    'lisa':'python',
    }
for key,value in favorite_language.items():
    print("\nkey:"+key.title())
    print("value:"+value)

"""
结果:
key:Jen
value:python

key:Sarah
value:c

key:Tom
value:ruby

key:Lisa
value:python
"""

#遍历字典中所以的键

for key in favorite_language.keys():
    print("\nkey:"+key.title())

"""
结果:
key:Jen

key:Sarah

key:Tom

key:Lisa
"""
friend=['tom']
for key in favorite_language.keys():
    print("\nkey:"+key.title())
    if key in friend:
        print("name:"+key+" love:"+favorite_language[key])

"""
结果:
key:Jen

key:Sarah

key:Tom
name:tom love:ruby

key:Lisa
"""
if 'timi' not in favorite_language.keys():
    print("nice")

#结果:nice

#按顺序遍历字典所有键
favorite_languages={
    'tom':'c',
    'lisa':'java',
    'jen':'pytjon',
    'lay':'ruby',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title())

"""
结果：
Jen
Lay
Lisa
Tom
"""
#遍历字典中的所有值
print("languages:")
for value in favorite_languages.values():
    print(value.title())

"""
结果：
languages:
C
Java
Pytjon
Ruby
"""
#字典列表

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':12}
alien_2={'color':'red','points':2}
aliens=[alien_0,alien_1,alien_2]
for all in aliens:
    print(all)

"""
结果：
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 12}
{'color': 'red', 'points': 2}
"""

aliens=[]
for i in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for i in aliens[0:3]:
    if i['color']=='green':
        i['points']=99
        i['speed']='fast'
for i in aliens[:6]:
    print(i)
print('...')
print('finish')

"""
结果：
{'color': 'green', 'points': 99, 'speed': 'fast'}
{'color': 'green', 'points': 99, 'speed': 'fast'}
{'color': 'green', 'points': 99, 'speed': 'fast'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
finish
"""
#在字典中存储列表

favorite_languages={
    'tom':['c','c++'],
    'lisa':['java','python'],
    'jen':['pytjon'],
    'lay':['ruby','http'],
    }
for name,languages in favorite_languages.items():
    print(name.title()+"`s favorite languages are :")
    for language in languages:
        print (language)

"""
结果：
Tom`s favorite languages are :
c
c++
Lisa`s favorite languages are :
java
python
Jen`s favorite languages are :
pytjon
Lay`s favorite languages are :
ruby
http
"""
#在字典中存储字典

users={
    'tom':{
        'first':'tom',
        'last':'esinsten',
        'location':'princeton',
        },
    'lisa':{
        'first':'lisa',
        'last':'esinsten',
        'location':'sanfrancisical',
        },
    }
for name,value in users.items():
    print("usernam:"+name)
    fullname=value['first'].title()+" "+value['last']
    location=value['location']
    print("\tfullname:"+fullname+"\n\tlocation:"+location)

"""
结果：
usernam:tom
	fullname:Tom esinsten
	location:princeton
usernam:lisa
	fullname:Lisa esinsten
	location:sanfrancisical
"""

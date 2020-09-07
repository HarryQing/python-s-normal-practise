#定义一个函数 
def get_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name.title()+middle_name+last_name
    else:
        full_name=first_name.title()+last_name
    return full_name
user1=get_name('wang','qing','yong')
print(user1)
user2=get_name('bralan','jaery')
print(user2)
friend={}
friend[user1]=user2
for key,value in friend.items():
    print(key+"`s frind is "+value+"!")

"""
结果：
Wangyongqing
Bralanjaery
Wangyongqing`s frind is Bralanjaery!
"""
#定义给已有字典添加键值的函数
def get_name(users,first_name,last_name):
    users[first_name]=last_name
a_users={}
get_name(a_users,'a','tom')
get_name(a_users,'b','lisa')
get_name(a_users,'c','zreak')
for key,value in a_users.items():
    print("\nfirst_name:"+key.title())
    print("last_name:"+value)
    
print("\n"+str(a_users))
    
"""
结果：
first_name:A
last_name:tom

first_name:B
last_name:lisa

first_name:C
last_name:zreak

{'a': 'tom', 'b': 'lisa', 'c': 'zreak'}
"""
#传递任意数量的实参
def make_pizza(size,*name):
    print("size:"+str(size))
    for names in name:
        print(names.title())
make_pizza(12,'a')
make_pizza(33,'a','b','c')
       
"""
结果：
size:12
A
size:33
A
B
C
"""
#使用任意数量的关键字实参
def users(first_name,last_name,**userss):
    user={}
    user['first_name']=first_name.title()
    user['last_name']=last_name.title()
    for key,value in userss.items():
        user[key]=value
    return user
user1=users('a','tom',age=12)
user2=users('b','jafk',age=14,area='beijing')
print(user1)
print(user2)

"""
结果：
{'first_name': 'A', 'last_name': 'Tom', 'age': 12}
{'first_name': 'B', 'last_name': 'Jafk', 'age': 14, 'area': 'beijing'}
"""

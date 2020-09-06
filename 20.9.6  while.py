#让用户选择何时退出
prompt="\nTll me something!"
prompt+="\nEnter 'quit' to end the program."
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)

"""
结果：
Tll me something!
Enter 'quit' to end the program.wqe
wqe

Tll me something!
Enter 'quit' to end the program.eqe
eqe

Tll me something!
Enter 'quit' to end the program.qwe
qwe

Tll me something!
Enter 'quit' to end the program.quit
"""
#使用标志
prompt="\nTll me something!"
prompt+="\nEnter 'quit' to end the program."
active=True
while active:
    message=input(prompt)
    if message!='quit':
        print(message)
    else:
        active=False

"""
结果：
Tll me something!
Enter 'quit' to end the program.sad
sad

Tll me something!
Enter 'quit' to end the program.ad
ad

Tll me something!
Enter 'quit' to end the program.ad
ad

Tll me something!
Enter 'quit' to end the program.quit
"""
#使break退出循环
prompt="\nTll me something!"
prompt+="\nEnter 'quit' to end the program."
while True:
    message=input(prompt)
    if message!='quit':
        print(message)
    else:
        break

"""
结果：
Tll me something!
Enter 'quit' to end the program.qw
qw

Tll me something!
Enter 'quit' to end the program.dsa
dsa

Tll me something!
Enter 'quit' to end the program.quit
"""
#在循环中使用continue
current_number=0
while current_number<=10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number) 
        
"""
结果：
1
3
5
7
9
11
"""
#在列表之间移动元素
unconfirmed_users=['alisa','jaky','breage']
confirmed_users=[]
while unconfirmed_users:
    user=unconfirmed_users.pop()
    confirmed_users.append(user)
    print("have added:"+user.title())
print("\nThe following users have been confirmed:")
for i in confirmed_users:
    print(i.title())
        
"""
结果：
have added:Breage
have added:Jaky
have added:Alisa

The following users have been confirmed:
Breage
Jaky
Alisa
""" 
#删除包含特定值的所有列表元素
pet=['a','s','d','a','w','e','a']
print(pet)
while 'a' in pet:
    pet.remove('a')
print(pet)
        
"""
结果：
['a', 's', 'd', 'a', 'w', 'e', 'a']
['s', 'd', 'w', 'e']
""" 
#使用用户输入来填充字典
responses={}
active=True
while active:
    name=input("\nwhst is your name?")
    where=input("where to go?")
    responses[name]=where
    repeat=input("'Yes'or'No'")
    if repeat=="No" :
        active=False
print("-----------")
for name,area in responses.items():
    print("\nname:"+name.title())
    print("area:"+area.title())
"""
结果：
whst is your name?qwqw
where to go?qwq
'Yes'or'No'Yes

whst is your name?fdd
where to go?dfd
'Yes'or'No'Yes

whst is your name?fds
where to go?xcv
'Yes'or'No'No
-----------

name:Qwqw
area:Qwq

name:Fdd
area:Dfd

name:Fds
area:Xcv
""" 

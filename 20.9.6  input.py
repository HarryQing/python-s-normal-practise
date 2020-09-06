#认识input()方法
prompt="If you tell us who you are ,we can personalize the messages you see."
prompt+="\nWhat is your first name!\n"
name=input(prompt)
print("\nHello,"+name.title()+"!")

"""
结果：
If you tell us who you are ,we can personalize the messages you see.
What is your first name!
tom

Hello,Tom!
"""
#使用int()来获取数值输入
height=input("How tall you are?\n")
height=int(height)
if height>=178:
    print("you are tall enough to rid!")
else:
    print("you well be able to ride when you are a little older")

"""
结果：
How tall you are?
188
you are tall enough to rid!

"""

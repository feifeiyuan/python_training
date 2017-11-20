#!/usr/bin/python3
#coding=utf-8
# 单行注释
'''
多行注释
'''

"""
多行注释
"""
x = 21
y = 10

# 算术运算符
print("x+y=%d"%(x+y))
print("x-y=%d"%(x-y))
print("x*y=%d"%(x*y))
print("x/y=%f"%(x/y))
print("x//y=%d"%(x//y))
print("x%%y=%d"%(x%y))
print("x**y=%ld"%(x**y))

# 逻辑运算符号

# 赋值运算符
'''
+= 不存在i++
'''
# 位运算
'''
& | ^ ~ << >>
'''
# 逻辑运算
'''
and or not
'''
a = 20
b = 0
if (a and b):
	print("hello")
if (a or b):
	print("world")
if (not b):
	print("not b is True")

# 成员元算符
'''
in
not in
'''
temp1=3
list1=[1,2,3,4,5]
if (temp1 in list1):
	print("temp1 is in list1")
else:
	print("temp1 is not in list1")

# 身份运算符
'''
is 
it not
'''
temp2=56
temp3=56
if (id(temp2) is id(temp3)):
	print("temp2 is temp3")
else:
	print("temp2 is temp3")



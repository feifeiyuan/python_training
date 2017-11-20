#!/usr/bin/python3
#coding=utf8

#for python key world
print("hello world")

# for pyhton keyworld
import keyword
print(keyword.kwlist)

#斐波那契数列
a,b = 0,1
while b<10:
	print(b,end=',')
	a, b = b, a+b # 复合赋值运算会在变动之前执行
print()

# for python3 six basic data type Numbers
#type
a,b,c,d = 20, 45.9, True, 4+7j
print(type(a),type(b),type(c), type(d))
#comp 
print((a+b), (a*b), (c/d), (a//b), (d-a))

# for python3 six basic data type String
s = 'yes this is a string\t' # add r complment natual str
print(s, type(s), len(s))
# strcat
bay="baby\n"
print(bay+"I\t"+"like\t"*3+"you")
# reverse
t = "python"
print(t[0], t[-1]) #p n
print(t[0:3],t[2:3]) # pyt t
# t[0] = 's' this is error string can not be changed


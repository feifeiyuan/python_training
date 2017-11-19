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

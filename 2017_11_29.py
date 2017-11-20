#!/usr/bin/python3
#coding=utf-8

# python 3 six basic data struct list
a = ['yuanhui', 'is', 20, 'and', 89.3]
# through list
print(a)
for i in range(len(a)):
	print(a[i])
# + is valaible
a = a+[7,5,'test']
print(a)

# list can be change
a[4] = 'kk'
print(a)
# can be del
a[2:4] = []
print(a)

# python 3 six basic data struct tuple
b = ('liuhao', 'is', 28, 78.3)
print(b, type(b), len(b))
for j in range(len(b)):
	print(b[j])
print(b[3:4]) # 一个元素需要在后面添加，(78.3,)
empty = ()# for empty list
one = (3,) # for one element list
print(b+one)
#b[2]='d' this is error

# python 3 six basic data struct sets
# 无序不重复
name = { 'judy', "tom", 'harry', 'judy'} 
print(name)#重复的元素不显示
song = set('adle')
empty_set = set() # it must use set not {}
print(song)
print('adle' in name)
seta = {'abracadabra'}
setb = {'alacazam'}
print(seta - setb)
print(seta | setb)
print(seta & setb)
print(seta ^ setb)

# python 3 six basic data struct dictionaries
dic = {} # this is empty dictionary
tele = {'yuanhui':26, 'liuhao':28, 'caodeng':30}
print(tele)
print(tele['yuanhui'])
del tele['liuhao']
print(tele)
#change dic to list
print(list(tele.keys())) # print(list(tele))
print(list(tele.values()))
print('caodeng' in tele.keys())
print(sorted(tele.keys()))

print(dict([('me', 'k'), ('you', 'kk')]))
print({x: x**2 for x in(2,4,6)})
print(dict(sape=41, guid=67, rosy='hello'))
# the key of dic is ifxed it can not list or tuple(it can include list)

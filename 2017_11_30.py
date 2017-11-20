#!/usr/bin/python3
#coding=utf-8
import re
expression='((100+40)*5/2-3*2*2/4+9)*(((3+4)-4)-4)'
l=re.findall('([\d\.]+|/|-|\+|\*)',expression)
print(l)



#!usr/bin/python3
#coding=utf8

# 用于正则匹配，需要使用re模块
import re

# 获取传入的参数
import sys
file_name = sys.argv[1]
str1 = "sprdfgu: d cap"
str2 = "\d{2}-\d{2} \d{2}:\d{2}:\d{2}" # 解析日期
str3 = "\d*mAh" # 电流值
list_time = []
list_value = []
# try except
try:
	# 打开文件
	file_obj = open(file_name, "rt" , encoding="utf-8", errors='ignore')
	# 循环读取文件
	while True:
		content = file_obj.readline()
		if not content:
			break

		# 在字符串中查找包含指定字符串的字串,返回值为第一个字串的索引，未找到返回-1
		index = content.find(str1)
		if index != -1:
			# 查找字符串中正则匹配的信息,返回值为一个list
			index_time = re.findall(str2, content)
			index_value = re.findall(str3, content)
			
			# 将list转换成字串
			index_time = ''.join(index_time)
			index_value = ''.join(index_value)


			print(index_time)
			print(index_value)
			
			#将字符串压入list
			list_time.append(index_time)
			list_value.append(index_value)
except:
	print("the file is not exist")




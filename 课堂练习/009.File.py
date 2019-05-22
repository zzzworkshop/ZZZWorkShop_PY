#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

#1、遍历目录下的所有文件，找到有特定关键字"zzzsl"的文件，并打印出来！
#   首先创建文件和目录
import os

# filelist = os.listdir(os.getcwd())
# print(filelist)
# #查看当前目录
#
# os.mkdir('test')    #创建一个test目录
# os.chdir('test')    #进入这个新的目录
# zzzsl1 = open('zzzsl1','w')   #创建一个zzzsl的文件，用写入模式打开
# zzzsl1.write('test file\n') #写入内容
# zzzsl1.write('this is zzzsl1\n')
# zzzsl1.close()
#
# zzzsl2 = open('zzzsl2','w')
# zzzsl2.write('test file\n')
# zzzsl2.write('this is zzzsl2\n')
# zzzsl2.close()
#
# zzzsl3 = open('zzzsl3','w')
# zzzsl3.write('test file\n')
# zzzsl3.write('this is python\n')
# zzzsl3.close()
#
# os.mkdir('zzzsl4')
# os.mkdir('zzzsl5')

os.chdir('/Users/zhizhezheng/PycharmProjects/ZZZWorkShop_PY/课堂练习/test')
#进入上面创建的文件目录
filelist = os.listdir(os.getcwd())  #罗列该目录下的所有文件与目录信息，并赋予字符串filelist
print(filelist)

zzzsl_file = []

for x in filelist:  #遍历字符串filelist，也就是文件夹下的所有
    if os.path.isfile(x):   #如果是文件
        for line in open(x):    #打开文件，逐行遍历
            if 'zzzsl' in line: #如果在当前行发现字符串"zzzsl"
                zzzsl_file.append(x)    #将文件名记录到列表中

set(zzzsl_file) #将列表转换为集合，这样可以自动清除重复的文件名，防止一个有多行zzzsl的文件重复记录

print('文件中包含"zzzsl"关键字的文件为：')
for y in zzzsl_file:
    print('{0:>15s}'.format(y))




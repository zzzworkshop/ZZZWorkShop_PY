#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
# Created by ZZZWorkShop

# 找到两个清单中相同的内容
list1 = ['aaa',111,(4,5),2.01]
list2 = ['bbb',333,111,3.14,(4,5)]

for x in list1:
    if x in list2:
        print(x,'is in list1 and list2')
    else:
        print(x,'is only in list1')


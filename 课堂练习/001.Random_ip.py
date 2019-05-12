#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop
import random   #导入random模块

#随机产生IP地址四个段落的数字
section1 = random.randint(1,255)
section2 = random.randint(1,255)
section3 = random.randint(1,255)
section4 = random.randint(1,255)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
#要把数字转换成为字符串，并且拼接到一起！

print("The random IP address is: %s" %random_ip)
#打印结果






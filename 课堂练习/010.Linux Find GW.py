#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
# Created by ZZZWorkShop

# Linux的"route -n"命令输出存储在文件"route -n.txt"中。
# 进入文件夹"Meterial"即可读取。文件的内容如下：
# [root@localhost ~]# route -n
# Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# 0.0.0.0         27.116.56.254   0.0.0.0         UG    100    0        0 ens33
# 27.116.56.0     0.0.0.0         255.255.255.0   U     100    0        0 ens33
# 27.116.57.0     0.0.0.0         255.255.255.0   U     100    0        0 ens33

# 根据输出找到网关，并打印到屏幕上。（网关的Flags为UG）

import os
import re

os.chdir('Meterial')

myfile = open('route -n.txt','r')
for x in myfile:
    x = myfile.readline()
    if x.split()[3] == 'UG':
        gateway = x.split()[1]
        print('网关是：',gateway)



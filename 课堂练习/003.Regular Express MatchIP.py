#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

#使用正则表达式对思科的show命令输出提取IP地址，并格式化打印结果
# SH_HLO17_MCD_3G01#sh ip int brie
# Interface                  IP-Address      OK? Method Status                Protocol
# Embedded-Service-Engine0/0 unassigned      YES unset  administratively down down
# GigabitEthernet0/0         116.246.14.221  YES manual up                    up

str1 = 'Embedded-Service-Engine0/0 unassigned      YES unset  administratively down down'
str2 = 'GigabitEthernet0/0         116.246.14.221  YES manual up                    up      '

import re
result1 = re.match('(\w.*\d)\s+(unassigned|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(YES|NO)\s+(unset|manual|dhcp)\s+'
                   '(ad\w+\sdown|up|down)\s+(up|down)',str1.strip()).groups()
result2 = re.match('(\w.*\d)\s+(unassigned|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(YES|NO)\s+(unset|manual|dhcp)\s+'
                   '(ad\w+\sdown|up|down)\s+(up|down)',str2.strip()).groups()

print('-'*40)
print('{0:<10s}{1:<s}'.format('接口1:',result1[0]))
print('{0:<10s}{1:<s}'.format('IP地址:',result1[1]))
print('{0:<10s}{1:<s}'.format('状态:',result1[4]))
print('{0:<10s}{1:<s}'.format('接口协议:',result1[5]))
print('-'*40)
print('{0:<10s}{1:<s}'.format('接口2:',result2[0]))
print('{0:<10s}{1:<s}'.format('IP地址:',result2[1]))
print('{0:<10s}{1:<s}'.format('状态:',result2[4]))
print('{0:<10s}{1:<s}'.format('接口协议:',result2[5]))





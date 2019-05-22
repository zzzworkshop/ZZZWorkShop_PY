#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

#把ASA防火墙上显示的当前连接输出转换为字典，然后格式化打印输出。
# ASA5506# show conn
#
# UDP outside  222.84.29.246:23744 outside  192.168.200.4:1863, idle 0:01:30, bytes 190, flags -
# UDP outside  46.166.190.142:44651 inside_3  27.116.56.20:50624, idle 0:00:25, bytes 402, flags -
# UDP outside  46.46.199.212:54309 inside_3  27.116.56.20:50624, idle 0:01:56, bytes 392, flags -
# TCP outside  62.210.202.61:80 inside_3  27.116.56.20:62200, idle 0:00:39, bytes 891, flags UfrxIO
# TCP outside  62.210.202.61:80 inside_3  27.116.56.20:62142, idle 0:00:54, bytes 2608, flags UfxO

import re

ASA_Output = 'UDP outside  222.84.29.246:23744 outside  192.168.200.4:1863, idle 0:01:30, bytes 190, flags -\n' \
             'UDP outside  46.166.190.142:44651 inside_3  27.116.56.20:50624, idle 0:00:25, bytes 402, flags -\n' \
             'UDP outside  46.46.199.212:54309 inside_3  27.116.56.20:50624, idle 0:01:56, bytes 392, flags -\n' \
             'TCP outside  62.210.202.61:80 inside_3  27.116.56.20:62200, idle 0:00:39, bytes 891, flags UfrxIO\n' \
             'TCP outside  62.210.202.61:80 inside_3  27.116.56.20:62142, idle 0:00:54, bytes 2608, flags UfxO'

D = {}

List_ASA_Output = ASA_Output.split('\n')

for x in List_ASA_Output:
    Key_ASA_Output = re.match('.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{2,5})\s+.*\s+'
                                '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{2,5}).*',x).groups()
    Value_ASA_Output = re.match('.*bytes\s(\d+),\s+flags\s(\w+|\-)',x).groups()
    D[Key_ASA_Output]=Value_ASA_Output
print('打印字典')
print(D)
print()

print('格式化打印输出')
print()
for key,value in D.items():
    print('{0:^10s} : {1:^20s} | {2:^10s} : {3:^10s} | {4:^10s} : {5:^20s} | {6:^10s} : {7:^10s}'
          .format('src',key[0],'src_p',key[1],'dest',key[2],'dst_p',key[3]))
    print('{0:^10s} : {1:^20s} | {2:^10s} : {3:^10s}'.format('bytes',value[0],'flags',value[1]))
    print('='*130)









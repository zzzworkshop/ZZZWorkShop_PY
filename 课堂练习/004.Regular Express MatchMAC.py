#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

# 配置RE匹配MAC地址，并格式化输出：
# SW#sh mac address-table
#           Mac Address Table
# -------------------------------------------
#
# Vlan    Mac Address       Type        Ports
# ----    -----------       --------    -----
#  All    0100.0ccc.cccc    STATIC      CPU
#  100    0000.0c07.ac64    DYNAMIC     Gi1/0/1
#  100    34f8.e73b.5bd1    STATIC      Vl100

str1 = '  All    0100.0ccc.cccc    STATIC      CPU'
str2 = '  100    0000.0c07.ac64    DYNAMIC     Gi1/0/1'
str3 = '  100    34f8.e73b.5bd1    STATIC      Vl100'

import re

MAC1 = re.match('(All|\d{1,4})\s+([\d,a-f,A-F]{4}.[\d,a-f,A-F]{4}.[\d,a-f,A-F]{4})\s+'
                '(STATIC|DYNAMIC)\s+(\w.*)',str1.strip()).groups()
MAC2 = re.match('(All|\d{1,4})\s+([\d,a-f,A-F]{4}.[\d,a-f,A-F]{4}.[\d,a-f,A-F]{4})\s+'
                '(STATIC|DYNAMIC)\s+(\w.*)',str2.strip()).groups()
MAC3 = re.match('(All|\d{1,4})\s+([\d,a-f,A-F]{4}.[\d,a-f,A-F]{4}.[\d,a-f,A-F]{4})\s+'
                '(STATIC|DYNAMIC)\s+(\w.*)',str3.strip()).groups()

print('-'*40)
print('{0:<10s}: {1:<10s}'.format('VLAN ID',MAC1[0]))
print('{0:<10s}: {1:<10s}'.format('MAC',MAC1[1]))
print('{0:<10s}: {1:<10s}'.format('Type',MAC1[2]))
print('{0:<10s}: {1:<10s}'.format('Interface',MAC1[3]))
print('-'*40)
print('{0:<10s}: {1:<10s}'.format('VLAN ID',MAC2[0]))
print('{0:<10s}: {1:<10s}'.format('MAC',MAC2[1]))
print('{0:<10s}: {1:<10s}'.format('Type',MAC2[2]))
print('{0:<10s}: {1:<10s}'.format('Interface',MAC2[3]))
print('-'*40)
print('{0:<10s}: {1:<10s}'.format('VLAN ID',MAC3[0]))
print('{0:<10s}: {1:<10s}'.format('MAC',MAC3[1]))
print('{0:<10s}: {1:<10s}'.format('Type',MAC3[2]))
print('{0:<10s}: {1:<10s}'.format('Interface',MAC3[3]))





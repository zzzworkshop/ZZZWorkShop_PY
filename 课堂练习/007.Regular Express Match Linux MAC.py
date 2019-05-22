#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

# 需求：用正则表达式对在Linux系统中使用命令"ifconfig"的输出进行处理，提取其中的MAC地址。
#
# 可以使用下面的方法得到Linux的ifconfig的输出：
# 1，在Linux命令行执行Python
# 2，import os
# 3，ifconfig_result = os.popen("ifconfig " + 'ens33').read() #其中，'ens33'是Linux一个接口的名称
# [root@localhost ~]# ifconfig
# ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 27.116.56.240  netmask 255.255.255.0  broadcast 27.116.56.255
#         inet6 fe80::820f:50b4:d1ce:f701  prefixlen 64  scopeid 0x20<link>
#         ether 00:0c:29:4f:2c:15  txqueuelen 1000  (Ethernet)
#         RX packets 234249  bytes 108981498 (103.9 MiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 124139  bytes 12322378 (11.7 MiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# 4，得到的输出是一个多行的字符串。返回值如下：

import re
ifconfig_result = 'ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n' \
                  '        inet 27.116.56.240  netmask 255.255.255.0  broadcast 27.116.56.255\n' \
                  '        inet6 fe80::820f:50b4:d1ce:f701  prefixlen 64  scopeid 0x20<link>\n' \
                  '        ether 00:0c:29:4f:2c:15  txqueuelen 1000  (Ethernet)\n' \
                  '        RX packets 234948  bytes 109164856 (104.1 MiB)\n' \
                  '        RX errors 0  dropped 0  overruns 0  frame 0\n' \
                  '        TX packets 124482  bytes 12360127 (11.7 MiB)\n' \
                  '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'

list_ifconfig_result = ifconfig_result.split('\n')

for x in list_ifconfig_result:
    Mac_Index = x.split()
    for y in Mac_Index:
        if re.match('[\d,a-f,A-F]{2}:[\d,a-f,A-F]{2}:[\d,a-f,A-F]{2}:[\d,a-f,A-F]{2}:[\d,a-f,A-F]{2}:[\d,a-f,A-F]{2}',y):
            print('MAC地址为：'+ y)








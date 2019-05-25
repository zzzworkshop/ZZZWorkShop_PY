#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
# Created by ZZZWorkShop

# 使用While语句循环监控TCP 80的HTTP服务运行状态

# 用Python配置一个简单的HTTP服务器
#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_

# from http.server import HTTPServer, CGIHTTPRequestHandler
#
# port = 80
#
# httpd = HTTPServer(('',port),CGIHTTPRequestHandler)
# print('Starting simple httpd on port:'+str(httpd.server_port))
# httpd.serve_forever()

import re
import os
import time

#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
#Created by ZZZWorkShop

#格式化字符串打印

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1 name:%-10sManager:%-10sCOURSE FEES:%-10.2fThe End!'%(department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%-10sManager:%-10sCOURSE FEES:%-10.2fThe End!'%(department2,depart2_m,COURSE_FEES_Python)
line3 = 'Department1 name:{0:<10s}Manager:{1:<10s}COURSE FEES:{2:<10.2f}The End!'\
    .format(department1,depart1_m,COURSE_FEES_SEC)
line4 = 'Department2 name:{0:<10s}Manager:{1:<10s}COURSE FEES:{2:<10.2f}The End!'\
    .format(department2,depart2_m,COURSE_FEES_Python)

length1 = len(line1)
length2 = len(line3)

print('String Format Print Method 1:')
print('='*length1)
print(line1)
print(line2)
print('='*length1)
print('String Format Print Method 2:')
print('='*length2)
print(line3)
print(line4)
print('='*length2)




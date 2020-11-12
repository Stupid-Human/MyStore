#!/usr/bin/env python
# coding=utf-8
age = int(input())      #int()函数 强制类型转换
if age>=18:
    print('you are adult, come in please')
elif age>0:
    print('you are too young, sorry about that')
else:
    print('maybe you have the wrong age')


#!/usr/bin/env python
# coding=utf-8
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中文自然语言处理'.encode('utf-8'))
print(len('中文自然语言处理'.encode('utf-8')))
#len求字符个数，如果求字节个数，则用encode来先转化一下

#最后一个print输出24，说明utf-8编码，将一个中文汉字编码为3个字节

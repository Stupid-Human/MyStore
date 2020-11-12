#!/usr/bin/env python
# coding=utf-8
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print('show 1+2+...+100')
sum = 0;
for x in range(101):   #range(x)函数生成小于x的整数列
    sum = sum + x
print('1+2+...+100 = %d' % sum)

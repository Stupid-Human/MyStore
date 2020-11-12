#!/usr/bin/env python
# coding=utf-8
print('T = %s %s %s \n' % ('one', 'two', 'three'))

#如果先令T = ('one', 'two', 'three')
#再输出 print('T = %s' % T) 
#会报错 TypeError: not all arguments converted during string formatting

ML = [1,2,3]

LL = (1, True, 'aha', ML)
print('LL = %s %s %s %s\n' % LL)

#tuple不变的意思是指向不变,
ML[0] = '01'    #LL[3]指向ML的地址，这个地址是不变的，但是ML里的内容本身是可变的
LL[3][1] = '02'
#LL[1] = False LL[1]指向的空间内容是不可变的
print('after change ML, LL = %s %s %s %s\n' % LL)

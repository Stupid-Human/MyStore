#!/usr/bin/env python
# coding=utf-8
#可变参数就是说传入的参数个数是可变的
def calc(number):
    sum = 0
    for x in number:
        sum = sum + x * x
    return sum
print(calc([1, 2, 3]))
print(calc((1, 2, 3)))

#print(calc(1, 2, 3))
#TypeError: calc() takes 1 positional argument but 3 were given

print('*******************')
#可变仅仅在参数前面加了一个*号
#函数内部，参数numbers接收到的是一个tuple。可传入任意个参数
def calc(*number):
    sum = 0
    for x in number:
        sum = sum + x * x
    return sum
print(calc(1, 2, 3))
print(calc())

print('*******************')
nums = [1, 2, 3]
#print(calc(nums))
#TypeError: can't multiply sequence by non-int of type 'list'

print(calc(*nums))
#输出14
nums = (1, 2, 3)
print(calc(*nums))
#输出14
#*nums表示把nums这个list/tuple的所有元素作为可变参数传进去!!!

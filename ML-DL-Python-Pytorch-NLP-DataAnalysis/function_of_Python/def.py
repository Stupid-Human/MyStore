#!/usr/bin/env python
# coding=utf-8
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-1))
#def语句，依次写出函数名、括号、括号中的参数和冒号
#在缩进块中编写函数体，函数的返回值用return语句返回

def nop():
    pass
#pass可以用来作为占位符
#暂时还没想好怎么写函数的代码，可先放一个pass，让代码能运行起来

age = 20
if age > 18:
    pass
#pass还可以用在其他语句里


import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

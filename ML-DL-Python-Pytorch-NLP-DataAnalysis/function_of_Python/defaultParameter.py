#!/usr/bin/env python
# coding=utf-8
print("*********************")
def power(x, n = 2):    
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(power(5, 3))
print(power(5))
#n=2 设置默认参数，调用power(5)时就相当于调用power(5, 2)
#但是必选参数必须在前，默认参数必须在后，否则会有歧义
#把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数

print("*********************")
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('\n')
enroll('Liming', 'F', 8)
enroll('Cuihua', 'F', city = 'Chengdu')
#当不按顺序提供部分默认参数时，需要把参数名写上

print("*********************")
#默认参数必须指向不变对象
def add_end(L = []):
    L.append('END')
    return L
print(add_end(['much', 2, False]))
print(add_end())
#输出：['END']
print(add_end())
#输出：['END', 'END']
print(add_end())
#输出：['END', 'END', 'END']

print("*********************")
#加入不变对象None来修改程序
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end(['aha']))
print(add_end())
print(add_end())
print(add_end())
#调用多少次都输出：['END']

#!/usr/bin/env python
# coding=utf-8
#多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来
"""
五种参数可以组合使用，但是要遵守下述规则
必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#f2中d是命名关键字参数，f1中kw是关键字参数

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 4, 'a', 'b')
f1(1, 2, 5, 'a', grade = 'Five', age = 23)
f2(1, 2, 5,d =  6, City = 'Guangzhou', Grade = 'One')
#f2 d是命名关键字参数 而kw是关键字参数
'''输出
a = 1 b = 2 c = 0 args = () kw = {}
a = 1 b = 2 c = 3 args = () kw = {}
a = 1 b = 2 c = 4 args = ('a', 'b') kw = {}
a = 1 b = 2 c = 5 args = ('a',) kw = {'age': 23, 'grade': 'Five'}
a = 1 b = 2 c = 5 d = 6 kw = {'City': 'Guangzhou', 'Grade': 'One'}
'''
print('***********************')
args = (1, 2, 3, 4)
kw = {'e':99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3, 4, 5)
kw = {'e':99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d':88, 'x':'#'}
f2(*args, **kw)

'''输出
a = 1 b = 2 c = 0 args = () kw = {}
a = 1 b = 2 c = 3 args = () kw = {}
a = 1 b = 2 c = 4 args = ('a', 'b') kw = {}
a = 1 b = 2 c = 5 args = ('a',) kw = {'grade': 'Five', 'age': 23}
a = 1 b = 2 c = 5 d = 6 kw = {'City': 'Guangzhou', 'Grade': 'One'}
***********************
a = 1 b = 2 c = 3 args = (4,) kw = {'e': 99, 'x': '#'}
a = 1 b = 2 c = 3 args = (4, 5) kw = {'e': 99, 'x': '#'}
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
'''
#so，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
#无论它的参数是如何定义的

print('***********************')
#计算两个数的乘积，并改造，可接受1个或多个数并求乘积
def product(*x):
    if len(x) == 0:
        raise TypeError('bad operand type')
    multiply = 1
    for mm in x:
         multiply = multiply * mm
    return multiply

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

'''输出
product(5) = 5 
product(5, 6) = 30 
product(5, 6, 7) = 210 
product(5, 6, 7, 9) = 1890 
测试成功! 
'''

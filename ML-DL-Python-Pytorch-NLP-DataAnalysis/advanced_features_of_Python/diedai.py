#!/usr/bin/env python
# coding=utf-8
#任何可迭代对象都可以作用于for循环
#包括我们自定义的数据类型
#只要符合迭代条件，就可以使用for循环

def findMinAndMax(L):
    if L==[]:
        return(None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i>max:
                max = i
            if i<min:
                min = i
        return(min, max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


#!/usr/bin/env python
# coding=utf-8
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
#取指定范围内的数的操作用循环十分麻烦


#切片操作出场
print(L[0:3])
#从索引0开始取，直到索引3为止，但不包括索引3
print(L[-2:])
print(L[-2:-1])

#支持倒数切片
L = list(range(100))
print(L)
print(L[0:10:2]) 
#前10个数，每两个取一个
print(L[-1:])
#获取最后一个数
print(L[:1])
#获取第一个数
print(L[::5])
#所有数，每5个取一个
print(L[:])
#只写[:]就可以原样复制一个list

print((0, 1, 2, 3, 4, 5)[:3])
#tuple也可以用切片操作，操作结果仍是tuple

print('ABCDEFGHIGKLMN'[:3])
#字符串也可以看成是一种list，每个元素就是一个字符
#因此，字符串也可以用切片操作，操作结果仍是字符串

print('*****************')
#实战：利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

#测试：
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')





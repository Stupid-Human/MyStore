#!/usr/bin/env python
# coding=utf-8
sum = 0
n = 99
i = 0
while n>0:
    sum = sum + n
    n = n-2
    i = i+1
print('sum = %d' % sum)
print('how many times cycling:%d' % i)

print('another programm to show while:')
L = ['Bart', 'Lisa', 'Adam']
i = len(L)
j = 0
while i>0:
    print(L[j])
    j = j+1
    i = i-1


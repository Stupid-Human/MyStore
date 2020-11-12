#!/usr/bin/env python
# coding=utf-8
sum = 0
i = 1
while i <= 100:
    i = i + 1
    if i%2 == 1: # 当n为奇数时 跳过循环
        continue # 跳过当前的这次循环，直接开始下一次循环
    sum = sum + i
print('2+4+6+...+100 = %d' % sum)

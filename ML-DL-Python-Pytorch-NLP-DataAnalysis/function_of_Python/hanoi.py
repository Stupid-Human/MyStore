#!/usr/bin/env python
# coding=utf-8

def move(n, A, B, C):
    if n == 1:
        print(A, '-->', C)
    else:
        move(n-1, A, C, B)
        move(1, A, B, C)
        #上一条语句可以改成:print(A, '-->', C)
        move(n-1, B, A, C)

move(3, 'A', 'B', 'C')

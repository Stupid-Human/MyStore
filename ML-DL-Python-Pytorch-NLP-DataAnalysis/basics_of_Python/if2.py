#!/usr/bin/env python
# coding=utf-8
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi<18.5:
    printf('two light')
elif bmi<23.0:
    print('normal')
elif bmi<28.0:
    print('a little heavy')
elif bmi<32.0:
    print('fat')
else:
    print('two fat')

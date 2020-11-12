#!/usr/bin/env python
# coding=utf-8
classmate = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print('classmate = %s' % classmate)
print('The length of classmate is %d' % len(classmate))   #len求list元素的个数
print('classmate[0] = %s' % classmate[0])
print('classmate[-1] = %s' % classmate[-1])     #-1可以直接获取最后一个元素
print('classmate[-2] = %s' % classmate[-2])     #-2类推，获取倒数第二个元素
print('classmate[1] = %s' % classmate[1])
print('classmate[-7] = %s\n' % classmate[-7])

#print('classmate[7] = %s' % classmate[7])
#报错:IndexError: list index out of range

#print('classmate[-8] = %s' % classmate[-8])
#报错:IndexError: list index out of range

print('after(insert(1,\'Jack\'))')
classmate.insert(1, 'Jack')     #把元素插入到指定位置
print('classmate = %s' % classmate)
print('The length of classmate is %d\n' % len(classmate))   

print('after(append(\'Ayida\'))')
classmate.append('Ayida')     #追加元素到末尾
print('classmate = %s' % classmate)
print('The length of classmate is %d\n' % len(classmate))   

print('after pop()')
classmate.pop()     #删除末尾元素
print('classmate = %s' % classmate)
print('The length of classmate is %d\n' % len(classmate))   

print('after pop(1)')
classmate.pop(1)     #删除指定索引位置元素
print('classmate = %s' % classmate)
print('The length of classmate is %d\n' % len(classmate))   

print('after replaceclassmate[1]')
classmate[1] = 'Two'     
print('classmate = %s' % classmate)
print('The length of classmate is %d\n' % len(classmate))   

print('show that list has different data type')
L = ['aha', 1, True, classmate, ['hello', 'you', 1]]
#list可以包含不同的数据类型，甚至可以包含另一个List
print('L = %s' % classmate)   
#求长度只是求“第一层”的“元素”的个数
print('The length of classmate is %d\n' % len(classmate))   

print('show array')
print('classmate[4] = %s' % classmate[4])
print('L[3][4] = %s\n' % L[3][4])     #类似于二维数组

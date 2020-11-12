#!/usr/bin/env python
# coding=utf-8

#可变参数允许你传入0个或任意个参数
#这些可变参数在函数调用时自动组装为一个tuple
#而关键字参数允许传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Xiaoming', 24, city = 'Beijing')
#output:name: Xiaoming age: 24 other: {'city': 'Beijing'}

person('Xiaoming', 24, city = 'Beijing', job = 'Engineer')
d = {'city':'Beijing', 'job':'Engineer'}
person('Xiaoming', 24, city = d['city'], job = d['job'])
#按照格式来写就行了
#person('Xiaoming', 24, d['city'], d['job'])
#TypeError: person() takes 2 positional arguments but 4 were given

person('Xiaoming', 24, **d)
#**d表示把d这个dict的所有key-value用关键字参数传入到函数的**kw参数
#传完相当于拷贝 对kw的改动不影响d

#命名关键字参数
#*后面的参数被视为命名关键字参数
#限制关键字参数的名字，用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Xiaomei', 22, city = 'Nanjing', job = 'teacher')

#如果函数定义中已经有了一个可变参数
#后面跟着的命名关键字参数就不再需要分隔符*了
#但命名关键字参数必须传入参数名，这和位置参数不同
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Dahuang', 27, 233, 332, 222, city = 'Beijing', job = 'doctor')
#输出：Dahuang 27 (233, 332, 222) Beijing doctor

person('Dahuang', 27, city = 'Beijing', job = 'doctor')
#输出：Dahuang 27 () Beijing doctor

#person('Dahuang', 27, 233, 332, 222, 'Beijing', 'doctor')
#TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

#命名关键字参数可以有缺省值 简化调用
def person(name, age, *, city = 'Wuhan', job):
    print(name, age, city, job)
person('Wangshuang', 54, job = 'CivilServant')
#Wangshuang 54 Wuhan CivilServant

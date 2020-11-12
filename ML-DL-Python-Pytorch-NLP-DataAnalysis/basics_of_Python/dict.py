#!/usr/bin/env python
# coding=utf-8
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('d = %s' % d)

d['Steven'] = 911
print('d = %s' % d)

d['Bob'] = 110
print('d = %s' % d)

print('\'Tom\' in d:%s' % ('Tom' in d))
print('\'Bob\' in d:%s' % ('Bob' in d))

print('get Tom') 
print(d.get('Tom', -1))
print('d = %s' % d)
d.pop('Bob')
print('after delete Bob')
print('d = %s' % d)

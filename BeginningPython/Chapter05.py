#!/usr/bin/python
# -*- coding: utf-8 -*
# 第五章 条件、循环和其他语句

# 使用逗号输出
print 'Age:', 31
print 'Hello',
print 'world'

import math as foobar
print foobar.sqrt(8)

# 赋值魔法
x, y, z = 1, 2, 3
print x, y, z
x, y = y, x
print x, y, z

# 布尔变量
print "bool('0') =", bool('0')
print "bool(0)   =", bool(0)
print "bool('')  =", bool('')
print "bool([])  =", bool([])
print "bool(())  =", bool(())

# if...elif...else
if (x == 1):
    print 'x is one'
elif (x == 2):
    print 'x is two'
else:
    print 'x is x'

c = 33
if (31 < c < 38):
    print 'She is mine!'

x = y = [3]
z = [3]
print 'x == y :', x == y
print 'x == z :', x == z
print 'x is y :', x is y
print 'x is z :', x is z

# 循环
for number in range(0, 10):
    print '%2d' % number,
print

girls = {'changxy' : 'A', 'lixue' : 'D', 'xuejj' : 'B', 'lijia' : 'C'}
for name in girls:
    print '%-7s cup is %s.' % (name, girls[name])
for name, cup in girls.items():
    print '%-7s : %s.' % (name, cup)

print zip(range(5), xrange(1000000))

from math import sqrt as qr
for n in range(99, 0, -1):
    root = qr(n)
    if root == int(root):
        print n
        break
for n in range(99, 81, -1):
    root = qr(n)
    if root == int(root):
        print n
        break
else:
    print "I can't find it."

# 列表推导式
print [x * x for x in range(10)]
print [x * x for x in range(10) if x % 3 == 0]

girls = ['changxy', 'lixue', 'xuejj']
names = ['cxy', 'lx', 'xjj']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print [n+':'+g for n in names for g in letterGirls[n[0]]]

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(9)
print scope['sqrt']

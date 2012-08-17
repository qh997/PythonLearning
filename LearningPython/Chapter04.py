#!/usr/bin/python
# -*- coding: utf-8 -*
# 第四章 介绍 Python 对象类型
print '####\n#### 第四章 介绍 Python 对象类型\n####\n'

# 数字
print '【数字】'
print '123 + 321  =', 123 + 321
print '1.5 * 4    =', 1.5 * 4
print ' 2 ** 100  =', 2 ** 100
print '`2 ** 100` =', `2 ** 100`

import math
print 'math.pi = ' + str(math.pi)
print 'math.sqrt(85) = ' + str(math.sqrt(85))

import random
print 'random.random() =', random.random()
print 'random.choice([1,2,3,4]) =', random.choice([1,2,3,4])
print

# 字符串
print '【字符串】'
S = 'lixue'
print 'S =', S
print 'len(S) =', len(S)
print 'S[2] =', S[2]
print 'S[-1] =', S[-1]
print 'S[0:2] =', S[0:2]
print 'S[2:] =', S[2:]
print 'S[-1::-1] =', S[-1::-1]
print 'S[:] =', S[:]
print 'S + \'Jie\' ＝', S + 'Jie'
print 'S * 3 ＝', S * 3
print "S.find('x') =", S.find('x')
print "S.replace('x', ' X') =", S.replace('x', ' X')
print "S.upper() =", S.upper()
print "S.isalpha() =", S.isalpha()
L = 'aaa,bbb,ccc'
print 'L =', L
print "L.split(',') =", L.split(',')
print

# 模式匹配
print '【模式匹配】'
import re
match = re.match('\w+\s+(\w+)', 'Hello Python world')
print 'match.group(1) =', match.group(1)
print

# 列表
print '【列表】'
L = [123, 'lixue', 1.23, 'changxy']
print 'L =', L
print 'len(L) =', len(L)
print 'L[1] =', L[1]
print 'L[:-1] =', L[:-1]
print "L.append('xuejj') =", L.append('xuejj')
print 'L =', L
print 'L.pop(2) =', L.pop(2)
print 'L =', L
print 'L.sort() =', L.sort()
print 'L =', L
print 'L.reverse() =', L.reverse()
print 'L =', L
print

# 嵌套
print '【嵌套】'
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print 'M =', M
print 'M[1] =', M[1]
print 'M[2][1] =', M[2][1]
print

# 列表解析
print '【列表解析】'
print '[row[1] * 2 for row in M] =', [row[1] * 2 for row in M]
print '[row[2] for row in M if row[1] % 2 == 0] =', [row[2] for row in M if row[1] % 2 == 0]
print "[c * 2 for c in 'lixue'] =", [c * 2 for c in 'lixue']
print

# 字典
print '【字典】'
D = {'name' : 'lixue', 'cup' : 'D+', 'color' : 'purple'}
print 'D =', D
print "D['color'] =", D['color']
D['times'] = 8
print 'D =', D
rec = {'name' : {'frist' : 'Li', 'last' : 'Xue'},
       'size' : [91, 62, 85],
       'cup'  : 'D+'}
print 'rec =', rec
print "rec['name'] =", rec['name']
print "rec['name']['last'] =", rec['name']['last']
print "rec['size'][0] =", rec['size'][0]
print "rec['size'][-1] =", rec['size'][-1]
print

# 键的排序
print '【键的排序】'
D = {'a': 1, 'b': 2, 'c': 3}
print 'D =', D
print 'sorted(D) =', sorted(D)
for key in sorted(D):
    print '  ', key, '=>', D[key]
print

# 不存在的键：if测试
print '【不存在的键：if测试】'
print "D.has_key('x') =", D.has_key('x')
print

# 元组
print '【元组】'
T = (1,2,3,4)
print 'T =', T
print 'len(T) =', len(T)
print 'T + (5, 6) =', T + (5, 6)
print

# 文件
print '【文件】'
f = open('data.txt', 'w')
print 'f =', f
f.write('Hello\n')
f.write('World\n')
f.close()
f = open('data.txt')
print 'f =', f
byte = f.read()
print 'byte =', repr(byte)
print 'byte.split() =', byte.split()
f.seek(0)
for line in f.readlines():
    print '  line =', repr(line)
print

# 集合
print '【集合】'
X = set('changxy')
Y = set(['c', 'x', 'y'])
print 'X, Y =', X, Y
print 'X & Y =', X & Y
print 'X | Y =', X | Y
print 'X - Y =', X - Y
print

# 十进制数
print '【十进制数】'
import decimal
d = decimal.Decimal('3.141')
print 'd =', d
print 'repr(d + 1) =', repr(d + 1)
print

# 布尔值
print '【布尔值】'
print ' 1 > 2 =', 1 > 2
print ' 1 < 2 =', 1 < 2
print

# None
print '【None】'
print 'L.sort() =', L.sort()
print

# 对象类型
print '【对象类型】'
print 'type(L) =', type(L)
print '(type(L) == list) =', type(L) == list
print '(type(L) == type([])) =', type(L) == type([])
print 'isinstance(L, list) =', isinstance(L, list)
print

# 用户定义的类
print '【用户定义的类】'
class Worker:
    def __init__(self, name, breast):
        self.name = name
        self.breast = breast

    def lastName(self):
        return self.name.split()[-1]

    def getSize(self):
        return self.breast

    def knead(self):
        new_cup = chr(ord(self.breast[-1:]) + 1)
        if ord(new_cup) < ord('G'):
            self.breast = self.breast[:-1] + new_cup

lx = Worker('Li Xue', '36B')
print 'lx =', lx
print 'lx.lastName()  =', lx.lastName()
print lx.getSize()
lx.knead()
print lx.getSize()
lx.knead()
print lx.getSize()
lx.knead()
print lx.getSize()
print

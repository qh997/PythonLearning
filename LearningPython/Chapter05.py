#!/usr/bin/python
# -*- coding: utf-8 -*
# 第五章 数字
print '####\n#### 第五章 数字\n####\n'

# 变量和基本的表达式
print '【变量和基本的表达式】'
a = 3
b = 4
print 'a + 1, b + 1 =', repr((a + 1, a - 1))
print 'repr(2 ** 200)', repr(2 ** 200)
print '(2 + 1j) * (3 + 2j) =', (2 + 1j) * (3 + 2j)
print '01, 010, 0100 :', (01, 010, 0100)
print '0x1, 0x10, 0x100 :', (0x1, 0x10, 0x100)
print 'oct(997), hex(997) :', (oct(997), hex(997))
print "int('0100'), int('0100', 8), int('0x40', 16) :", (int('0100'), int('0100', 8), int('0x40', 16))
print '997 /  19 =', 997 / 19
print '997 %  19 =', 997 % 19
print '997 // 19 =', 997 // 19
print

# math 模块
print '【math 模块】'
import math
print 'math.pi =', math.pi
print 'math.e =', math.e
print 'math.sin(math.pi / 6) =', math.sin(math.pi / 6)
print 'mmath.sqrt(2) =', math.sqrt(2)
print

# random 模块
print '【random 模块】'
import random
print "random.random() =", random.random()
print "random.randint(1, 10) =", random.randint(1, 10)
print "random.randint(1, 10) =", random.choice(['LiXue', 'ChangXingYe', 'XueJiaJia', 'GuoNa'])
print

# 小数数字
print '【小数数字】'
print '    0.1   +     0.1   +     0.1   -     0.3   =', 0.1 + 0.1 + 0.1 - 0.3
from decimal import Decimal as dc
print "dc('0.1') + dc('0.1') + dc('0.1') - dc('0.3') =", dc('0.1') + dc('0.1') + dc('0.1') - dc('0.3')
print

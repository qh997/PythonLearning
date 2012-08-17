#!/usr/bin/python
# -*- coding: utf-8 -*
# 第六章 动态类型简介
print '####\n#### 第六章 动态类型简介\n####\n'

# 共享引用和相等
print '【共享引用和相等】'
L = [1,2,3]
M = L
print 'L = [1,2,3]; M = L'
print 'L == M :', L == M
print 'L is M :', L is M
L = [1,2,3]
M = [1,2,3]
print 'L = [1,2,3]; M = [1,2,3]'
print 'L == M :', L == M
print 'L is M :', L is M
a = 997
import sys
print 'sys.getrefcount(1) =', sys.getrefcount(1)
print 'sys.getrefcount(997) =', sys.getrefcount(997)

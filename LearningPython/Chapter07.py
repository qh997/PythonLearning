#!/usr/bin/python
# -*- coding: utf-8 -*
# 第七章 字符串
print '####\n#### 第七章 字符串\n####\n'

# 字符串常量
print '【字符串常量】'
print "r'D:\\ndown\\hello' =", r'D:\ndown\hello'
s = 'a\nb\tc'
print 's =', s
print 'len(s) =', len(s)
print

# 基本操作
print '【基本操作】'
print "len('abc') =", len('abc')
print "'abc' + 'def' =", 'abc' + 'def'
print "'Nil' * 3 =", 'Nil' * 3
myMis = 'LiXue'
for c in myMis:
    print c,
print
print "'X' in myMis =", 'X' in myMis
print "'x' in myMis =", 'x' in myMis
print

# 索引和分片
print '【索引和分片】'
S = 'lixue'
print 'S =', S
print 'S[0], S[-1] ＝', repr((S[0], S[-1]))
print 'S[1:3] ＝', S[1:3]
print

# 字符串转换工具
print '【字符串转换工具】'
print 'int("42") =', repr(int("42"))
print 'str(42) =', repr(str(42))
print 'float("3.141") =', repr(float("3.141"))
print 'ord("x") =', ord("x")
print 'chr(120) =', chr(120)
print 'chr(ord("x") + 1) =', chr(ord("x") + 1)
print 'chr(ord("x") + 2) =', chr(ord("x") + 2)
print

# 修改字符串
print '【修改字符串】'
M = S
print 'M =', M
M = M + 'ying'
print 'M =', M
M = 'zhang' + M[2:]
print 'M =', M
M = M.replace('zhangxue', 'wang')
print 'M =', M
print

# 字符串格式化
print '【字符串格式化】'
print "%d %s %d you!" % (1, 'lixue', 2)
print "%s -- %s -- %s" % (42, 1.414, [1,'a',3])
x = 1234
print 'x =', x
print "...%d...%-6d...%06d" % (x, x, x)
x = 1.23456789
print 'x =', x
print "%e | %f | %g" % (x, x, x)
print "%-6.2f | %05.2f | %+06.1f" % (x, x, x)
print "%s" % x
print

# 基于字典的字符串格式化
print '【基于字典的字符串格式化】'
print '%(bust)d%(cup)c %(name)s' % {'bust': 37, 'name': 'lixue', 'cup': 'D'}
print '%(myMis)s <=> %(M)s' % vars()
print

# 字符串方法
print '【字符串方法】'
S = 'changzy'
print 'S =', S
L = list(S)
print 'L =', L
L[-2] = 'x'
print 'L =', L
S = ''.join(L)
print 'S =', S
print "'<=>'.join(['lixue','changxy','xuejj']) =", '<=>'.join(['lixue','changxy','xuejj'])
print "'a,b,c'.split(',') =", 'a,b,c'.split(',')
line = 'xuejj\n'
print 'line =', repr(line)
print 'line.rstrip() =', repr(line.rstrip())

#!/usr/bin/python
# -*- coding: utf-8 -*
# 第八章 列表与字典
print '####\n#### 第八章 列表与字典\n####\n'

# 列表的基本操作
print '【列表的基本操作】'
print 'len([1,2,3]) =', len([1,2,3])
print '[1,2] + [3,4] =', [1,2] + [3,4]
print "['LiXue'] * 3 =", ['LiXue'] * 3
print '3 in [1,2,3] =', 3 in [1,2,3]
print '4 in [1,2,3] =', 4 in [1,2,3]
print

# 原处修改列表
print '【原处修改列表】'
L = ['changxy', 'changxy', 'xuejj']
print 'L =', L
L[0] = 'lixue'
print 'L =', L
L[0:2] = ['guon', 'guoshuai']
print 'L =', L
L[0:2] = L[1:3]
print 'L =', L
L.append('lixue')
print 'L =', L
L.sort()
print 'L =', L
del L[2]
print 'L =', L
print

# 字典的基本操作
print '【字典的基本操作】'
D = {'lixue': 37, 'changxy': 34, 'xuejj': 36}
print 'D =', D
print "D['xuejj'] =", D['xuejj']
print 'len(D) =', len(D)
print "D.has_key('lixue') =", D.has_key('lixue')
print "'lixue' in D =", 'lixue' in D
print 'D.keys() =', D.keys()
print

# 原处修改字典
print '【原处修改字典】'
D['xuejj'] = [34,25,36]
print 'D =', D
del D['changxy']
print 'D =', D
D['guoshuai'] = 'LEWD'
print 'D =', D
print 'D.items() =', D.items()
print "D.get('lixue', 'D') =", D.get('lixue', 'D')
print "D.get('guona') =", D.get('guona')
print "D.get('changxy', 'B') =", D.get('changxy', 'B')
D1 = D
D2 = {'zhaoting': '36C', 'lixue': '37D'}
print 'D1 =', D1
print 'D2 =', D2
print 'D1.update(D2) =', D1.update(D2)
print 'D1 =', D1
print "D2.pop('lixue') =", D2.pop('lixue')
print 'D2 =', D2
print

# 创建字典的其他方法
print '【创建字典的其他方法】'
print dict(name = 'lixue', size = [37,25,36], cup = 'D')
print dict([('name','lixue'), ('size',[37,25,36]), ('cup','D')])
print dict.fromkeys(['a', 'b'], 99)

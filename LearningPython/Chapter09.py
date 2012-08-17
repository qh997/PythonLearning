#!/usr/bin/python
# -*- coding: utf-8 -*
# 第九章 元组、文件及其他
print '####\n#### 第九章 元组、文件及其他\n####\n'

# 实际应用中的元组
print '【实际应用中的元组】'
print '(1,2) + (3,4) =', (1,2) + (3,4)
print '(1,2) * 3 =', (1,2) * 3
T = (1,2,3,4)
print 'T =', T
print 'T[0] =', (T[0], T[1:3])
print '(40,) =', (40,)
print

# 转换以及不可变性
print '【转换以及不可变性】'
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
print 'T =', T
print 'list(T) =', list(T)
tmp.sort()
T = tuple(tmp)
print 'T =', T
T = (1, [2, 3], 4)
print 'T =', T
T[1][0] = 'lixue'
print 'T =', T
T = (1,2,3)
M = (1,2,3)
print 'T =', T
print 'M =', M
print 'T == M :', T == M
print 'T is M :',T is M
print

# 实际应用中的文件
print '【实际应用中的文件】'
myfile = open('myfile', 'w')
myfile.write('hello text file\n')
myfile.close

myfile = open('myfile')
print 'myfile.readline() :', repr(myfile.readline())
print 'myfile.readline() :', repr(myfile.readline())
myfile.close
print

# 在文件中储存并解析 Python 对象
print '【在文件中储存并解析 Python 对象】'
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

bytes = open('datafile.txt').read()
print 'repr(bytes) =', repr(bytes)

F = open('datafile.txt')
print 'repr(F.readline().rstrip()) =', repr(F.readline().rstrip())
print "[int(x) for x in F.readline().rstrip().split(',')] =", [int(x) for x in F.readline().rstrip().split(',')]
print "[eval(p) for p in F.readline().rstrip().split('$')] =", [eval(p) for p in F.readline().rstrip().split('$')]
F.close()
print

# 使用 pickle 储存 Python 原生对象
print '【使用 pickle 储存 Python 原生对象】'
F = open('datafile.txt', 'w')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.txt')
print 'repr(pickle.load(F)) =', repr(pickle.load(F))
F.close()
print

# 文件中打包二进制数据的储存与解析
print '【文件中打包二进制数据的储存与解析】'
F = open('data.bin', 'wb')
import struct
bytes = struct.pack('>i4sh', 7, 'spam', 8)
print 'repr(bytes) =', repr(bytes)
F.write(bytes)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print 'repr(data) =', repr(data)
print "struct.unpack('>i4sh', data) =", struct.unpack('>i4sh', data)
print

# 引用 VS 拷贝
print '【引用 VS 拷贝】'
X0 = [1, 2, 3]
L1 = ['a', X0, 'b']
L2 = ['a', X0[:], 'b']
D1 = {'x': X0, 'y': 2}
D2 = {'x': X0[:], 'y': 2}
print 'X0 =', X0
print 'L1 =', L1
print 'L2 =', L2
print 'D1 =', D1
print 'D2 =', D2
X0[1] = 'LiXue'
print "X0[1] = 'LiXue'"
print 'X0 =', X0
print 'L1 =', L1
print 'L2 =', L2
print 'D1 =', D1
print 'D2 =', D2
import copy
print "import copy"
X = ['abc', [(1, 2), {'x': [9, 8]}], 5]
C1 = X[:]
C2 = copy.deepcopy(X)
print 'X  =', X
print 'C1 =', C1
print 'C2 =', C2
X[2] += 7
X[1][1]['x'].append(7)
print "X[2] += 7"
print "X[1][1]['x'].append(7)"
print 'X  =', X
print 'C1 =', C1
print 'C2 =', C2
print

# 比较、相等和真值
print '【比较、相等和真值】'
S1 = 'spam'
S2 = 'spam'
print 'S1 =', S1
print 'S2 =', S2
print '(S1 == S2, S1 is S2)'
print '  %-6s    %-6s' % (S1 == S2, S1 is S2)
S1 = 'a longer string 0123456789' * 2
S2 = 'a longer string 0123456789' * 2
print 'S1 =', S1
print 'S2 =', S2
print '(S1 == S2, S1 is S2)'
print '  %-6s    %-6s' % (S1 == S2, S1 is S2)
print

# 重复能够增加层次深度
print '【重复能够增加层次深度】'
L = [4, 5, 6]
X = L * 4
Y = [L] * 4
print 'X =  L  * 4 :', X
print 'Y = [L] * 4 :', Y
L[1] = 0
print 'L[1] = 0'
print 'X =  L  * 4 :', X
print 'Y = [L] * 4 :', Y

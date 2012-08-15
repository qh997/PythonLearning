#!/usr/bin/python
# -*- coding: utf-8 -*
# 第三章 使用字符串

format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print format % values

from string import Template

s = Template('$x, glorious ${z}yx $$!')
d = {}
d['x'] = 'foo'
d['z'] = 'bar'
print s.substitute(d)

# 字符串格式化
print "%s plus %s equals %s" % (1, 1, 2)
print "%15.12f" % 3.14159265358
print "%*.*s" % (7, 5, 'Guido van Rossum')
print ('% 5d' % 10) + '\n' + ('% 5d' % -10)

width = 35
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width
print header_format % (item_width, 'Item', price_width, 'Price')
print '-' * width

print format % (item_width, 'Apples', price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.5)
print format % (item_width, 'Cantaloupes', price_width, 1.92)
print format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8)
print format % (item_width, 'prunes (4 lbs.)', price_width, 12)

print '=' * width

# 字符串方法
index = 'Dried Apricots (16 oz.)'.find('pri')
print index
print 'Dried Apricots (16 oz.)'.find('x')

seq = ['1','2','3','4','5','6']
sep = ' + '
print sep.join(seq)
print 'CHANG XING YE'.lower()
print 'CHANG XING YE'.title()

print 'lixue has B cup'.replace('B', 'D')
print 'lixue xuejj changxy lihhaitang'.split()
print '  *** changxy ***       '.strip()

from string import maketrans
table = maketrans('cs', 'kz')
print 'this is an incredible test'.translate(table)
print 'this is an incredible test'.translate(table, ' ')
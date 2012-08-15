#!/usr/bin/python
# -*- coding: utf-8 -*
# 第二章 列表和元组

edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print "database = " + `database`

greeting = 'Hello'
print greeting[0]
print greeting[-1]

numbers = [0,1,2,3,4,5,6,7,8,9]
print "numbers[3:6] = " + `numbers[3:6]`
print "numbers[3:] = " + `numbers[3:]`
print "numbers[:4] = " + `numbers[:4]`
print "numbers[0:10:2] = " + `numbers[1:10:2]`
print "numbers[::3] = " + `numbers[::3]`

sequence = [None] * 10
print sequence

sentence = "She's a very cute girl!"

screen_width = 80
text_width = len(sentence)
box_width = text_width
left_margin = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+-' + '-' * box_width  + '-+'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '| ' +       sentence   + ' |'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '+-' + '-' * box_width  + '-+'
print

permissions = "rw"
if 'r' in permissions:
    print "r is in permissions"
    print permissions
    print

numbers = [100, 34, 678]
print "numbers = " + `numbers`
print "len(numbers) = " + `len(numbers)`
print "max(numbers) = " + `max(numbers)`
print "min(numbers) = " + `min(numbers)`
print

print "list('Hello') = " + `list('Hello')`
print "''.join(list('Hello')) = " + `''.join(list('Hello'))`
print

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print names
del names[3]
print names
print

name = list("Perl")
name[1:] = list('ython')
print name
name[len(name):] = list(' is fool')
print name
print

lst = [1,2,3]
lst.append(4)
print lst
print

a = [2,9,4]
b = [8,1,6]
a.extend(b)
print a
print a.index(4)
y = a[:]
y.sort()
print y
print

x = ['aaaaaaa','v sdf','acms','hello','xyzxyzxyz']
x.sort()
print x
x.sort(key=len)
print x

team = (42,)
print team
team = tuple(name)
print team

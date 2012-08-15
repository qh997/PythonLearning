#!/usr/bin/python
# -*- coding: utf-8 -*
# 第四章 字典

phonebook = {'changxy' : '8888', 'lixue' : '066', 'xuejj' : '0356'}
print phonebook['lixue']

items = [('name', 'lixue'), ('cup', 'D')]
gl = dict(items)
print gl['name'] + ' : ' + gl['cup']
gl = dict(name = 'lijia', cup = 'C')
print gl['name'] + ' : ' + gl['cup']

print len(gl)

print "lixue's phone number is %(lixue)s." % phonebook
print gl.get('age')

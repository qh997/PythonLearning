#!/usr/bin/python
# -*- coding: utf-8 -*
# 第七章 更加抽象

__metaclass__ = type

class Person:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def greet(self):
        print "Hello world! I'm %s." % self.__name

foo = Person()
bar = Person()

foo.setName('Li Xue')
print foo.getName()
print foo._Person__name

bar.setName('Xue Jia Jia')
bar.greet()

# 超类
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'lixue', 'changxy', 'xuejj', 'guon',])

print 'issubclass(SPAMFilter, Filter) =', issubclass(SPAMFilter, Filter)
print '__bases__ =', SPAMFilter.__bases__
print 'type(s) =', type(s)
print 'isinstance(s, SPAMFilter) =', isinstance(s, SPAMFilter)
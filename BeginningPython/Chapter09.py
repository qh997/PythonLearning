#!/usr/bin/python
# -*- coding: utf-8 -*
# 第九章 魔法方法、属性和迭代器

__metaclass__ = type

class FooBar:
    def __init__(self, name = 'lixue'):
        self.name = name

f = FooBar('changxy')
print f.name

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No. Thanks!'

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk'

    def sing(self):
        print self.sound
        self.hungry = True

sb = SongBird()
sb.sing()
sb.eat()
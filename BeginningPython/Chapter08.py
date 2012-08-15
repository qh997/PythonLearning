#!/usr/bin/python
# -*- coding: utf-8 -*
# 第八章 异常

try:
    x = 46
    y = 0
    print x / y
except (ZeroDivisionError, TypeError), e:
    print e

try:
    print "A simple task"
    #raise TypeError
except:
    print "What? Something went wrong?"
else:
    print "Ah... It went as planned"
finally:
    print "OK, now go on"

# 异常与函数
def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'

handle_exception()

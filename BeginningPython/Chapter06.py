#!/usr/bin/python
# -*- coding: utf-8 -*
# 第六章 抽象

def hello(name = 'changxy'):
    return 'Hello, ' + name + '!'

def fibs(num):
    '获取 Fibonacci 数列'
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-1] + result[-2])
    return result

print hello('lixue')
print fibs(10)
print fibs.__doc__

def inc(x):
    return x + 1

foo = 10
foo = inc(foo)
print foo
print inc(x = 55)
print hello()

def print_params(*params):
    for para in params:
        print para

print_params('xuejj', 'lixue', 'changxy')

def print_params_4(x, y, z = 3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar

print_params_4(1, 2, 3, 'xyz', 'abc', foo = 1, bar = 2)

def multiplier(factor):
    def multiplyByFactor(number):
        return factor * number
    return multiplyByFactor

double = multiplier(2)
print double(5)
print double(7)
print multiplier(3)(9)

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

print factorial(3)

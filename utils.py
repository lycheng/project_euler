#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

import time

def timeit(times=1000):

    def real_decorator(function):

        def wrapper(*args, **kwargs):
            start = time.clock()
            result = 0
            for i in xrange(times):
                result = function()
            end =time.clock()
            print 'result: ', result
            print 'used: %.2fs in %d times' % ((end - start), times)

        return wrapper

    return real_decorator


def is_prime(num):
    num = int(num)
    if num == 1 or num % 2 == 0:
        return False
    if num == 2:
        return True
    upper = num ** 0.5 + 1
    p = 3
    while p < upper:
        if not num % p:
            return False
        p = p + 2
    return True


def gcd(b, s):
    b = max(b, s)
    s = min(b, s)
    if b % s != 0:
        return gcd(s, b % s)
    return s


def factorial(num):
    if num == 0:
        return 1
    rv = num
    for i in range(2, num):
        rv *= i
    return rv


def is_palindromic(num):
    num = str(num)
    return num[:] == num[::-1]

def str_permutation(s):
    ''' 求一个字符串的所有组合 '''
    s = str(s)
    if len(s) == 0:
        return set()
    if len(s) == 1:
        return set([s])
    if len(s) == 2:
        return set([s, s[1]+s[0]])
    rv = set()
    for index in range(len(s)):
        sub_str_permutation = str_permutation("%s%s" % (s[0:index], s[index+1:]))
        for r in sub_str_permutation:
            rv.add(s[index]+r)
    return rv

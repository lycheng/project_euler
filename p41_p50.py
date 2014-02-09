#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit
from utils import is_prime


@timeit(times=1)
def p41():

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
            sub_str_permutation = str_permutation(s[0:index] + s[index+1:])
            for r in sub_str_permutation:
                rv.add(s[index]+r)
        return rv

    digits = ['8', '7', '6', '5', '4', '3', '2', '1']
    while len(digits) >= 2:
        str_num = ''.join(digits)
        rv = sorted(str_permutation(str_num), reverse=True)
        for num in rv:
            if is_prime(int(num)):
                return num
        digits = digits[1:]

    return 0


def run():
    p41()


if __name__ == "__main__":
    run()

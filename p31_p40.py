#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit

@timeit(times=1)
def p31():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for j in range(coin, target+1):
            ways[j] += ways[j - coin]

    return ways[-1]


@timeit(times=1)
def p32():
    def is_pandigital(digits):
        if len(digits) != 9:
            return False
        for i in range(1, 10):
            if str(i) not in digits:
                return False
        return True

    rv = set()
    for i in range(2, 99):
        for j in range(i + 1, 10000):
            digits = "%d%d%d" % (i, j, i * j)
            if len(digits) > 9:
                continue

            if not is_pandigital(digits):
                continue
            rv.add(i * j)

    return sum(rv)


def run():
    p32()


if __name__ == "__main__":
    run()

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


def run():
    p31()


if __name__ == "__main__":
    run()

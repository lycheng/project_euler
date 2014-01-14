#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit, gcd

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


@timeit(times=1)
def p33():

    def check(no, de):
        digit_in_de = {digit for digit in str(denominator)}
        digit_in_no = {digit for digit in str(nominator)}
        same_digit = digit_in_de.intersection(digit_in_no)
        digit_in_de = digit_in_de - same_digit
        digit_in_no = digit_in_no - same_digit

        if "0" in same_digit or len(same_digit) != 1:
            return False

        if not digit_in_de or not digit_in_no or "0" in digit_in_de:
            return False

        if float(digit_in_no.pop()) / float(digit_in_de.pop()) == \
                float(nominator) / float(denominator):
            return True

    target_de = 1
    target_no = 1
    for denominator in range(12, 100):
        for nominator in range(11, denominator):
            if not check(nominator, denominator):
                continue
            target_no *= nominator
            target_de *= denominator

    return target_de / gcd(target_de, target_no)


def run():
    p33()


if __name__ == "__main__":
    run()

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import is_palindromic
from utils import factorial
from utils import is_prime
from utils import timeit
from utils import gcd

from collections import defaultdict
from re import search

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


@timeit(times=1)
def p34():
    target = factorial(9) * 7
    digit_fact = [factorial(i)for i in range(0, 10)]
    result = 0
    for num in range(4, target):
        sum_of_fact = sum([digit_fact[int(digit)]
            for digit in str(num)])

        if sum_of_fact != num:
            continue
        result += sum_of_fact
    return result


@timeit(times=1)
def p35():
    limit = 1000000
    rv = defaultdict(int)
    for num in range(11, limit, 2):
        cur_num = "".join(sorted(str(num)))
        if '5' in cur_num or\
           '0' in cur_num or\
           '2' in cur_num or\
           '4' in cur_num or\
           '6' in cur_num or\
           '8' in cur_num:
            continue
        if not is_prime(num):
            continue
        rv[cur_num] += 1

    count = 5  # 2, 3, 5, 7, 11
    for key, value in rv.items():
        if len(key) == value:
            count += value
    return count


@timeit(times=1)
def p36():
    target = 1000000
    result = 0
    for num in range(target):
        if is_palindromic(num) and is_palindromic("{0:b}".format(num)):
            result += num

    return result


@timeit(times=1)
def p37():
    primes = set([2, 3, 5, 7, 11])
    def is_adv_prime(num):
        if not is_prime(num):
            return False
        primes.add(int(num))
        for i in range(1, len(num)):
            if int(num[0:i]) not in primes:
                return False
            if int(num[-i:]) not in primes:
                return False
        return True

    limit = 1000000
    result = []
    for num in range(13, limit, 2):
        num = str(num)
        if not is_adv_prime(num):
            continue
        result.append(int(num))

    return sum(result)

def run():
    p37()


if __name__ == "__main__":
    run()

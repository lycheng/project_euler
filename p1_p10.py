#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit

def p1():
    print sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


def p2():
    p = 1
    n = 2
    result = 0
    while p < 4000000:
        if not n % 2:
            result += n
        p, n = n, p + n
    print result


@timeit
def p3():
    target = 600851475143
    result = 0
    while target % 2 == 0:
        target = target / 2
        result = 2

    p = 3
    while target != 1:
        while target % p == 0:
            result = p
            target  = target / p
        p = p + 2

    return result


def p4():
    def is_palindromic(num):
        num = str(num)
        return num[:] == num[::-1]

    result = 0
    for i in range(999, 100, -1):
        for j in range(i, 1000):
            num = i * j
            if is_palindromic(num):
                if num > result:
                    result = num

    return result


@timeit
def p5():
    result = 20
    while result % 11 or result % 12 or result % 13 or \
            result % 14 or result % 15 or result % 16 or \
            result % 17 or result % 18 or result % 19 or result % 20:
        result = result + 20
    return result


@timeit
def p5_update():
    result = 20
    for i in range(2, 21):
        if result % i == 0:
            continue

        for j in range(2, 21):
            if (result * j) % i == 0:
                result = result * j
                break

    return result


@timeit(times=100000)
def p6():
    n = 100
    sum_of_squares = sum([(item) * (item) for item in range(1, n + 1)])
    square_of_sum = pow((1 + n) * n / 2, 2)

    return square_of_sum - sum_of_squares


@timeit(times=100000)
def p6_update():
    n = 100
    sum_of_squares = n * (n + 1) * (2 * n + 1) * 1 / 6
    square_of_sum = pow((1 + n) * n / 2, 2)

    return square_of_sum - sum_of_squares


@timeit(times=1)
def p7():

    def is_prime(num):
        p = 3
        while p < num ** 0.5 + 1:
            if not num % p:
                return False
            p = p + 2
        return True

    nth = 10001
    current_prime_count = 2
    current_num = 3

    while current_prime_count <= nth:

        if is_prime(current_num):
            current_prime_count = current_prime_count + 1

        current_num = current_num + 2

    return current_num - 2

def run():
    p7()

if __name__ == "__main__":
    run()

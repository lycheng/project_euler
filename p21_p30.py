#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit

from requests import get
from string import ascii_uppercase

@timeit(times=1)
def p21():

    def get_factors(n):
        rv = set(reduce(list.__add__,
                            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        if n != 1:
            rv.remove(n)
        return rv

    N = 10000
    except_num = set()
    result = 0
    for i in range(1, N + 1):

        if i in except_num:
            continue

        cur_sum = sum(get_factors(i))
        if i != cur_sum and sum(get_factors(cur_sum)) == i:
            result = result + cur_sum + i

            except_num.add(cur_sum)
            except_num.add(i)

    return result


@timeit(times=1)
def p22():

    def get_name_value(name):
        """
        get value of a name
        """
        value = sum([ascii_uppercase.index(letter) + 1
            for letter in name])
        return value

    url = "http://projecteuler.net/project/names.txt"
    try:
        content = get(url, timeout=1).content
    except:
        with open("./problems/p22") as fp:
            content = fp.readline()[0:-1]  # 去除换行符

    names = content[1:-1].split('","')
    names.sort()

    score = 0
    for index, name in enumerate(names):
        score = score + get_name_value(name) * (index + 1)

    return score


@timeit(times=1)
def p23():

    def get_factors(n):
        rv = set(reduce(list.__add__,
                            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        rv.remove(n)
        return rv

    upper_limit = 28123
    abundant_nums = set()
    except_nums = set()

    for i in range(2, upper_limit + 1):
        sum_of_factors = sum(get_factors(i))
        if sum_of_factors > i:
            abundant_nums.add(i)

    for i in abundant_nums:
        for j in abundant_nums:
            except_nums.add(i + j)

    result = 0
    for i in range(upper_limit + 1):
        if i in except_nums:
            continue
        result = result + i

    return result


@timeit(times=1)
def p24():

    target = 1000000 - 1
    num_of_digits = 10

    digits = range(num_of_digits)

    def factorial(n):
        rv = 1
        if n > 0:
            rv = reduce(lambda x, y: x * y, range(1, n+1))
        return rv

    result = []

    while len(digits) > 0:
        f = factorial(len(digits) - 1)
        b = target / f
        result.append(str(digits[b]))
        digits.remove(digits[b])
        target = target % f

    return "".join(result)

def run():
    p24()


if __name__ == "__main__":
    run()

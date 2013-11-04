#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit
from utils import is_prime 

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


@timeit(times=1)
def p25():
    target = 1000
    p, n = 0, 1
    index = 1
    while True:
        p, n = n, p + n
        if len(str(p)) >= target:
            return index
        index = index + 1


@timeit(times=1)
def p26():
    target = 1000

    def get_len(num):
        result = 1
        remainder = 10 % num
        while remainder != 1:
            remainder = (remainder * 10) % num
            result = result + 1
        return result

    result = 0
    max_len = 0
    for num in range(3, target + 1):
        if num % 2 == 0 or num % 5 == 0:
            continue

        len_of_digits = get_len(num)
        if len_of_digits > max_len:
            result = num
            max_len = len_of_digits

    return result


@timeit(times=1)
def p27():

    limit = 1000

    result = 0
    max_count = 0

    for b in range(2, limit):
        if not is_prime(b):
            continue

        for a in range(-b, limit):
            n = 0
            cur_num = n * n + a * n + b
            while cur_num > 0 and is_prime(cur_num):
                n = n + 1
                cur_num = n * n + a * n + b

            if n > max_count:
                max_count = n
                result = a * b

    return result


@timeit(times=1)
def p28():

    limit = 1001 / 2
    result = 1
    for i in range(1, limit + 1):
        r = ((i * 2) + 1) ** 2
        result = result + 4 * r - (i * 2) * 6

    return result


@timeit(times=1)
def p29():

    upper_limit = 100

    result = set()
    for a in range(2, upper_limit + 1):
        for b in range(2, upper_limit + 1):
            result.add(a ** b)
    return len(result)


def run():
    p29()


if __name__ == "__main__":
    run()

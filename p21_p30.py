#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit

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


def run():
    p21()


if __name__ == "__main__":
    run()

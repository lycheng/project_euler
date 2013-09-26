#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit
from datetime import date

@timeit(times=1)
def p11():

    def cal_sub_max_product(m, i, j, x_max, y_max):
        """
        calculate sub matrix product
        """
        result = 0
        if x_max - i >= 4:
            result = max(m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j], result)

        if y_max - j >= 4:
            result = max(m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3], result)

        if x_max - i >= 4 and y_max - j >= 4:
            result = max(m[i][j] * m[i+1][j+1] * m[i+2][j+2] * m[i+3][j+3], result)

        if i >= 3 and y_max - j >= 4:
            result = max(m[i][j] * m[i-1][j+1] * m[i-2][j+2] * m[i-3][j+3], result)

        return result

    matrix = []

    with open("/home/lycheng/p11") as f:
        for line in f:
            nums = map(int, line.split(' '))
            matrix.append(nums)

    result = 0
    x_max = len(matrix)
    for i in xrange(x_max):
        y_max = len(matrix[i])
        for j in xrange(len(matrix[i])):
            result = max(cal_sub_max_product(matrix, i, j, x_max, y_max), result)

    return result


@timeit(times=1)
def p12():

    def get_factors(n):
        return set(reduce(list.__add__,
                            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    n = 1
    m = 2
    while len(get_factors(n + m)) <= 500:
        n, m = n + m, m + 1

    return n + m


@timeit(times=1)
def p12_old():
    def get_factors_num(n):
        count = 2
        if n == 0 or n == 1:
            return 1

        for i in range(2, n / 2 + 1):
            if n % i == 0:
                count = count + 1

        return count

    n = 1
    m = 2
    while get_factors_num(n + m) <= 500:
        n, m = n + m, m + 1

    return n + m

@timeit(times=1)
def p13():
    nums = []
    with open("./problems/p13") as f:
        for line in f:
            nums.append(line[:-1])

    result = 0
    for index in xrange(len(nums[0])):
        result = result * 10
        for num in nums:
            result = result + int(num[index])

        if len(str(result)) >= 14:
            return str(result)[0:10]


@timeit(times=1)
def p14():

    cache = {1: 1}

    def get_len_of_chain(n):
        if n in cache:
            pass
        elif n % 2:
            cache[n] = get_len_of_chain(n * 3 + 1) + 1
        else:
            cache[n] = get_len_of_chain(n / 2) + 1

        return cache[n]

    max_len = 0

    for i in xrange(2, 1000000):
        current_len = get_len_of_chain(i)
        if current_len > max_len:
            max_len = current_len
            result = i

    return result


@timeit(times=1)
def p15():

    grid_len = 20 + 1

    grid = [[1] * (grid_len) for row in range(grid_len)]

    def get_routers(i, j):
        if not i or not j:
            return 1

        return grid[i - 1][j] + grid[i][j - 1]

    for i in range(grid_len):
        for j in range(grid_len):
            grid[i][j] = get_routers(i, j)

    return grid[-1][-1]


@timeit(times=100000)
def p16():

    # rv = sum([int(x) for x in str(2 ** 1000)]) # little faster than generator
    # rv = sum(int(x) for x in str(2 ** 1000))
    rv = reduce(lambda x, y: x + y ,[int(i) for i in str(2 ** 1000)]) # slowest
    return rv


@timeit(times=1)
def p17():

    single = 'one,two,three,four,five,six,seven,eight,nine'.split(',')
    less_than_twenty = 'ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    more_than_twenty = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')

    def get_num_of_letter(num):
        if num == 0:
            return 0

        if num <= 9:
            return len(single[num - 1])

        elif num <= 19:
            return len(less_than_twenty[num - 10])

        elif num <= 99:
            return len(more_than_twenty[num / 10 - 2]) + get_num_of_letter(num % 10)

        elif num >= 100:
            return len(single[num / 100 - 1]) + len('hundred') + len('and') + get_num_of_letter(num % 100)

    total_len = 0
    for num in range(1, 1000):
        total_len = total_len + get_num_of_letter(num)

    total_len = total_len + len('one thousand') - 1
    total_len = total_len - len('and') * 9
    return total_len


@timeit(times=1)
def p18():

    src = []
    with open('problems/p18') as fp:
        for line in fp:
            nums = [int(i) for i in line.split(' ')]
            src.append(nums)

    depth = len(src)
    for i in range(depth - 2, -1, -1):

        for j in range(len(src[i])):
            src[i][j] = max(src[i+1][j], src[i+1][j+1]) + src[i][j]

    return src[0][0]


@timeit(times=1)
def p19():

    beg_year = 1901
    end_year = 2001

    num = 0

    for year in range(beg_year, end_year):
        for month in range(1, 13):
            cur_date = date(year, month, 1)
            if cur_date.isoweekday() == 7:
                num = num + 1

    return num


@timeit(times=1)
def p20():
    n = 100
    return sum([int(s) for s in str(reduce(lambda x, y: x * y, range(1, n + 1)))])


def run():
    p20()


if __name__ == "__main__":
    run()

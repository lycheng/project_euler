#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "lycheng997@gmail.com"

from utils import timeit
from utils import is_prime
from utils import str_permutation

from math import fabs#,sqrt


@timeit(times=1)
def p41():

    digits = ['8', '7', '6', '5', '4', '3', '2', '1']
    while len(digits) >= 2:
        str_num = ''.join(digits)
        rv = sorted(str_permutation(str_num), reverse=True)
        for num in rv:
            if is_prime(int(num)):
                return num
        digits = digits[1:]

    return 0


@timeit(times=1)
def p42():

    fp = open('./problems/p42')
    content = fp.read()

    words = [word[1:-1] for word in content.split(",")]
    max_word_len = 0
    for word in words:
        max_word_len = max(max_word_len, len(word))

    limit = max_word_len * 26
    tri_nums = set()

    for i in range(1, 1000000):
        nth_tri_num = i * (i + 1) / 2
        tri_nums.add(nth_tri_num)
        if nth_tri_num > limit:
            break

    word_count = 0
    for word in words:
        word_val = sum([ord(letter) - ord('A') + 1 for letter in word])
        if word_val in tri_nums:
            word_count += 1

    return word_count

@timeit(times=1)
def p43():

    rv = str_permutation('0123456789')  # 花费 3 / 4 的时间
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]

    result = 0
    for num in rv:
        if num.startswith('0'):
            continue
        is_target = True
        for i in range(1, 8):
            sub_num = int(num[i:i+3])
            if sub_num % divisors[i] > 0:
                is_target = False
                break
        if is_target:
            result += int(num)

    return result


@timeit(times=1)
def p44():

    # def is_pentagonal(num):
        # rv = (sqrt(24 * num + 1) + 1.0) / 6.0
        # return rv == int(rv)

    pentagonal_num = set([1])
    def is_pentagonal(num):
        return num in pentagonal_num

    result = 0
    is_found = False
    n = 2
    while not is_found:
        num = n * (3 * n  - 1) / 2
        for i in range(1, n):
            j = i * (3 * i - 1) / 2
            if is_pentagonal(num - j) and is_pentagonal(fabs(num - j - j)):
                is_found = True
                result = int(fabs(num -j - j))
                break

        pentagonal_num.add(num)
        n += 1

    return result


def run():
    p44()


if __name__ == "__main__":
    run()

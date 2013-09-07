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


@timeit(times=1)
def p8():

    def calculate_product(seq):
        result = 1

        for i in seq:
            result = result * int(i)

        return result

    src = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    sequece = src.split('0')

    result = 0

    for sub_sequence in sequece:
        sub_sequence_len = len(sub_sequence)
        if sub_sequence_len < 5:
            continue

        for i in xrange(len(sub_sequence) - 4):
            current_result = calculate_product(sub_sequence[i:i+5])
            if current_result > result:
                result = current_result

    return result


@timeit(times=1)
def p9():

    target = 1000

    for mid in xrange(2, target / 2 + 1):
        for pre in xrange(1, mid):
            for end in xrange(mid + 1, target):

                if pre + mid + end == 1000:
                    if pre * pre + mid * mid == end * end:
                        return pre * mid * end
    return 0

def run():
    p9()

if __name__ == "__main__":
    run()

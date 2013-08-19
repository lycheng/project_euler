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

def run():
    p5()
    p5_update()

if __name__ == "__main__":
    run()

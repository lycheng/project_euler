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

def run():
    p1()
    p2()

if __name__ == "__main__":
    run()

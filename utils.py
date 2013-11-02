import time

def timeit(times=1000):

    def real_decorator(function):

        def wrapper(*args, **kwargs):
            start = time.clock()
            result = 0
            for i in xrange(times):
                result = function()
            end =time.clock()
            print 'result: ', result
            print 'used: %.2fs in %d times' % ((end - start), times)

        return wrapper

    return real_decorator


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    upper = num ** 0.5 + 1
    p = 3
    while p < upper:
        if not num % p:
            return False
        p = p + 2
    return True

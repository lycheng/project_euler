import time

def timeit(func):
    def wrapper():
        start = time.clock()
        result = 0
        for i in xrange(10):
            result = func()
        end =time.clock()
        print 'result: ', result
        print 'used: %.2fs in 10 times' % (end - start)
    return wrapper

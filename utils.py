import time

def timeit(func):
    def wrapper():
        start = time.clock()
        result = 0
        for i in xrange(10000):
            result = func()
        end =time.clock()
        print 'result: ', result
        print 'used: %f in 10000 times' % (end - start)
    return wrapper

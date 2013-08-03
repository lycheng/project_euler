import time

def timeit(func):
    def wrapper():
        start = time.clock()
        for i in xrange(10000):
            func()
        end =time.clock()
        print 'used: %f in 10000 times' % (end - start)
    return wrapper

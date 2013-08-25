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

import time


class Profiler:
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Время выполнения программы: {:.5f} секунд".format(time.time()-self._startTime))

with Profiler():
    def factorial_rec(n):
        if type(n) != int:
            raise ValueError('ненатуральное число')
        if n == 0:
            return 1
        else:
            return n*factorial_rec(n-1)

    print(factorial_rec(200))

with Profiler():
    def factorial_not_rec(x):
        if type(x) != int:
            raise ValueError('ненатуральное число')

        res = 1
        while x > 0:
            res *= x
            x -= 1
        return res

    print(factorial_not_rec(200))
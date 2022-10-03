from memory_profiler import profile


@profile
def factorial_rec(n):
    if type(n) != int:
        raise ValueError('ненатуральное число')
    if n == 0:
        return 1
    else:
        return n*factorial_rec(n-1)


print(factorial_rec(15))


@profile
def factorial_not_rec(x):
    if type(x) != int:
        raise ValueError('ненатуральное число')
    res = 1
    while x > 0:
        res *= x
        x -= 1
    return res

print(factorial_not_rec(10))
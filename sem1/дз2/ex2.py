def perfect_number(n):
    if type(n) != int:
        raise ValueError
    if n == 0:
        raise ValueError
    s = [i for i in range(1, n//2+1) if not n % i]
    return sum(s) == n

print(perfect_number(1))
print(perfect_number(6))
print(perfect_number(0))

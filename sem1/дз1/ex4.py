x = int(input('Введите число: ',))

res = []
rev_x = -1*x
maxi = max( x,rev_x )
mini = min( x,rev_x )
for i in range( mini,maxi + 1 ):
    if i == 0:
        continue
    if x % i == 0:
        res.append(i)


if len(res) == 4:
    print('число является простым')
else:
    print('число не является простым')
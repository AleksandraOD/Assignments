def rotate(lst):
    if lst == []:
        return lst
    else:
        result = []
        b = lst[-1]
        for element in lst:
            result.append(element)
        result.insert(0, b)
        result.pop(-1)
        return result

l = []
x = int(input("Введите число: ",))
for i in range(0,x+1):
    l.append(int(input('Введите число: ',)))


print(rotate(l))
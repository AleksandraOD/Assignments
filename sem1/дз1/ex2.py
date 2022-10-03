def calc(a,operation,b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b
    else:
        raise ValueError('Неизвестная операция')

a1 = int(input("Введите первое число: ",))
op = input("Введите операцию: ",)
b1 = int(input("Введите второе число: ",))
print(calc(a1, op, b1))
import poly_logic as pl

print("Введите полином. Используйте только цифры и знаки 'x', '+', '-', '^'")
poly = input()
alph = '1234567890-+^x'
for i in poly:
    while i not in alph:
        poly = input("Введите полином корректно ", )
print("Полученная производная: ", pl.derivative(poly))

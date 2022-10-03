from caesar_logic import encrypt, decrypt

print("Если хотите зашифровать слово, введите 'e' ")
print("Если хотите расшифровать слово, введите 'd' ")

x = input()

if x != 'e' and x != 'd':
    raise TypeError("Введено некорректное значение, начните сначала")

text = input("Введите текст латинскими буквами: ", )
offset = int(input("Введите число : ", ))

if offset not in range(-25, 25) or offset == 0:
    raise ValueError('Введено некорректное число, начните сначала')

if x == 'e':
    print("Результат: ", encrypt(offset, text))

if x == 'd':
    print("Результат: ", decrypt(offset, text))

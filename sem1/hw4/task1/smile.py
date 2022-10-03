from smile_logic import is_right

expression = input("Введите строку на проверку: ", )
if is_right(expression) is True:
    print("Скобки расставленны правильно")
else:
    print("Скобки расставленны неправильно")

ln = str(input('Введите строку: ',))
lenght = len(ln)
for i in range(lenght // 2):
    if ln[i] != ln[-1-i]:
     print('Строка не является палиндромом')
    quit()
print('Строка является палиндромом')
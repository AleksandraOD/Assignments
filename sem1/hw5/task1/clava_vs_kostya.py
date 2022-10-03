import random

chance = float(input('Введите вероятность нахождение бага в процентах: '))
t_time = int(input("Введите время прогона тестов в минутах: "))
clava_time = int(input("Введите время работы Клавы в минутах: "))
count = int(input("Введите колличество симуляций: "))
res = ""
fail = None
sum_k = float()
test_count = clava_time // t_time
for i in range(count):
    for j in range(test_count):
        if random.random() <= chance / 100:
            res += "L"
            break
    else:
        if random.random() < chance / 100:
            res += "S"
            sum_k += 1 / count
        else:
            res += "F"
print(res)
print("Вероятность встретить Костю равна ", sum_k)

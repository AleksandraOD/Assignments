T1 = int(input('Введите время наполнения в секундах: '))
T2 = int(input('Введите время передачи в секундах: '))
T3 = int(input('Введите время инъекции в секкундах: '))
attempts_number = int(input('Введите длительность симуляции в секундах: '))
junkie1_fill = False
T_f = 0
T_t = 0
T_i = 0
junkie1_condition = 'N'
junkie2_condition = '.'
junkie1_condition_all = ''
junkie2_condition_all = ''
all_time = 0
time_btw = 0
number = 0
if T1 == 0 or T2 == 0 or T3 == 0:
    raise ValueError("Введите нормальные значения")
for i in range(attempts_number):
    if junkie1_condition == 'p':
        T_f += 1
        if T_f >= T2:
            T_f = 0
            junkie1_condition = 'N'
            junkie1_fill = False
            junkie2_condition = 'I'
            if time_btw > 0:
                all_time += i - time_btw
                number += 1
    if junkie1_condition == 'N':
        T_t += 1
        if T_t > T1:
            junkie1_condition = '.'
            junkie1_fill = True
            T_t = 0
    if junkie2_condition == 'I':
        T_i += 1
        if T_i > T3:
            T_i = 0
            junkie2_condition = '.'
            time_btw = i
    if not junkie1_fill:
        junkie1_condition = 'N'
    if junkie1_fill and junkie2_condition == '.':
        junkie1_condition = 'p'
    junkie1_condition_all += junkie1_condition
    junkie2_condition_all += junkie2_condition
print('1:', junkie1_condition_all, '\n2:', junkie2_condition_all)
if number == 0:
    print('Невозможно определить, увеличьте длительность симуляции')
else:
    print(f'среднее время между инъекциями: {int(all_time / number)}')
# не смогла исправить прошлую версию программы, поэтому полностью новая идея
# в реализации помог одногруппник

"""
2.	Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

fix_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
fix_lst = [i for i in fix_.keys()]

a = list(input('Первое шестнадцатеричное число:\n'))
b = list(input('Второе шестнадцатеричное число:\n'))

a_des = deque([fix_[i] for i in a])
b_des = deque([fix_[i] for i in b])
if len(b_des) > len(a_des):
    len_dif = len(b_des) - len(a_des)
    while len_dif > 0:
        a_des.appendleft(0)
        len_dif -= 1
else:
    len_dif = len(a_des) - len(b_des)
    while len_dif > 0:
        b_des.appendleft(0)
        len_dif -= 1

sum_a_b = [x+y for x, y in zip(a_des, b_des)]

deq_ = deque()
flag_ = 0
for i in sum_a_b[::-1]:
    if i <= 15:
        if flag_:
            deq_.appendleft(fix_lst[i + 1])
            flag_ = 0
        else:
            deq_.appendleft(fix_lst[i])
    else:
        flag_ = 1
        deq_.appendleft(1)

print(f'{a} + {b} = {list(deq_)}')






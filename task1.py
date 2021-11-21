"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти
(укажите какую задачу вы взяли в комментарии);
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.

/////
Выбрана задача: Урок 2. Задача 2.

2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import sys

# Вариант 1.
s = 34560
num_ev = 0
num_non_ev = 0
while s != 0:
    if (s % 10) % 2 and (s % 10) != 0:
        num_non_ev += 1
    else:
        num_ev += 1
    s = s // 10
#  print(num_ev, num_non_ev)

print('Вариант 1')
print(sys.getsizeof(s) + sys.getsizeof(num_ev) + sys.getsizeof(num_non_ev))  # 80

# Вариант 2.
num = [3, 4, 5, 6, 0]
s_ev = [i for i in num if i == 0 or i % 2 == 0]
s_non_ev = [i for i in num if i != 0 and i % 2 != 0]
#  print(len(s_ev), len(s_non_ev))

print('Вариант 2')
print(sys.getsizeof(num) + sys.getsizeof(s_ev) + sys.getsizeof(s_non_ev))  # 296

# Вариант 3.
n_ev = '02468'
c_ev = 0
c_non_ev = 0
t = '34560'
for i in t:
    if i in n_ev:
        c_ev += 1
    else:
        c_non_ev += 1
#  print(c_ev, c_non_ev)

print('Вариант 3')
print(sys.getsizeof(t) + sys.getsizeof(n_ev) + sys.getsizeof(c_ev) + sys.getsizeof(c_non_ev))  # 164

"""
Вывод.
Вариант 1 занимает меньше оперативной памяти за счет типа данных int (самый оптимальный вариант).
Вариант 3 занимает больше оп.памяти, чем вариант 1, за счет типа данных string.
Вариант 2 занимает больше всех оп.памяти за счет списков (счетчик/ссылка/объект)
"""

# ОС Windows 10 Home версия 20H2 сборка 19042.631
# PyCharm 2020.3.3

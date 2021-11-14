
"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать
(укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.


/////
Выбрана задача: Урок 2. Задача 2.

2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import timeit
import cProfile


# Вариант 1. Цикл while
def ev_count_wl(s):
    num_ev = 0
    num_non_ev = 0
    while s != 0:
        if (s % 10) % 2 or (s % 10) == 0:
            num_non_ev += 1
        else:
            num_ev += 1
        s = s // 10
    return num_ev, num_non_ev


# Вариант 2. Рекурсия
def ev_count_rec(a, b, s):
    if s <= 0:
        return a, b

    if s % 10 != 0 and (s % 10) % 2 == 0:
        return ev_count_rec(a + 1, b, s // 10)
    else:
        return ev_count_rec(a, b + 1, s // 10)


# Вариант 3. Списки.
def ev_count_lst(s):
    s = list(s)
    s_ev = [i for i in s if int(i) != 0 and int(i) % 2 == 0]
    s_non_ev = [i for i in s if int(i) == 0 or int(i) % 2 != 0]
    return len(s_ev), len(s_non_ev)


print('I')
num = int('1234' * 10)  # 40 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 0.010915500000000002
num = int('1234' * 20)  # 80 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 0.0161696
num = int('1234' * 30)  # 120 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 0.027573399999999998
num = int('1234' * 100)  # 400 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 0.15246679999999999
num = int('123456789' * 100)  # 900 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 0.5967575
num = int('1234' * 1000)  # 4000 эл-тов
print(timeit.timeit('ev_count_wl(num)', number=1000, globals=globals()))  # 9.999653799999999
cProfile.run('ev_count_wl(num)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 task1.py:28(ev_count_wl)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Вариант 1. Анализ ч/з timeit. Линейная сложность (время). Время увеличивалось прим.пропорционально кол-ву N.
# Анализ ч/з cProfile. Линейная сложность (время).
print('II')
num = 1234  # 4 эл-та
print(timeit.timeit('ev_count_rec(0, 0, num)', number=1000, globals=globals()))  # 0.001058699999999746
num = int(str(num) * 10)  # 40 эл-тов
print(timeit.timeit('ev_count_rec(0, 0, num)', number=1000, globals=globals()))  # 0.015442900000000037
num = int(str(num) * 10)  # 400 эл-тов
print(timeit.timeit('ev_count_rec(0, 0, num)', number=1000, globals=globals()))  # 0.27838090000000015
num = int('123456789' * 100)  # 900 эл-тов
print(timeit.timeit('ev_count_rec(0, 0, num)', number=1000, globals=globals()))  # 0.8484187999999993
cProfile.run('ev_count_rec(0, 0, num)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    901/1    0.002    0.000    0.002    0.002 task1.py:41(ev_count_rec)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Вариант 2. Анализ ч/з timeit. Линейная сложность (время). Время увеличивалось прим.пропорционально кол-ву N.
# Анализ ч/з cProfile. Линейная сложность (время). Кол-во вызовов 901 равно N+1.

print('III')
num = '1234' * 10  # 40 эл-та
print(timeit.timeit('ev_count_lst(num)', number=1000, globals=globals()))  # 0.02994849999999971
num = '1234' * 20  # 80 эл-тов
print(timeit.timeit('ev_count_lst(num)', number=1000, globals=globals()))  # 0.04815870000000011
num = '1234' * 100  # 400 эл-тов
print(timeit.timeit('ev_count_lst(num)', number=1000, globals=globals()))  # 0.243428999999999
num = '123456789' * 100  # 900 эл-тов
print(timeit.timeit('ev_count_lst(num)', number=1000, globals=globals()))  # 0.5459604999999996
num = '1234' * 1000  # 4000 эл-тов
print(timeit.timeit('ev_count_lst(num)', number=1000, globals=globals()))  # 2.4699057999999994
cProfile.run('ev_count_lst(num)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 task1.py:52(ev_count_lst)
        1    0.001    0.001    0.001    0.001 task1.py:54(<listcomp>)
        1    0.001    0.001    0.001    0.001 task1.py:55(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вариант 3. Анализ ч/з timeit. Линейная сложность (время). Время увеличивалось пропорционально кол-ву N.
# # Анализ ч/з cProfile. Линейная сложность (время): list() + list() + 2 len() = O(N) + O(N) + 2 * O(N) = 4 N

"""
Вывод.
Вариант 3 работает быстрее где-то от N=900.
Вариант 1 работает быстрее до N=900.
Вариант 2 работает дольше всех + есть лимит от N=999.
Вариант 3 выгоднее для большого объема данных.
"""

"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2

"""

import timeit
import cProfile

# Вариант 1 - алгоритм «Решето Эратосфена».


def sieve(el):
    s = list(range(500))  # n + 1
    s[1] = 0
    for i in s:
        if i > 1:
            for j in range(i + i, len(s), i):
                s[j] = 0
    while 0 in s:
        s.remove(0)
    return s[el - 1]


#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(timeit.timeit('sieve(3)', number=1000, globals=globals()))   # 0.6394875; для 100 чисел 0.050966899999999996
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.6928784999999998
cProfile.run('sieve(10)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task2.py:29(sieve)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       95    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      405    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
"""


# Вариант 2
def sieve_v(el):
    ls = list(range(2, 500))
    for i in range(2, 500):
        for j in range(2, i):
            if i % j == 0 and i in ls:
                ls.remove(i)
    return ls[el - 1]


print(timeit.timeit('sieve_v(3)', number=1000, globals=globals()))   # 13.351111; для 100 чисел 0.44589629999999997
print(timeit.timeit('sieve_v(10)', number=1000, globals=globals()))  # 13.2594986
cProfile.run('sieve_v(10)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
        1    0.013    0.013    0.013    0.013 task2.py:57(sieve_v)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      403    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
"""

"""
Вариант 1. Линейная сложность. Гораздо быстрее варианта 2.
Вариант 2. Квадратичная сложность.
"""
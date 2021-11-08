"""
6.	В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

min_ = int(input('Диапазон списка от:\n'))
max_ = int(input('До:\n'))
sz = int(input('Размер списка:\n'))
arr = [random.randint(min_, max_) for _ in range(sz)]
min_el = arr[0]
max_el = 0
min_ind = 0
max_ind = 0
for i in range(len(arr)):
    if arr[i] > max_el:
        max_el = arr[i]
        max_ind = i
    if arr[i] < min_el or arr[i] == 0:
        min_el = arr[i]
        min_ind = i
print('Исходный список:')
print(arr)
s = 0
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind
for i in arr[min_ind + 1:max_ind]:
    s += i

print(f'Сумма чисел между позициями {min_ind} и {max_ind}: {s}')

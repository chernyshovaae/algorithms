"""
3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

min_ = int(input('Диапазон списка от:\n'))
max_ = int(input('До:\n'))
sz = int(input('Размер списка:\n'))
arr = [random.randint(min_, max_) for _ in range(sz)]
arr_new = []
min_el = arr[0]
max_el = 0
min_ind = 0
max_ind = 0
for i in range(len(arr)):
    if arr[i] > max_el:
        max_el = arr[i]
        max_ind = i
    if arr[i] < min_el:
        min_el = arr[i]
        min_ind = i
print('Исходный список:')
print(arr)
arr[min_ind], arr[max_ind] = arr[max_ind], arr[min_ind]
print('Новый список:')
print(arr)
